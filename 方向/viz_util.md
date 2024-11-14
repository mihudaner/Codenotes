## show_point

```python
def show_point(*points_list):
    fig = mlab.figure("point", bgcolor=(0, 0, 0), size=(1650, 1500))

    for i, points in enumerate(points_list):
        x = points[:, 0]  # x position of point
        y = points[:, 1]  # y position of point
        z = points[:, 2] + i * 0.01  # z position of point
        colors = [(1, 0, 0), (0, 1, 0), (1, 1, 1)]

        mlab.points3d(x, y, z,
                      scale_factor=0.05 - 0.01 * i,
                      # z,
                      color=colors[i],  # Values used for Color
                      mode="point",
                      # mode="sphere",
                      colormap='spectral',  # 'bone', 'copper', 'gnuplot'
                      # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                      figure=fig,
                      )

    mlab.show()
```



## 显示三类目标的mask

```python
def show_seg(seg_masks, seg_labels):
    mask_r = np.zeros(seg_masks.shape[1:], dtype=bool)
    mask_g = np.zeros(seg_masks.shape[1:], dtype=bool)
    mask_b = np.zeros(seg_masks.shape[1:], dtype=bool)
    for i in range(seg_masks.shape[0]):
        mask = seg_masks[i]
        label = seg_labels[i]
        if label == 0: mask_r = np.logical_or(mask_r, mask)
        if label == 1: mask_g = np.logical_or(mask_g, mask)
        if label == 2: mask_b = np.logical_or(mask_b, mask)

    img_r = np.zeros_like(mask_r, dtype=np.uint8)
    img_r[mask_r] = 255
    img_g = np.zeros_like(mask_g, dtype=np.uint8)
    img_g[mask_g] = 255
    img_b = np.zeros_like(mask_b, dtype=np.uint8)
    img_b[mask_b] = 255

    img = np.stack([img_r, img_g, img_b])
    img = np.transpose(img, (1, 2, 0))
    global sample_idx
    cv2.imshow(sample_idx, img)
    cv2.waitKey(0)
    cv2.destroyWindow(sample_idx)
```



## kitti_util

```python
""" Helper methods for loading and parsing KITTI data.

Author: Charles R. Qi
Date: September 2017
"""
from __future__ import print_function

import numpy as np
import cv2
import os

class Object3d(object):
    ''' 3d object label '''
    def __init__(self, label_file_line):
        data = label_file_line.split(' ')
        print('---data', data)
        data[1:] = [float(x) for x in data[1:]]
        print('---data', data)
        # extract label, truncation, occlusion
        self.type = data[0] # 'Car', 'Pedestrian', ...
        self.truncation = data[1] # truncated pixel ratio [0..1]
        self.occlusion = int(data[2]) # 0=visible, 1=partly occluded, 2=fully occluded, 3=unknown
        self.alpha = data[3] # object observation angle [-pi..pi]

        # extract 2d bounding box in 0-based coordinates
        self.xmin = data[4] # left
        self.ymin = data[5] # top
        self.xmax = data[6] # right
        self.ymax = data[7] # bottom
        self.box2d = np.array([self.xmin,self.ymin,self.xmax,self.ymax])
        
        # extract 3d bounding box information
        self.h = data[8] # box height
        self.w = data[9] # box width
        self.l = data[10] # box length (in meters)
        self.t = (data[11],data[12],data[13]) # location (x,y,z) in camera coord.
        self.ry = data[14] # yaw angle (around Y-axis in camera coordinates) [-pi..pi]

    def print_object(self):
        print('Type, truncation, occlusion, alpha: %s, %d, %d, %f' % \
            (self.type, self.truncation, self.occlusion, self.alpha))
        print('2d bbox (x0,y0,x1,y1): %f, %f, %f, %f' % \
            (self.xmin, self.ymin, self.xmax, self.ymax))
        print('3d bbox h,w,l: %f, %f, %f' % \
            (self.h, self.w, self.l))
        print('3d bbox location, ry: (%f, %f, %f), %f' % \
            (self.t[0],self.t[1],self.t[2],self.ry))


class Calibration(object):
    ''' Calibration matrices and utils
        3d XYZ in <label>.txt are in rect camera coord.
        2d box xy are in image2 coord
        Points in <lidar>.bin are in Velodyne coord.

        y_image2 = P^2_rect * x_rect
        y_image2 = P^2_rect * R0_rect * Tr_velo_to_cam * x_velo
        x_ref = Tr_velo_to_cam * x_velo
        x_rect = R0_rect * x_ref

        P^2_rect = [f^2_u,  0,      c^2_u,  -f^2_u b^2_x;
                    0,      f^2_v,  c^2_v,  -f^2_v b^2_y;
                    0,      0,      1,      0]
                 = K * [1|t]

        image2 coord:
         ----> x-axis (u)
        |
        |
        v y-axis (v)

        velodyne coord:
        front x, left y, up z

        rect/ref camera coord:
        right x, down y, front z

        Ref (KITTI paper): http://www.cvlibs.net/publications/Geiger2013IJRR.pdf

        TODO(rqi): do matrix multiplication only once for each projection.
    '''
    def __init__(self, calib_filepath, from_video=False):
        if from_video:
            calibs = self.read_calib_from_video(calib_filepath)
        else:
            calibs = self.read_calib_file(calib_filepath)
        # Projection matrix from rect camera coord to image2 coord
        self.P = calibs['P2'] 
        self.P = np.reshape(self.P, [3,4])
        """
        [[fu, 0,  cu, -fu*b]
         [0,  fv, cv, 0]
         [0,  0,  1,  0]]
        
        [[ 7.070493e+02  0.000000e+00  6.040814e+02  4.575831e+01]
        [ 0.000000e+00  7.070493e+02  1.805066e+02 -3.454157e-01]
        [ 0.000000e+00  0.000000e+00  1.000000e+00  4.981016e-03]]
        """
        # Rigid transform from Velodyne coord to reference camera coord
        self.V2C = calibs['Tr_velo_to_cam']
        self.V2C = np.reshape(self.V2C, [3, 4])
        self.C2V = inverse_rigid_trans(self.V2C)
        # Rotation from reference camera coord to rect camera coord
        self.R0 = calibs['R0_rect']
        self.R0 = np.reshape(self.R0,[3,3])

        # Camera intrinsics and extrinsics
        # print(self.P)
        self.c_u = self.P[0,2]
        self.c_v = self.P[1,2]
        self.f_u = self.P[0,0]
        self.f_v = self.P[1,1]
        self.b_x = self.P[0,3]/(-self.f_u) # relative 
        self.b_y = self.P[1,3]/(-self.f_v)

    def read_calib_file(self, filepath):
        ''' Read in a calibration file and parse into a dictionary.
        Ref: https://github.com/utiasSTARS/pykitti/blob/master/pykitti/utils.py
        '''
        data = {}
        with open(filepath, 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                if len(line)==0: continue
                key, value = line.split(':', 1)
                # The only non-float values in these files are dates, which
                # we don't care about anyway
                try:
                    data[key] = np.array([float(x) for x in value.split()])
                except ValueError:
                    pass

        return data
    
    def read_calib_from_video(self, calib_root_dir):
        ''' Read calibration for camera 2 from video calib files.
            there are calib_cam_to_cam and calib_velo_to_cam under the calib_root_dir
        '''
        data = {}
        cam2cam = self.read_calib_file(os.path.join(calib_root_dir, 'calib_cam_to_cam.txt'))
        velo2cam = self.read_calib_file(os.path.join(calib_root_dir, 'calib_velo_to_cam.txt'))
        Tr_velo_to_cam = np.zeros((3,4))
        Tr_velo_to_cam[0:3,0:3] = np.reshape(velo2cam['R'], [3,3])
        Tr_velo_to_cam[:,3] = velo2cam['T']
        data['Tr_velo_to_cam'] = np.reshape(Tr_velo_to_cam, [12])
        data['R0_rect'] = cam2cam['R_rect_00']
        data['P2'] = cam2cam['P_rect_02']
        return data

    def cart2hom(self, pts_3d):
        ''' Input: nx3 points in Cartesian
            Oupput: nx4 points in Homogeneous by pending 1
        '''
        n = pts_3d.shape[0]
        pts_3d_hom = np.hstack((pts_3d, np.ones((n,1))))
        return pts_3d_hom
 
    # =========================== 
    # ------- 3d to 3d ---------- 
    # =========================== 
    def project_velo_to_ref(self, pts_3d_velo):
        # print(pts_3d_velo[0])
        pts_3d_velo = self.cart2hom(pts_3d_velo) # nx4
        # print(np.dot(pts_3d_velo, np.transpose(self.V2C))[0])
        # exit()
        return np.dot(pts_3d_velo, np.transpose(self.V2C))

    def project_ref_to_velo(self, pts_3d_ref):
        pts_3d_ref = self.cart2hom(pts_3d_ref) # nx4
        return np.dot(pts_3d_ref, np.transpose(self.C2V))

    def project_rect_to_ref(self, pts_3d_rect):
        ''' Input and Output are nx3 points '''
        return np.transpose(np.dot(np.linalg.inv(self.R0), np.transpose(pts_3d_rect)))
    
    def project_ref_to_rect(self, pts_3d_ref):
        ''' Input and Output are nx3 points '''
        return np.transpose(np.dot(self.R0, np.transpose(pts_3d_ref)))
 
    def project_rect_to_velo(self, pts_3d_rect):
        ''' Input: nx3 points in rect camera coord.
            Output: nx3 points in velodyne coord.
        ''' 
        pts_3d_ref = self.project_rect_to_ref(pts_3d_rect)
        return self.project_ref_to_velo(pts_3d_ref)

    def project_velo_to_rect(self, pts_3d_velo):
        pts_3d_ref = self.project_velo_to_ref(pts_3d_velo)
        # print('ref coord.', pts_3d_ref[0])
        return self.project_ref_to_rect(pts_3d_ref)

    # =========================== 
    # ------- 3d to 2d ---------- 
    # =========================== 
    def project_rect_to_image(self, pts_3d_rect):
        ''' Input: nx3 points in rect camera coord.
            Output: nx2 points in image2 coord.
        '''
        pts_3d_rect = self.cart2hom(pts_3d_rect)
        pts_2d = np.dot(pts_3d_rect, np.transpose(self.P)) # nx3
        pts_2d[:,0] /= pts_2d[:, 2]
        pts_2d[:,1] /= pts_2d[:, 2]
        return pts_2d[:,0:2]
    
    def project_velo_to_image(self, pts_3d_velo):
        ''' Input: nx3 points in velodyne coord.
            Output: nx2 points in image2 coord.
        '''
        pts_3d_rect = self.project_velo_to_rect(pts_3d_velo)   # velo coord. -> camera coord.
        return self.project_rect_to_image(pts_3d_rect)

    # =========================== 
    # ------- 2d to 3d ---------- 
    # =========================== 
    def project_image_to_rect(self, uv_depth):
        ''' Input: nx3 first two channels are uv, 3rd channel
                   is depth in rect camera coord.
            Output: nx3 points in rect camera coord.
        '''
        # print('---uv_depth.shape', uv_depth.shape)
        # print('---uv_depth', uv_depth)
        n = uv_depth.shape[0]
        x = ((uv_depth[:,0]-self.c_u)*uv_depth[:,2])/self.f_u + self.b_x
        y = ((uv_depth[:,1]-self.c_v)*uv_depth[:,2])/self.f_v + self.b_y
        pts_3d_rect = np.zeros((n,3))
        pts_3d_rect[:,0] = x
        pts_3d_rect[:,1] = y
        pts_3d_rect[:,2] = uv_depth[:,2]
        return pts_3d_rect

    def project_image_to_velo(self, uv_depth):
        pts_3d_rect = self.project_image_to_rect(uv_depth)
        return self.project_rect_to_velo(pts_3d_rect)

 
def rotx(t):
    ''' 3D Rotation about the x-axis. '''
    c = np.cos(t)
    s = np.sin(t)
    return np.array([[1,  0,  0],
                     [0,  c, -s],
                     [0,  s,  c]])


def roty(t):
    ''' Rotation about the y-axis. '''
    c = np.cos(t)
    s = np.sin(t)
    return np.array([[c,  0,  s],
                     [0,  1,  0],
                     [-s, 0,  c]])


def rotz(t):
    ''' Rotation about the z-axis. '''
    c = np.cos(t)
    s = np.sin(t)
    return np.array([[c, -s,  0],
                     [s,  c,  0],
                     [0,  0,  1]])


def transform_from_rot_trans(R, t):
    ''' Transforation matrix from rotation matrix and translation vector. '''
    R = R.reshape(3, 3)
    t = t.reshape(3, 1)
    return np.vstack((np.hstack([R, t]), [0, 0, 0, 1]))


def inverse_rigid_trans(Tr):
    ''' Inverse a rigid body transform matrix (3x4 as [R|t])
        [R'|-R't; 0|1]
    '''
    inv_Tr = np.zeros_like(Tr) # 3x4
    inv_Tr[0:3,0:3] = np.transpose(Tr[0:3,0:3])
    inv_Tr[0:3,3] = np.dot(-np.transpose(Tr[0:3,0:3]), Tr[0:3,3])
    return inv_Tr

def read_label(label_filename):
    print('---label_filename', label_filename)
    lines = [line.rstrip() for line in open(label_filename)]
    print('---lines', lines)
    objects = [Object3d(line) for line in lines]
    return objects

def load_image(img_filename):
    return cv2.imread(img_filename)

def load_velo_scan(velo_filename):
    scan = np.fromfile(velo_filename, dtype=np.float32)
    scan = scan.reshape((-1, 4))
    return scan

def project_to_image(pts_3d, P):
    ''' Project 3d points to image plane.

    Usage: pts_2d = projectToImage(pts_3d, P)
      input: pts_3d: nx3 matrix
             P:      3x4 projection matrix
      output: pts_2d: nx2 matrix

      P(3x4) dot pts_3d_extended(4xn) = projected_pts_2d(3xn)
      => normalize projected_pts_2d(2xn)

      <=> pts_3d_extended(nx4) dot P'(4x3) = projected_pts_2d(nx3)
          => normalize projected_pts_2d(nx2)
    '''
    n = pts_3d.shape[0]
    pts_3d_extend = np.hstack((pts_3d, np.ones((n,1))))
    #print(('pts_3d_extend shape: ', pts_3d_extend.shape))
    pts_2d = np.dot(pts_3d_extend, np.transpose(P)) # nx3
    pts_2d[:,0] /= pts_2d[:,2]
    pts_2d[:,1] /= pts_2d[:,2]
    return pts_2d[:,0:2]


def compute_box_3d(obj, P):
    ''' Takes an object and a projection matrix (P) and projects the 3d
        bounding box into the image plane.
        Returns:
            corners_2d: (8,2) array in left image coord.
            corners_3d: (8,3) array in in rect camera coord.
    '''
    # compute rotational matrix around yaw axis
    R = roty(obj.ry)    

    # 3d bounding box dimensions
    l = obj.l;
    w = obj.w;
    h = obj.h;
    
    # 3d bounding box corners
    x_corners = [l/2,l/2,-l/2,-l/2,l/2,l/2,-l/2,-l/2];
    y_corners = [0,0,0,0,-h,-h,-h,-h];
    z_corners = [w/2,-w/2,-w/2,w/2,w/2,-w/2,-w/2,w/2];
    
    # rotate and translate 3d bounding box
    corners_3d = np.dot(R, np.vstack([x_corners,y_corners,z_corners]))
    #print corners_3d.shape
    corners_3d[0,:] = corners_3d[0,:] + obj.t[0];
    corners_3d[1,:] = corners_3d[1,:] + obj.t[1];
    corners_3d[2,:] = corners_3d[2,:] + obj.t[2];
    #print 'cornsers_3d: ', corners_3d 
    # only draw 3d bounding box for objs in front of the camera
    if np.any(corners_3d[2,:]<0.1):
        corners_2d = None
        return corners_2d, np.transpose(corners_3d)
    
    # project the 3d bounding box into the image plane
    print(corners_3d.shape)   # (3, 8)
    print(np.transpose(corners_3d).shape)  # (8, 3)
    corners_2d = project_to_image(np.transpose(corners_3d), P);
    #print 'corners_2d: ', corners_2d
    return corners_2d, np.transpose(corners_3d)


def compute_orientation_3d(obj, P):
    ''' Takes an object and a projection matrix (P) and projects the 3d
        object orientation vector into the image plane.
        Returns:
            orientation_2d: (2,2) array in left image coord.
            orientation_3d: (2,3) array in in rect camera coord.
    '''
    
    # compute rotational matrix around yaw axis
    R = roty(obj.ry)
   
    # orientation in object coordinate system
    orientation_3d = np.array([[0.0, obj.l],[0,0],[0,0]])
    
    # rotate and translate in camera coordinate system, project in image
    orientation_3d = np.dot(R, orientation_3d)
    orientation_3d[0,:] = orientation_3d[0,:] + obj.t[0]
    orientation_3d[1,:] = orientation_3d[1,:] + obj.t[1]
    orientation_3d[2,:] = orientation_3d[2,:] + obj.t[2]
    
    # vector behind image plane?
    if np.any(orientation_3d[2,:]<0.1):
      orientation_2d = None
      return orientation_2d, np.transpose(orientation_3d)
    
    # project orientation into the image plane
    orientation_2d = project_to_image(np.transpose(orientation_3d), P);
    return orientation_2d, np.transpose(orientation_3d)

def draw_projected_box3d(image, qs, color=(255,255,255), thickness=2):
    ''' Draw 3d bounding box in image
        qs: (8,3) array of vertices for the 3d box in following order:
            1 -------- 0
           /|         /|
          2 -------- 3 .
          | |        | |
          . 5 -------- 4
          |/         |/
          6 -------- 7
    '''
    qs = qs.astype(np.int32)
    for k in range(0,4):
       # Ref: http://docs.enthought.com/mayavi/mayavi/auto/mlab_helper_functions.html
       i,j=k,(k+1)%4
       # use LINE_AA for opencv3
       cv2.line(image, (qs[i,0],qs[i,1]), (qs[j,0],qs[j,1]), color, thickness, cv2.LINE_AA)

       i,j=k+4,(k+1)%4 + 4
       cv2.line(image, (qs[i,0],qs[i,1]), (qs[j,0],qs[j,1]), color, thickness, cv2.LINE_AA)

       i,j=k,k+4
       cv2.line(image, (qs[i,0],qs[i,1]), (qs[j,0],qs[j,1]), color, thickness, cv2.LINE_AA)
    return image

```

### import kitti_util as utils

```c
def show_image_with_boxes(img, objects, calib, show3d=True):
    ''' Show image with 2D bounding boxes '''
    img1 = np.copy(img) # for 2d bbox
    img2 = np.copy(img) # for 3d bbox
    print('---objects', objects)
    for obj in objects:
        if obj.type=='DontCare':continue
        cv2.rectangle(img1, (int(obj.xmin),int(obj.ymin)),
            (int(obj.xmax),int(obj.ymax)), (0,255,0), 2)
        box3d_pts_2d, box3d_pts_3d = utils.compute_box_3d(obj, calib.P)
        img2 = utils.draw_projected_box3d(img2, box3d_pts_2d)
    # Image.fromarray(img1).show()
    if show3d:
        Image.fromarray(img2).show()
```

## 统计图

```c
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


def count(a, n, ranges):
    arr = [0] * n
    dis = [i for i in range(0, n * (ranges // n), (ranges // n))]
    for x in a:
        idx = -1
        for i in range(len(dis)):
            if x > dis[i]: idx += 1
        arr[idx] += 1
    return arr


def plot_clonm_mult(x1, y1, x2, y2,  label_x, label_y, title):
    """
    miss_dist, miss_pts_num,
    detected_dist, detected_pts_num,
    "距离", "box内点数", "丢失目标"
    """
    # 创建示例数据
    scores_group1 = np.array([8, 7, 5, 6, 9, 7, 6, 8, 9, 10])
    scores_group2 = np.array([7, 6, 4, 5, 8, 6, 5, 7, 8, 9])
    scores_group1 = count(x1, 10, 50)
    scores_group2 = count(x2, 10, 50)

    x = [i for i in range(0, 50, 5)]  # 创建分数区间
    x = np.asarray(x, dtype=float)
    # 绘制柱状图
    bar_width = 0.8
    plt.bar(x, scores_group1, width=bar_width, label='漏检', align='center')
    plt.bar(x + bar_width, scores_group2, width=bar_width, label='成功检测', align='center')

    # 在每个柱子上添加标签
    for i, score in enumerate(scores_group1):
        plt.text(x[i], score, str(score), ha='center', va='bottom')
    for i, score in enumerate(scores_group2):
        plt.text(x[i] + bar_width, score, str(score), ha='center', va='bottom')

    # 设置图形标签和标题
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(title)
    plt.xticks(x + bar_width / 2, x)  # 设置x轴标签

    # 添加图例
    plt.legend()

    # 显示图形
    plt.show()
    pass


def plot_clonm():
    # 柱状图数据
    labels = ['>10%', '>20%', '>30%', '>40%', '>50%', '>60%', '>70%', '>80%', '>90%']
    data = [0, 0, 75, 28, 5, 4, 0, 2, 0]  # 每个部分的大小，可以是整数或浮点数
    colors = plt.cm.viridis(np.linspace(0, 1, len(labels)))
    # 创建柱状图
    plt.figure(figsize=(10, 6))  # 设置图形大小
    bars = plt.bar(labels, data, color=colors)
    # plt.bar(labels, data, color='blue')
    sum1 = 0
    for i in data:
        sum1 += i
    print(sum1)
    # 可选：添加标题和轴标签
    plt.title('car')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.ylim(0, 80)
    # 显示图形
    plt.xticks(rotation=45)  # 旋转 x 轴标签以便更好地显示
    plt.tight_layout()  # 调整布局以避免标签重叠
    plt.show()


def plot_scatter(x1, y1, x2, y2, label_x, label_y, title):
    # 创建散点图
    plt.scatter(x1, y1, s=1, c='b')
    plt.scatter(x2, y2, s=1, c='r')
    # 添加标签和标题
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.xlim(-10, 80)
    plt.title(title)

    # 显示图形
    plt.show()




if __name__ == "__main__":
    # 示例数据
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 1, 3, 7]
    plot_clonm_mult(0, 0, 0, 0, "为", "pts_num", "miss")

```

## yolo绘制box

```c
def plot_one_box(x, img, color=None, label=None, line_thickness=3):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
```

## sam绘制mask

```c
def show_mask(mask, ax, random_color=False):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30/255, 144/255, 255/255, 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)
    
def show_points(coords, labels, ax, marker_size=375):
    pos_points = coords[labels==1]
    neg_points = coords[labels==0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)   
    
def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0,0,0,0), lw=2))    
```



## 读取点云文件

```c
def show_np_o3d(point_cloud_data):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(point_cloud_data[:, :3])  # 只使用前三列作为坐标
    o3d.visualization.draw_geometries([pcd])


def load_binary_point_cloud(file_path, show=False):
    """
    加载点云bin为返回o3d.pcd
    :param file_path: 
    :param show: 
    :return: 
    """
    point_cloud_data = np.fromfile(file_path, dtype=np.float32, count=-1).reshape([-1, 4])

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(point_cloud_data[:, :3])  # 只使用前三列作为坐标
    if show: o3d.visualization.draw_geometries([pcd])
    return pcd


def load_ply_point_cloud(file_path, show=False):
    """
    加载点云Ply返回o3d.pcd
    :param file_path:
    :param show:
    :return:
    """
    pcd = o3d.io.read_point_cloud(file_path)
    if show: o3d.visualization.draw_geometries([pcd])
    return pcd


def save_point_cloud_as_ply(file_path, point_cloud):
    """
    o3d.pcd保存为ply
    :param file_path:
    :param point_cloud:
    :return:
    """
    o3d.io.write_point_cloud(file_path, point_cloud)


def save_point_cloud_as_bin(file_path, point_cloud):
    """
    o3d.pcd保存为bin
    :param file_path:
    :param point_cloud:
    :return:
    """
    # 获取点云数据
    points = np.asarray(point_cloud.points)

    # 创建一个新的点云数据，将反射率设置为0
    num_points = points.shape[0]
    reflectance = np.zeros((num_points, 1), dtype=np.float32)
    point_cloud_data = np.hstack((points, reflectance))
    # 将点云数据保存为二进制文件
    with open(file_path, 'wb') as f:
        point_cloud_data.astype(np.float32).tofile(f)


def Kitti_bin2ply():
    """
    批量bin保存为ply
    :return:
    """
    for i in range(511, 512):
        # 指定二进制点云文件路径
        input_file_path = r"G:\dataset\kitti\object\testing\velodyne\%06d.bin" % i

        # 指定要保存的 PLY 文件路径
        output_file_path = r"C:\Users\33567\Desktop\car_model\%06d.ply" % i

        # 加载二进制点云文件
        point_cloud = load_binary_point_cloud(input_file_path)

        # 将点云保存为 PLY 文件
        save_point_cloud_as_ply(output_file_path, point_cloud)

        print(f"点云{i}已保存为 {output_file_path}")


def ply_save2bin(ply_file_path, bin_file_path):
    """

    :param ply_file_path:
    :param bin_file_path:
    :return:
    """
    pts = load_ply_point_cloud(ply_file_path)
    save_point_cloud_as_bin(bin_file_path, pts)


def conver_ply2bin(search_directory):
    """
    目录下所有的ply文件ply_save2bin
    :param search_directory:
    :return:
    """
    # 遍历目录下的所有文件和子目录
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            if file.endswith('.ply'):
                ply_file_path = os.path.join(root, file)
                bin_file_path = os.path.join(root, file.replace('.ply', '.bin'))

                # 检查同名的 .bin 文件是否存在
                if not os.path.exists(bin_file_path):
                    ply_save2bin(ply_file_path, bin_file_path)
```

## fusion_yolo_seg

```c
import numpy as np
import torch
from pathlib import Path
import os
import random
from tqdm import tqdm
from mayavi import mlab
import cv2

global sample_idx


def get_idx(i):
    # 用于指定文件路径
    file_path = "../car_model/train.txt"  # 替换成您的文件路径 #3712
    # file_path = "./val.txt"  # 替换成您的文件路径 #3769
    file = open(file_path, 'r')
    lines = file.readlines()
    if i <= len(lines):
        line = lines[i - 1]  # Python中的列表索引从0开始，所以要减1
        number = int(line.strip())  # 去除空白符并转为整数
        print("get_idx:", number)
        return number
    else:
        print("行数超出文件范围")


def plot_one_box(x, img, color=None, label=None, line_thickness=3):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 4, thickness=tf * 3)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 4, [225, 255, 255], thickness=tf * 3, lineType=cv2.LINE_AA)
    return img


def show_seg(segment_masks, segment_labels, img):
    mask_r = np.zeros(segment_masks.shape[1:], dtype=bool)
    mask_g = np.zeros(segment_masks.shape[1:], dtype=bool)
    mask_b = np.zeros(segment_masks.shape[1:], dtype=bool)
    for i in range(segment_masks.shape[0]):
        mask = segment_masks[i]
        label = segment_labels[i]
        if label == 0: mask_r = np.logical_or(mask_r, mask)
        if label == 1: mask_g = np.logical_or(mask_g, mask)
        if label == 2: mask_b = np.logical_or(mask_b, mask)

    # img_r = np.zeros_like(mask_r, dtype=np.uint8)
    img_r = img[:, :, 0]
    img_r[mask_r] = 255
    img_g = img[:, :, 1]
    img_g[mask_g] = 255
    img_b = img[:, :, 2]
    img_b[mask_b] = 255

    img = np.stack([img_r, img_g, img_b])
    img = np.transpose(img, (1, 2, 0))
    global sample_idx
    cv2.imshow(sample_idx, img)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyWindow(sample_idx)


# def fusion_v1(seg_masks):
#     # 直接把mask和yolo mask相与不对
#     mask_path = os.path.join("/home/wangkai/yolov7/runs/detect/yolomask", '%s.npy' % sample_idx)
#     yolo_mask = np.load(mask_path)
#     yolo_mask = np.tile(yolo_mask, (seg_masks.shape[0], 1, 1))  # 拷贝n个
#     seg_masks = np.logical_and(seg_masks, yolo_mask)
#     return seg_masks


def caliou(seg_mask, gtbox):
    target_pixels = np.where(seg_mask)

    # 找到目标的最上、下、左、右边界
    y_min, x_min = np.min(target_pixels, axis=1)
    y_max, x_max = np.max(target_pixels, axis=1)

    # 从gtbox中获取真实边界框的坐标
    gt_x1, gt_y1, gt_x2, gt_y2, _, _ = gtbox

    # 计算交集部分的坐标
    inter_x1 = max(x_min, gt_x1)
    inter_y1 = max(y_min, gt_y1)
    inter_x2 = min(x_max, gt_x2)
    inter_y2 = min(y_max, gt_y2)

    # 计算交集面积
    intersection_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)

    # 计算目标和gtbox的面积
    target_area = (x_max - x_min) * (y_max - y_min)
    gtbox_area = (gt_x2 - gt_x1) * (gt_y2 - gt_y1)

    # 计算IoU
    iou = intersection_area / (target_area + gtbox_area - intersection_area)

    return iou


def fusion_v2(segment_masks, segment_labels, yolov7_labels):
    # n*[x1,y1,x2,y2,cof,class]
    del_idx = []
    yolov7_labels_flag = [False] * len(yolov7_labels)
    for i, mask in enumerate(segment_masks):
        ishave = False
        for j in range(len(yolov7_labels)):
            yolo_label = yolov7_labels[j]
            if (not yolov7_labels_flag[j]) and caliou(mask, yolo_label) > 0.5:
                yolov7_labels_flag[j] = True
                ishave = True
        if not ishave:
            del_idx.append(i)
    return np.delete(segment_masks, del_idx, axis=0), np.delete(segment_labels, del_idx, axis=0)


if __name__ == "__main__":
    global sample_idx
    root_split_path = "/media/wangkai/ROG/object_threetypes/training/"
    label_path = "/media/wangkai/ROG/Direction_code/yolov7/runs/detect/yololabel"
    out_path = "/media/wangkai/ROG/object_threetypes/training/middle_database/seg_2_01234xyolo"
    for idx in range(2015, 3713):
        idx = get_idx(idx)
        sample_idx = "%06d" % idx
        seg_file_path = '/media/wangkai/ROG/object_threetypes/training/middle_database/seg_2_01234/' + '%s.npy' % sample_idx
        seg_obj = np.load(seg_file_path, allow_pickle=True).item()  # 看看作者的加载npy字典的方法
        seg_masks = seg_obj['masks']  # [n,h,w]      #
        seg_labels = seg_obj['labels']  # [n]

        yolo_path = os.path.join(label_path, '%s.npy' % sample_idx)
        if seg_masks is None or not os.path.exists(yolo_path):
            seg_obj = {
                'masks': seg_masks,
                'labels': np.array(seg_labels),
                # 'scores': scores.cpu().numpy()
            }
            # np.save(os.path.join(out_path, '%s.npy' % sample_idx), seg_obj)
            continue

        yolo_labels = np.load(yolo_path)


        # 显示原始RGB
        rgb = cv2.imread(root_split_path + 'image_2/%s.png' % sample_idx)
        cv2.imshow(sample_idx, rgb)
        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'): break
        cv2.destroyWindow(sample_idx)

        # 显示原始分割结果
        _rgb = rgb.copy()
        show_seg(seg_masks, seg_labels, _rgb)

        # 显示结合YOLO的结果
        _rgb = rgb.copy()
        _rgb2 = rgb.copy()
        for xyxy in yolo_labels:
            if int(xyxy[5] > 2): continue
            _rgb = plot_one_box(xyxy, _rgb, line_thickness=3)
        show_seg(seg_masks, seg_labels, _rgb)

        seg_masks, seg_labels = fusion_v2(seg_masks, seg_labels, yolo_labels)
        if len(seg_masks) < 0:
            seg_masks = None
            seg_labels = []

        # 显示结合YOLO的结果
        for xyxy in yolo_labels:
            if int(xyxy[5] > 2): continue
            _rgb2 = plot_one_box(xyxy, _rgb2, line_thickness=3)
        show_seg(seg_masks, seg_labels, _rgb2)

        seg_obj = {
            'masks': seg_masks,
            'labels': np.array(seg_labels),
            # 'scores': scores.cpu().numpy()
        }
        # np.save(os.path.join(out_path, '%s.npy' % sample_idx), seg_obj)
        continue

```

## ONCE

### once.py

```python
import json
import functools
import os.path as osp
from collections import defaultdict
import cv2
import numpy as np
from scipy.spatial.transform import Rotation


def split_info_loader_helper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        split_file_path = func(*args, **kwargs)
        if not osp.isfile(split_file_path):
            split_list = []
        else:
            split_list = set(map(lambda x: x.strip(), open(split_file_path).readlines()))
        return split_list

    return wrapper


class ONCE(object):
    """
    dataset structure:
    - data_root
        -ImageSets
            - train_split.txt
            - val_split.txt
            - test_split.txt
            - raw_split.txt
        - data
            - seq_id
                - cam01
                - cam03
                - ...
                -
    """
    camera_names = ['cam01', 'cam03', 'cam05', 'cam06', 'cam07', 'cam08', 'cam09']
    camera_tags = ['top', 'top2', 'left_back', 'left_front', 'right_front', 'right_back', 'back']

    def __init__(self, dataset_root):
        self.dataset_root = dataset_root
        self.data_root = osp.join(self.dataset_root, 'data')
        self._collect_basic_infos()

    @property
    @split_info_loader_helper
    def train_split_list(self):
        return osp.join(self.dataset_root, 'ImageSets', 'train.txt')

    @property
    @split_info_loader_helper
    def val_split_list(self):
        return osp.join(self.dataset_root, 'ImageSets', 'val.txt')

    @property
    @split_info_loader_helper
    def test_split_list(self):
        return osp.join(self.dataset_root, 'ImageSets', 'test.txt')

    @property
    @split_info_loader_helper
    def raw_small_split_list(self):
        return osp.join(self.dataset_root, 'ImageSets', 'raw_small.txt')

    @property
    @split_info_loader_helper
    def raw_medium_split_list(self):
        return osp.join(self.dataset_root, 'ImageSets', 'raw_medium.txt')

    @property
    @split_info_loader_helper
    def raw_large_split_list(self):
        return osp.join(self.dataset_root, 'ImageSets', 'raw_large.txt')

    def _find_split_name(self, seq_id):
        if seq_id in self.raw_small_split_list:
            return 'raw_small'
        elif seq_id in self.raw_medium_split_list:
            return 'raw_medium'
        elif seq_id in self.raw_large_split_list:
            return 'raw_large'
        if seq_id in self.train_split_list:
            return 'train'
        if seq_id in self.test_split_list:
            return 'test'
        if seq_id in self.val_split_list:
            return 'val'
        print("sequence id {} corresponding to no split".format(seq_id))
        raise NotImplementedError

    def _collect_basic_infos(self):
        self.train_info = defaultdict(dict)
        self.val_info = defaultdict(dict)
        self.test_info = defaultdict(dict)
        self.raw_small_info = defaultdict(dict)
        self.raw_medium_info = defaultdict(dict)
        self.raw_large_info = defaultdict(dict)

        for attr in ['train', 'val', 'test', 'raw_small', 'raw_medium', 'raw_large']:
            if getattr(self, '{}_split_list'.format(attr)) is not None:
                split_list = getattr(self, '{}_split_list'.format(attr))
                info_dict = getattr(self, '{}_info'.format(attr))
                for seq in split_list:
                    anno_file_path = osp.join(self.data_root, seq, '{}.json'.format(seq))
                    if not osp.isfile(anno_file_path):
                        print("no annotation file for sequence {}".format(seq))
                        raise FileNotFoundError
                    anno_file = json.load(open(anno_file_path, 'r'))
                    frame_list = list()
                    for frame_anno in anno_file['frames']:
                        frame_list.append(str(frame_anno['frame_id']))
                        info_dict[seq][frame_anno['frame_id']] = {
                            'pose': frame_anno['pose'],
                        }
                        info_dict[seq][frame_anno['frame_id']]['calib'] = dict()
                        for cam_name in self.__class__.camera_names:
                            info_dict[seq][frame_anno['frame_id']]['calib'][cam_name] = {
                                'cam_to_velo': np.array(anno_file['calib'][cam_name]['cam_to_velo']),
                                'cam_intrinsic': np.array(anno_file['calib'][cam_name]['cam_intrinsic']),
                                'distortion': np.array(anno_file['calib'][cam_name]['distortion'])
                            }
                        if 'annos' in frame_anno.keys():
                            info_dict[seq][frame_anno['frame_id']]['annos'] = frame_anno['annos']
                    info_dict[seq]['frame_list'] = sorted(frame_list)

    def get_frame_anno(self, seq_id, frame_id):
        split_name = self._find_split_name(seq_id)
        frame_info = getattr(self, '{}_info'.format(split_name))[seq_id][frame_id]
        if 'annos' in frame_info:
            return frame_info['annos']
        return None

    def load_point_cloud(self, seq_id, frame_id):
        bin_path = osp.join(self.data_root, seq_id, 'lidar_roof', '{}.bin'.format(frame_id))
        points = np.fromfile(bin_path, dtype=np.float32).reshape(-1, 4)
        return points

    def load_image(self, seq_id, frame_id, cam_name):
        cam_path = osp.join(self.data_root, seq_id, cam_name, '{}.jpg'.format(frame_id))
        img_buf = cv2.cvtColor(cv2.imread(cam_path), cv2.COLOR_BGR2RGB)
        return img_buf

    def undistort_image(self, seq_id, frame_id):
        img_list = []
        split_name = self._find_split_name(seq_id)
        frame_info = getattr(self, '{}_info'.format(split_name))[seq_id][frame_id]
        for cam_name in self.__class__.camera_names:
            img_buf = self.load_image(seq_id, frame_id, cam_name)
            cam_calib = frame_info['calib'][cam_name]
            h, w = img_buf.shape[:2]
            cv2.getOptimalNewCameraMatrix(cam_calib['cam_intrinsic'],
                                          cam_calib['distortion'],
                                          (w, h), alpha=0.0, newImgSize=(w, h))
            img_list.append(cv2.undistort(img_buf, cam_calib['cam_intrinsic'],
                                          cam_calib['distortion'],
                                          newCameraMatrix=cam_calib['cam_intrinsic']))
        return img_list

    def undistort_image_v2(self, seq_id, frame_id):
        img_list = []
        new_cam_intrinsic_dict = dict()
        split_name = self._find_split_name(seq_id)
        frame_info = getattr(self, '{}_info'.format(split_name))[seq_id][frame_id]
        for cam_name in self.__class__.camera_names:
            img_buf = self.load_image(seq_id, frame_id, cam_name)
            cam_calib = frame_info['calib'][cam_name]
            h, w = img_buf.shape[:2]
            new_cam_intrinsic, _ = cv2.getOptimalNewCameraMatrix(cam_calib['cam_intrinsic'],
                                                                 cam_calib['distortion'],
                                                                 (w, h), alpha=0.0, newImgSize=(w, h))
            img_list.append(cv2.undistort(img_buf, cam_calib['cam_intrinsic'],
                                          cam_calib['distortion'],
                                          newCameraMatrix=new_cam_intrinsic))
            new_cam_intrinsic_dict[cam_name] = new_cam_intrinsic
        return img_list, new_cam_intrinsic_dict

    def project_lidar_to_image(self, seq_id, frame_id):
        points = self.load_point_cloud(seq_id, frame_id)

        split_name = self._find_split_name(seq_id)
        frame_info = getattr(self, '{}_info'.format(split_name))[seq_id][frame_id]
        points_img_dict = dict()
        img_list, new_cam_intrinsic_dict = self.undistort_image_v2(seq_id, frame_id)
        for cam_no, cam_name in enumerate(self.__class__.camera_names):
            calib_info = frame_info['calib'][cam_name]
            cam_2_velo = calib_info['cam_to_velo']
            cam_intri = np.hstack([new_cam_intrinsic_dict[cam_name], np.zeros((3, 1), dtype=np.float32)])
            point_xyz = points[:, :3]
            points_homo = np.hstack(
                [point_xyz, np.ones(point_xyz.shape[0], dtype=np.float32).reshape((-1, 1))])
            points_lidar = np.dot(points_homo, np.linalg.inv(cam_2_velo).T)
            mask = points_lidar[:, 2] > 0
            points_lidar = points_lidar[mask]
            points_img = np.dot(points_lidar, cam_intri.T)
            points_img = points_img / points_img[:, [2]]
            img_buf = img_list[cam_no]
            for point in points_img:
                try:
                    cv2.circle(img_buf, (int(point[0]), int(point[1])), 2, color=(0, 0, 255), thickness=-1)
                except:
                    print(int(point[0]), int(point[1]))
            points_img_dict[cam_name] = img_buf
        return points_img_dict

    @staticmethod
    def rotate_z(theta):
        return np.array([[np.cos(theta), -np.sin(theta), 0],
                         [np.sin(theta), np.cos(theta), 0],
                         [0, 0, 1]])

    def project_boxes_to_image(self, seq_id, frame_id):
        split_name = self._find_split_name(seq_id)
        if split_name not in ['train', 'val']:
            print("seq id {} not in train/val, has no 2d annotations".format(seq_id))
            return
        frame_info = getattr(self, '{}_info'.format(split_name))[seq_id][frame_id]
        img_dict = dict()
        img_list, new_cam_intrinsic_dict = self.undistort_image_v2(seq_id, frame_id)
        for cam_no, cam_name in enumerate(self.__class__.camera_names):
            img_buf = img_list[cam_no]

            calib_info = frame_info['calib'][cam_name]
            cam_2_velo = calib_info['cam_to_velo']
            cam_intri = np.hstack([new_cam_intrinsic_dict[cam_name], np.zeros((3, 1), dtype=np.float32)])

            cam_annos_3d = np.array(frame_info['annos']['boxes_3d'])

            corners_norm = np.stack(np.unravel_index(np.arange(8), [2, 2, 2]), axis=1).astype(
                np.float32)[[0, 1, 3, 2, 0, 4, 5, 7, 6, 4, 5, 1, 3, 7, 6, 2], :] - 0.5
            corners = np.multiply(cam_annos_3d[:, 3: 6].reshape(-1, 1, 3), corners_norm)
            rot_matrix = np.stack(list([np.transpose(self.rotate_z(box[-1])) for box in cam_annos_3d]), axis=0)
            corners = np.einsum('nij,njk->nik', corners, rot_matrix) + cam_annos_3d[:, :3].reshape((-1, 1, 3))

            for i, corner in enumerate(corners):
                points_homo = np.hstack([corner, np.ones(corner.shape[0], dtype=np.float32).reshape((-1, 1))])
                points_lidar = np.dot(points_homo, np.linalg.inv(cam_2_velo).T)
                mask = points_lidar[:, 2] > 0
                points_lidar = points_lidar[mask]
                points_img = np.dot(points_lidar, cam_intri.T)
                points_img = points_img / points_img[:, [2]]
                if points_img.shape[0] != 16:
                    continue
                for j in range(15):
                    cv2.line(img_buf, (int(points_img[j][0]), int(points_img[j][1])), (int(points_img[j + 1][0]), int(points_img[j + 1][1])),
                             (0, 255, 0), 2, cv2.LINE_AA)

            cam_annos_2d = frame_info['annos']['boxes_2d'][cam_name]

            for box2d in cam_annos_2d:
                box2d = list(map(int, box2d))
                if box2d[0] < 0:
                    continue
                cv2.rectangle(img_buf, tuple(box2d[:2]), tuple(box2d[2:]), (255, 0, 0), 2)

            img_dict[cam_name] = img_buf
        return img_dict

    def frame_concat(self, seq_id, frame_id, concat_cnt=0):
        """
        return new points coordinates according to pose info
        :param seq_id:
        :param frame_id:
        :return:
        """
        split_name = self._find_split_name(seq_id)

        seq_info = getattr(self, '{}_info'.format(split_name))[seq_id]
        start_idx = seq_info['frame_list'].index(frame_id)
        points_list = []
        translation_r = None
        try:
            for i in range(start_idx, start_idx + concat_cnt + 1):
                current_frame_id = seq_info['frame_list'][i]
                frame_info = seq_info[current_frame_id]
                transform_data = frame_info['pose']

                points = self.load_point_cloud(seq_id, current_frame_id)
                points_xyz = points[:, :3]

                rotation = Rotation.from_quat(transform_data[:4]).as_matrix()
                translation = np.array(transform_data[4:]).transpose()
                points_xyz = np.dot(points_xyz, rotation.T)
                points_xyz = points_xyz + translation
                if i == start_idx:
                    translation_r = translation
                points_xyz = points_xyz - translation_r
                points_list.append(np.hstack([points_xyz, points[:, 3:]]))
        except ValueError:
            print('warning: part of the frames have no available pose information, return first frame point instead')
            points = self.load_point_cloud(seq_id, seq_info['frame_list'][start_idx])
            points_list.append(points)
            return points_list
        return points_list


if __name__ == '__main__':
    dataset = ONCE('/media/wangkai/ROG/Direction_code_once/data/once')
    for seq_id, frame_id in [('000092', '1616442892300')]:
        img_buf_dict = dataset.project_boxes_to_image(seq_id, frame_id)
        for cam_name, img_buf in img_buf_dict.items():
            cv2.imwrite('images/box_project_{}_{}.jpg'.format(cam_name, frame_id), cv2.cvtColor(img_buf, cv2.COLOR_BGR2RGB))
        img_buf_dict = dataset.project_lidar_to_image(seq_id, frame_id)
        for cam_name, img_buf in img_buf_dict.items():
            cv2.imwrite('images/lidar_project_{}_{}.jpg'.format(cam_name, frame_id), cv2.cvtColor(img_buf, cv2.COLOR_BGR2RGB))
```

### once_dataset.py

```c
import copy
import pickle
import numpy as np

from PIL import Image
import torch
import torch.nn.functional as F
from pathlib import Path

from ..dataset import DatasetTemplate
from ...ops.roiaware_pool3d import roiaware_pool3d_utils
from ...utils import box_utils
from .once_toolkits import Octopus


class ONCEDataset(DatasetTemplate):
    def __init__(self, dataset_cfg, class_names, training=True, root_path=None, logger=None):
        """
        Args:
            root_path:
            dataset_cfg:
            class_names:
            training:
            logger:
        """
        super().__init__(
            dataset_cfg=dataset_cfg, class_names=class_names, training=training, root_path=root_path, logger=logger
        )
        self.split = dataset_cfg.DATA_SPLIT['train'] if training else dataset_cfg.DATA_SPLIT['test']
        assert self.split in ['train', 'val', 'test', 'raw_small', 'raw_medium', 'raw_large']

        split_dir = self.root_path / 'data' / (self.split + '_set.txt')
        print("split_dir:", split_dir)
        self.sample_seq_list = [x.strip() for x in open(split_dir).readlines()] if split_dir.exists() else None
        self.cam_names = ['cam01', 'cam03', 'cam05', 'cam06', 'cam07', 'cam08', 'cam09']
        self.cam_tags = ['top', 'top2', 'left_back', 'left_front', 'right_front', 'right_back', 'back']
        self.toolkits = Octopus(self.root_path)

        self.once_infos = []
        self.include_once_data(self.split)

    def include_once_data(self, split):
        if self.logger is not None:
            self.logger.info('Loading ONCE dataset')
        once_infos = []

        for info_path in self.dataset_cfg.INFO_PATH[split]:
            info_path = self.root_path / info_path
            if not info_path.exists():
                continue
            with open(info_path, 'rb') as f:
                infos = pickle.load(f)
                once_infos.extend(infos)

        def check_annos(info):
            return 'annos' in info

        if self.split != 'raw':
            once_infos = list(filter(check_annos, once_infos))

        self.once_infos.extend(once_infos)

        if self.logger is not None:
            self.logger.info('Total samples for ONCE dataset: %d' % (len(once_infos)))

    def set_split(self, split):
        super().__init__(
            dataset_cfg=self.dataset_cfg, class_names=self.class_names, training=self.training, root_path=self.root_path, logger=self.logger
        )
        self.split = split

        split_dir = self.root_path / 'ImageSets' / (self.split + '.txt')
        print("split_dir:", split_dir)
        self.sample_seq_list = [x.strip() for x in open(split_dir).readlines()] if split_dir.exists() else None

    def get_lidar(self, sequence_id, frame_id):
        return self.toolkits.load_point_cloud(sequence_id, frame_id)

    def get_image(self, sequence_id, frame_id, cam_name):
        return self.toolkits.load_image(sequence_id, frame_id, cam_name)

    def project_lidar_to_image(self, sequence_id, frame_id):
        return self.toolkits.project_lidar_to_image(sequence_id, frame_id)

    def project_lidar_to_image_depth(self, sequence_id, frame_id):
        return self.toolkits.project_lidar_to_image_depth(sequence_id, frame_id)

    def image_to_lidar(self, sequence_id, frame_id,  vitual_close_points_lidar_dict, virtual_points_img_dict):
        return self.toolkits.image_to_lidar(sequence_id, frame_id,vitual_close_points_lidar_dict, virtual_points_img_dict)

    def point_painting(self, points, info):
        semseg_dir = './'  # add your own seg directory
        used_classes = [0, 1, 2, 3, 4, 5]
        num_classes = len(used_classes)
        frame_id = str(info['frame_id'])
        seq_id = str(info['sequence_id'])
        painted = np.zeros((points.shape[0], num_classes))  # classes + bg
        for cam_name in self.cam_names:
            img_path = Path(semseg_dir) / Path(seq_id) / Path(cam_name) / Path(frame_id + '_label.png')
            calib_info = info['calib'][cam_name]
            cam_2_velo = calib_info['cam_to_velo']
            cam_intri = np.hstack([calib_info['cam_intrinsic'], np.zeros((3, 1), dtype=np.float32)])
            point_xyz = points[:, :3]
            points_homo = np.hstack(
                [point_xyz, np.ones(point_xyz.shape[0], dtype=np.float32).reshape((-1, 1))])
            points_lidar = np.dot(points_homo, np.linalg.inv(cam_2_velo).T)
            mask = points_lidar[:, 2] > 0
            points_lidar = points_lidar[mask]
            points_img = np.dot(points_lidar, cam_intri.T)
            points_img = points_img / points_img[:, [2]]
            uv = points_img[:, [0, 1]]
            # depth = points_img[:, [2]]
            seg_map = np.array(Image.open(img_path))  # (H, W)
            H, W = seg_map.shape
            seg_feats = np.zeros((H * W, num_classes))
            seg_map = seg_map.reshape(-1)
            for cls_i in used_classes:
                seg_feats[seg_map == cls_i, cls_i] = 1
            seg_feats = seg_feats.reshape(H, W, num_classes).transpose(2, 0, 1)
            uv[:, 0] = (uv[:, 0] - W / 2) / (W / 2)
            uv[:, 1] = (uv[:, 1] - H / 2) / (H / 2)
            uv_tensor = torch.from_numpy(uv).unsqueeze(0).unsqueeze(0)  # [1,1,N,2]
            seg_feats = torch.from_numpy(seg_feats).unsqueeze(0)  # [1,C,H,W]
            proj_scores = F.grid_sample(seg_feats, uv_tensor, mode='bilinear', padding_mode='zeros')  # [1, C, 1, N]
            proj_scores = proj_scores.squeeze(0).squeeze(1).transpose(0, 1).contiguous()  # [N, C]
            painted[mask] = proj_scores.numpy()
        return np.concatenate([points, painted], axis=1)

    def __len__(self):
        if self._merge_all_iters_to_one_epoch:
            return len(self.once_infos) * self.total_epochs

        return len(self.once_infos)

    def __getitem__(self, index):
        if self._merge_all_iters_to_one_epoch:
            index = index % len(self.once_infos)

        info = copy.deepcopy(self.once_infos[index])
        frame_id = info['frame_id']
        seq_id = info['sequence_id']
        points = self.get_lidar(seq_id, frame_id)

        if self.dataset_cfg.get('POINT_PAINTING', False):
            points = self.point_painting(points, info)

        input_dict = {
            'points': points,
            'frame_id': frame_id,
            'seq_id': seq_id
        }

        if 'annos' in info:
            annos = info['annos']
            input_dict.update({
                'gt_names': annos['name'],
                'gt_boxes': annos['boxes_3d'],
                'num_points_in_gt': annos.get('num_points_in_gt', None)
            })

        data_dict = self.prepare_data(data_dict=input_dict)
        data_dict.pop('num_points_in_gt', None)
        return data_dict

    def get_infos(self, num_workers=4, sample_seq_list=None):
        import concurrent.futures as futures
        import json
        root_path = self.root_path
        cam_names = self.cam_names

        """
        # dataset json format
        {
            'meta_info': 
            'calib': {
                'cam01': {
                    'cam_to_velo': list
                    'cam_intrinsic': list
                    'distortion': list
                }
                ...
            }
            'frames': [
                {
                    'frame_id': timestamp,
                    'annos': {
                        'names': list
                        'boxes_3d': list of list
                        'boxes_2d': {
                            'cam01': list of list
                            ...
                        }
                    }
                    'pose': list
                },
                ...
            ]
        }
        # open pcdet format
        {
            'meta_info':
            'sequence_id': seq_idx
            'frame_id': timestamp
            'timestamp': timestamp
            'lidar': path
            'cam01': path
            ...
            'calib': {
                'cam01': {
                    'cam_to_velo': np.array
                    'cam_intrinsic': np.array
                    'distortion': np.array
                }
                ...
            }
            'pose': np.array
            'annos': {
                'name': np.array
                'boxes_3d': np.array
                'boxes_2d': {
                    'cam01': np.array
                    ....
                }
            }          
        }
        """

        def process_single_sequence(seq_idx):
            print('%s seq_idx: %s' % (self.split, seq_idx))
            seq_infos = []
            seq_path = Path(root_path) / 'data' / seq_idx
            json_path = seq_path / ('%s.json' % seq_idx)
            with open(json_path, 'r') as f:
                info_this_seq = json.load(f)
            meta_info = info_this_seq['meta_info']
            calib = info_this_seq['calib']
            for f_idx, frame in enumerate(info_this_seq['frames']):
                frame_id = frame['frame_id']
                if f_idx == 0:
                    prev_id = None
                else:
                    prev_id = info_this_seq['frames'][f_idx - 1]['frame_id']
                if f_idx == len(info_this_seq['frames']) - 1:
                    next_id = None
                else:
                    next_id = info_this_seq['frames'][f_idx + 1]['frame_id']
                pc_path = str(seq_path / 'lidar_roof' / ('%s.bin' % frame_id))
                pose = np.array(frame['pose'])
                frame_dict = {
                    'sequence_id': seq_idx,
                    'frame_id': frame_id,
                    'timestamp': int(frame_id),
                    'prev_id': prev_id,
                    'next_id': next_id,
                    'meta_info': meta_info,
                    'lidar': pc_path,
                    'pose': pose
                }
                calib_dict = {}
                for cam_name in cam_names:
                    cam_path = str(seq_path / cam_name / ('%s.jpg' % frame_id))
                    frame_dict.update({cam_name: cam_path})
                    calib_dict[cam_name] = {}
                    calib_dict[cam_name]['cam_to_velo'] = np.array(calib[cam_name]['cam_to_velo'])
                    calib_dict[cam_name]['cam_intrinsic'] = np.array(calib[cam_name]['cam_intrinsic'])
                    calib_dict[cam_name]['distortion'] = np.array(calib[cam_name]['distortion'])
                frame_dict.update({'calib': calib_dict})

                if 'annos' in frame:
                    annos = frame['annos']
                    boxes_3d = np.array(annos['boxes_3d'])
                    if boxes_3d.shape[0] == 0:
                        print(frame_id)
                        continue
                    boxes_2d_dict = {}
                    for cam_name in cam_names:
                        boxes_2d_dict[cam_name] = np.array(annos['boxes_2d'][cam_name])
                    annos_dict = {
                        'name': np.array(annos['names']),
                        'boxes_3d': boxes_3d,
                        'boxes_2d': boxes_2d_dict
                    }

                    points = self.get_lidar(seq_idx, frame_id)
                    corners_lidar = box_utils.boxes_to_corners_3d(np.array(annos['boxes_3d']))
                    num_gt = boxes_3d.shape[0]
                    num_points_in_gt = -np.ones(num_gt, dtype=np.int32)
                    for k in range(num_gt):
                        flag = box_utils.in_hull(points[:, 0:3], corners_lidar[k])
                        num_points_in_gt[k] = flag.sum()
                    annos_dict['num_points_in_gt'] = num_points_in_gt

                    frame_dict.update({'annos': annos_dict})
                seq_infos.append(frame_dict)
            return seq_infos

        sample_seq_list = sample_seq_list if sample_seq_list is not None else self.sample_seq_list
        with futures.ThreadPoolExecutor(num_workers) as executor:
            print("sample_seq_list:", sample_seq_list)
            infos = executor.map(process_single_sequence, sample_seq_list)
        all_infos = []
        for info in infos:
            all_infos.extend(info)
        return all_infos

    def create_groundtruth_database(self, info_path=None, used_classes=None, split='train'):
        import torch

        database_save_path = Path(self.root_path) / ('gt_database' if split == 'train' else ('gt_database_%s' % split))
        db_info_save_path = Path(self.root_path) / ('once_dbinfos_%s.pkl' % split)

        database_save_path.mkdir(parents=True, exist_ok=True)
        all_db_infos = {}

        with open(info_path, 'rb') as f:
            infos = pickle.load(f)

        for k in range(len(infos)):
            if 'annos' not in infos[k]:
                continue
            print('gt_database sample: %d' % (k + 1))
            info = infos[k]
            frame_id = info['frame_id']
            seq_id = info['sequence_id']
            points = self.get_lidar(seq_id, frame_id)
            annos = info['annos']
            names = annos['name']
            gt_boxes = annos['boxes_3d']

            num_obj = gt_boxes.shape[0]
            point_indices = roiaware_pool3d_utils.points_in_boxes_cpu(
                torch.from_numpy(points[:, 0:3]), torch.from_numpy(gt_boxes)
            ).numpy()  # (nboxes, npoints)

            for i in range(num_obj):
                filename = '%s_%s_%d.bin' % (frame_id, names[i], i)
                filepath = database_save_path / filename
                gt_points = points[point_indices[i] > 0]

                gt_points[:, :3] -= gt_boxes[i, :3]
                with open(filepath, 'w') as f:
                    gt_points.tofile(f)

                db_path = str(filepath.relative_to(self.root_path))  # gt_database/xxxxx.bin
                db_info = {'name': names[i], 'path': db_path, 'gt_idx': i,
                           'box3d_lidar': gt_boxes[i], 'num_points_in_gt': gt_points.shape[0]}
                if names[i] in all_db_infos:
                    all_db_infos[names[i]].append(db_info)
                else:
                    all_db_infos[names[i]] = [db_info]

        for k, v in all_db_infos.items():
            print('Database %s: %d' % (k, len(v)))

        with open(db_info_save_path, 'wb') as f:
            pickle.dump(all_db_infos, f)

    @staticmethod
    def generate_prediction_dicts(batch_dict, pred_dicts, class_names, output_path=None):
        def get_template_prediction(num_samples):
            ret_dict = {
                'name': np.zeros(num_samples), 'score': np.zeros(num_samples),
                'boxes_3d': np.zeros((num_samples, 7))
            }
            return ret_dict

        def generate_single_sample_dict(box_dict):
            pred_scores = box_dict['pred_scores'].cpu().numpy()
            pred_boxes = box_dict['pred_boxes'].cpu().numpy()
            pred_labels = box_dict['pred_labels'].cpu().numpy()
            pred_dict = get_template_prediction(pred_scores.shape[0])
            if pred_scores.shape[0] == 0:
                return pred_dict

            pred_dict['name'] = np.array(class_names)[pred_labels - 1]
            pred_dict['score'] = pred_scores
            pred_dict['boxes_3d'] = pred_boxes
            return pred_dict

        annos = []
        for index, box_dict in enumerate(pred_dicts):
            frame_id = batch_dict['frame_id'][index]
            single_pred_dict = generate_single_sample_dict(box_dict)
            single_pred_dict['frame_id'] = frame_id
            annos.append(single_pred_dict)

            if output_path is not None:
                raise NotImplementedError
        return annos

    def evaluation(self, det_annos, class_names, **kwargs):
        from .once_eval.evaluation import get_evaluation_results

        eval_det_annos = copy.deepcopy(det_annos)
        eval_gt_annos = [copy.deepcopy(info['annos']) for info in self.once_infos]
        ap_result_str, ap_dict = get_evaluation_results(eval_gt_annos, eval_det_annos, class_names)

        return ap_result_str, ap_dict


def create_once_infos(dataset_cfg, class_names, data_path, save_path, workers=4):
    dataset = ONCEDataset(dataset_cfg=dataset_cfg, class_names=class_names, root_path=data_path, training=False)

    splits = ['train', 'val', 'test', 'raw_small', 'raw_medium', 'raw_large']
    ignore = ['test', 'raw_small', 'raw_medium', 'raw_large']

    print('---------------Start to generate data infos---------------')
    for split in splits:
        if split in ignore:
            continue

        filename = 'once_infos_%s.pkl' % split
        filename = save_path / Path(filename)
        dataset.set_split(split)
        once_infos = dataset.get_infos(num_workers=workers)
        with open(filename, 'wb') as f:
            pickle.dump(once_infos, f)
        print('ONCE info %s file is saved to %s' % (split, filename))

    train_filename = save_path / 'once_infos_train.pkl'
    print('---------------Start create groundtruth database for data augmentation---------------')
    dataset.set_split('train')
    dataset.create_groundtruth_database(train_filename, split='train')
    print('---------------Data preparation Done---------------')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='arg parser')
    parser.add_argument('--cfg_file', type=str, default=None, help='specify the config of dataset')
    parser.add_argument('--func', type=str, default='create_waymo_infos', help='')
    parser.add_argument('--runs_on', type=str, default='server', help='')
    args = parser.parse_args()

    if args.func == 'create_once_infos':
        import yaml
        from pathlib import Path
        from easydict import EasyDict

        dataset_cfg = EasyDict(yaml.load(open(args.cfg_file), Loader=yaml.FullLoader))

        ROOT_DIR = (Path(__file__).resolve().parent / '../../../').resolve()
        once_data_path = ROOT_DIR / 'data' / 'once'
        once_save_path = ROOT_DIR / 'data' / 'once'

        if args.runs_on == 'cloud':
            once_data_path = Path('/cache/once/')
            once_save_path = Path('/cache/once/')
            dataset_cfg.DATA_PATH = dataset_cfg.CLOUD_DATA_PATH

        create_once_infos(
            dataset_cfg=dataset_cfg,
            class_names=['Car', 'Bus', 'Truck', 'Pedestrian', 'Bicycle'],
            data_path=once_data_path,
            save_path=once_save_path
        )

```

### once_toolkits.py

```c
import json
import os.path as osp
from collections import defaultdict
import cv2
import numpy as np


class Octopus(object):
    """
    dataset structure:
    - data_root
        - train_split.txt
        - val_split.txt
        - test_split.txt
        -
    """
    camera_names = ['cam01', 'cam03', 'cam05', 'cam06', 'cam07', 'cam08', 'cam09']
    camera_tags = ['top', 'top2', 'left_back', 'left_front', 'right_front', 'right_back', 'back']

    def __init__(self, dataset_root):
        self.dataset_root = dataset_root
        self.data_root = osp.join(self.dataset_root, 'data')
        self._collect_basic_infos()

    @property
    def train_split_list(self):
        if not osp.isfile(osp.join(self.dataset_root, 'ImageSets', 'train.txt')):
            train_split_list = None
        else:
            train_split_list = set(map(lambda x: x.strip(),
                                       open(osp.join(self.data_root, 'train.txt')).readlines()))
        return train_split_list

    @property
    def val_split_list(self):
        if not osp.isfile(osp.join(self.dataset_root, 'ImageSets', 'val.txt')):
            val_split_list = None
        else:
            val_split_list = set(map(lambda x: x.strip(),
                                     open(osp.join(self.data_root, 'val.txt')).readlines()))
        return val_split_list

    @property
    def test_split_list(self):
        if not osp.isfile(osp.join(self.dataset_root, 'ImageSets', 'test.txt')):
            test_split_list = None
        else:
            test_split_list = set(map(lambda x: x.strip(),
                                      open(osp.join(self.data_root, 'test.txt')).readlines()))
        return test_split_list

    @property
    def raw_split_list(self):
        if not osp.isfile(osp.join(self.dataset_root, 'ImageSets', 'raw_set.txt')):
            raw_split_list = None
        else:
            raw_split_list = set(map(lambda x: x.strip(),
                                     open(osp.join(self.data_root, 'raw_set.txt')).readlines()))
        return raw_split_list

    def _find_split_name(self, seq_id):
        # if seq_id in self.raw_split_list:
        #     return 'raw'
        if seq_id in self.train_split_list:
            return 'train'
        if seq_id in self.test_split_list:
            return 'test'
        if seq_id in self.val_split_list:
            return 'val'
        print("sequence id {} corresponding to no split".format(seq_id))
        raise NotImplementedError

    def _collect_basic_infos(self):
        self.train_info = defaultdict(dict)
        if self.train_split_list is not None:
            for train_seq in self.train_split_list:
                anno_file_path = osp.join(self.data_root, train_seq, '{}.json'.format(train_seq))
                if not osp.isfile(anno_file_path):
                    print("no annotation file for sequence {}".format(train_seq))
                    raise FileNotFoundError
                anno_file = json.load(open(anno_file_path, 'r'))
                for frame_anno in anno_file['frames']:
                    self.train_info[train_seq][frame_anno['frame_id']] = {
                        'pose': frame_anno['pose'],
                        'calib': anno_file['calib'],
                    }

        self.val_info = defaultdict(dict)
        if self.val_split_list is not None:
            for val_seq in self.val_split_list:
                anno_file_path = osp.join(self.data_root, val_seq, '{}.json'.format(val_seq))
                if not osp.isfile(anno_file_path):
                    print("no annotation file for sequence {}".format(val_seq))
                    raise FileNotFoundError
                anno_file = json.load(open(anno_file_path, 'r'))
                for frame_anno in anno_file['frames']:
                    self.val_info[val_seq][frame_anno['frame_id']] = {
                        'pose': frame_anno['pose'],
                        'calib': anno_file['calib'],
                    }

    def get_frame_anno(self, seq_id, frame_id):
        split_name = self._find_split_name(seq_id)
        frame_info = getattr(self, '{}_info'.format(split_name))[seq_id][frame_id]
        if 'anno' in frame_info:
            return frame_info['anno']
        return None

    def load_point_cloud(self, seq_id, frame_id):
        bin_path = osp.join(self.data_root, seq_id, 'lidar_roof', '{}.bin'.format(frame_id))
        points = np.fromfile(bin_path, dtype=np.float32).reshape(-1, 4)
        return points

    def load_image(self, seq_id, frame_id, cam_name):
        cam_path = osp.join(self.data_root, seq_id, cam_name, '{}.jpg'.format(frame_id))
        img_buf = cv2.cvtColor(cv2.imread(cam_path), cv2.COLOR_BGR2RGB)
        return img_buf

    def project_lidar_to_image(self, seq_id, frame_id):
        points = self.load_point_cloud(seq_id, frame_id)

        split_name = self._find_split_name(seq_id)
        frame_info = getattr(self, '{}_info'.format(split_name))[seq_id][frame_id]
        points_img_dict = dict()
        for cam_name in self.__class__.camera_names:
            calib_info = frame_info['calib'][cam_name]
            cam_2_velo = calib_info['cam_to_velo']
            cam_intri = cam_intri = np.hstack([calib_info['cam_intrinsic'], np.zeros((3, 1), dtype=np.float32)])
            point_xyz = points[:, :3]
            points_homo = np.hstack(
                [point_xyz, np.ones(point_xyz.shape[0], dtype=np.float32).reshape((-1, 1))])
            points_lidar = np.dot(points_homo, np.linalg.inv(cam_2_velo).T)
            mask = points_lidar[:, 2] > 0
            points_lidar = points_lidar[mask]
            points_img = np.dot(points_lidar, np.array(cam_intri).T)
            points_img = points_img / points_img[:, [2]]
            uv = points_img[:, [0, 1]]
            points_img_dict[cam_name] = uv
        return points_img_dict

    def project_lidar_to_image_depth(self, seq_id, frame_id):
        points = self.load_point_cloud(seq_id, frame_id)

        split_name = self._find_split_name(seq_id)
        frame_info = getattr(self, '{}_info'.format(split_name))[seq_id][frame_id]
        points_lidar_dict = dict()
        point_xyz_dict = dict()
        for cam_name in self.__class__.camera_names:
            calib_info = frame_info['calib'][cam_name]
            cam_2_velo = calib_info['cam_to_velo']
            cam_intri = cam_intri = np.hstack([calib_info['cam_intrinsic'], np.zeros((3, 1), dtype=np.float32)])
            point_xyz = points[:, :3]
            points_homo = np.hstack(
                [point_xyz, np.ones(point_xyz.shape[0], dtype=np.float32).reshape((-1, 1))])
            points_lidar = np.dot(points_homo, np.linalg.inv(cam_2_velo).T)
            mask = points_lidar[:, 2] > 0
            points_lidar = points_lidar[mask]
            points_img = np.dot(points_lidar, np.array(cam_intri).T)
            depth = points_lidar[:, 2]
            points_lidar_dict[cam_name] = points_lidar

            point_xyz = point_xyz[mask]
            point_xyz_dict[cam_name] = point_xyz
        return points_lidar_dict,point_xyz_dict

    def image_to_lidar(self, seq_id, frame_id, vitual_close_points_lidar_dict, virtual_points_img_dict):
        split_name = self._find_split_name(seq_id)
        frame_info = getattr(self, '{}_info'.format(split_name))[seq_id][frame_id]

        # 初始化一个空列表来存储所有的 point_xyz
        all_point_xyz = dict()

        for cam_name in vitual_close_points_lidar_dict.keys():
            calib_info = frame_info['calib'][cam_name]
            cam_2_velo = calib_info['cam_to_velo']
            cam_intri = cam_intri = np.hstack([calib_info['cam_intrinsic'], np.zeros((3, 1), dtype=np.float32)])

            close_points_lidar = vitual_close_points_lidar_dict[cam_name]
            points_img = np.dot(close_points_lidar, np.array(cam_intri).T)
            uv = virtual_points_img_dict[cam_name]
            # points_img[:, [0, 1]] = uv * points_img[:, [2]]

            cam_intri_inv = np.linalg.pinv(cam_intri)
            points_lidar = np.dot(points_img, np.array(cam_intri_inv).T)

            # np.dot(np.dot(close_points_lidar, np.array(cam_2_velo).T), np.linalg.pinv(cam_2_velo).T)
            points_homo = np.dot(close_points_lidar, np.array(cam_2_velo).T)
            point_xyz = points_homo[:, :3]
            all_point_xyz[cam_name] = point_xyz

        return all_point_xyz

    def undistort_image(self, seq_id, frame_id):
        pass

```

## virNe vir_utils



## Openpcd 多进程显示比较