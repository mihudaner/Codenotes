# 研究方向讨论 2023.1.9
### Q: 1.点云超分辨效果目前看来不如伪点云，点云超分辨还有没利用价值？  
 RE:原论文的超分辨结构简单，模型有可以改进的地方，比如原本超64线，先超到32线。  
原本的残差结构简单，后面可以尝试用gan，diffusion model进行超分辨以及超分辨策略的改进。  

### Q: 2.深度补全方向的论文和MVP的代码有没有必要了解？  
 RE:深度补全和MVP与伪雷达不冲突，深度补全也是用到点云+图像通过稀疏深度生成逐像素的深度信息，具体效果和pseudo lidar相比有没有优势，需要比较检测性能。  
### Q: 3.伪雷达和超分辨点云两套点云怎么结合？  
 RE: 而且超分辨虽然效果不如伪雷达，但是优势在于拥有360°，而伪雷达只有前视。  
此外原本的pseudo lidar++用的4线激光雷达进行伪雷达点云的矫正，需要做实验去尝试，16线，超分辨32线相比于4线到底能不能获得更好的效果和性能。  

### Q: 4.目前眼下工作不知道从哪里开始了
 RE:先得验证64线，16线，超分辨点云的检测性能，验证超分辨点云相对于16线点云确实有提升，然后去尝试pseudo lidar++融合伪雷达点云，之后再去考虑超分辨模型的改进等。  

补充：  
验证超分辨的可行性后，先搭建点云超分辨+前向点云融合+目标检测模块的全通路，然后调优  

深度估计500ms  深度估计转点云100ms  伪点云稀疏到64 50ms   
生成4Line点云50-100ms  矫正后的估计转点云2-3s  

# 动机
别人只用在虚拟场景，角度投影存在困难，稀疏，列补全，行补全暂时不能用，但后面实验只需要1线deepmap，训练用的虚拟的数据集
修改了图像超分辨的模型，不再是unet不再fpn，mit只是一个思路，gt16和输出在一起用反射率区分


# 研一下开学讨论
1. 师兄论文的了解翻译和完善，smartiot（2023.5）
2. 项目软件的基本框架的完成（2023.10.1） 
3. 研究方向思路还是不变，突破第一个点 
4. 下周去清华弄好结构光相机

# 总结
+ 心态上的改变，完成任务的心态变成找到最好的方法解决一个技术困难的问题    
+ 时间分配更加合理，能更加合理的安排每一天的时间，不会拖到很晚，在焦急的情况下是没有办法完成好任务的  
+ 对知识的系统性补充，比如操作系统，高并发处理，数据传输，数据结构等等支持的完善和补充  
+ 看论文更加有目的性  
+ 灵活变通的解决问题，一个方法解决不了问题不能死磕，多尝试其他方法  
+ 更高效的看论文和代码，知道哪些是值得细究的  
+ 方向思路清晰了
+ 框架的学习和模型的理解openpcd paddle cmake
+ 陌生词汇越来越少，经常在摘要看到看过的论文
+ 一段工作后的代码整理

# 工具
+ Cloudcompare  
+ 小绿鲸  
+ Deeplearning翻译  
+ 翻译deepl美式好一点
+ newbeing

# 提高性能，创新和改进，
## point2deepmap的问题
用周期计算行 
列漏掉的点暂时用周围的点补充

## Unet的超分辨 
超分辨网络有个缺点就是不管近远都是1024个点，所以远处就会稀疏  
水平分辨率比实际低了，去噪也使得水平分辨率变低 

点云去噪去离散的算法

训练参数在cuda:1,迁移时候在加载模型的时候加上map_location=‘cuda:0’  

## 别的超分辨网络
1. unet-pytorch  unet改的失败了
[unet](https://blog.csdn.net/qq_32545287/article/details/117228826?app_version=5.14.3&csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22117228826%22%2C%22source%22%3A%22weixin_52613221%22%7D&utm_source=app)
2. [超分辨综述](https://zhuanlan.zhihu.com/p/558561628) 
3. Fast, accurate, and lightweight super-resolution with cascading residual network（CARN）
4. ***CARN很成功***


## 3D目标检测中点云的稀疏性问题及解决方案
[3D目标检测中点云的稀疏性问题及解决方案](https://mp.weixin.qq.com/s?__biz=MzU2NjU3OTc5NA==&mid=2247562187&idx=2&sn=0e0d137b5fbf4b0808d8d459b1c22b17&chksm=fca9f4f6cbde7de097e1ad435fefec0ac00d45fe5f4befed2c3d4390fd8363e61704f5780312&scene=27)


# pytorch部分
## 训练策略 OneCycleLR
[训练策略pytorch函数](https://blog.csdn.net/weiman1/article/details/125647517)
```python
scheduler = torch.optim.lr_scheduler.OneCycleLR(optimizer_nn, max_lr=0.1, pct_start=0.3, total_steps=121 * len(train_loader), div_factor=10, final_div_factor=1000)
```


## 模型的学习
### unet
![img_1.png](img_1.png)
```python
class UNet(nn.Module):
    def __init__(self, n_channels, n_classes, bilinear=False):
        super(UNet, self).__init__()
        self.n_channels = n_channels
        self.n_classes = n_classes
        self.bilinear = bilinear

        self.inc = DoubleConv(64, 64)

        self.up_1 = UP_h(n_channels, 64)
        self.up_2 = UP_h(64, 64)

        self.dbconv = DoubleConv(64, 64)

        self.down1 = Down(64, 128)
        self.down2 = Down(128, 256)
        self.down3 = Down(256, 512)
        factor = 2 if bilinear else 1
        self.down4 = Down(512, 1024 // factor)

        self.up1 = Up(1024, 512 // factor, bilinear)
        self.drop1 = nn.Dropout(dropout_rate)
        self.up2 = Up(512, 256 // factor, bilinear)
        self.drop2 = nn.Dropout(dropout_rate)
        self.up3 = Up(256, 128 // factor, bilinear)
        self.drop3 = nn.Dropout(dropout_rate)
        self.up4 = Up(128, 64, bilinear)
        self.outc = OutConv(64, n_classes)

    def forward(self, x):
        # 两次卷积,第一次卷积,第一次3维到64维,第二次64到64
        # x1 = self.inc(x)
        x = self.up_1(x) # 高度*2
        x1 = self.up_2(x) # 高度*2

        x1 = self.dbconv(x1) #  DoubleConv(64, 64)

        # 连续三次下采样 ，每次下采样都采取了maxpool和两次卷积，缩小了特征图宽高为1/2
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        # 先把传入的特征图x上采样
        # 上采样使用blinear或者转置卷积扩大特征图宽高为两倍。
        # 然后把x和之前的图concat，最后再进行两次卷积。
        # 这样即可在逐步把特征图大小变回原图的同时，逐步缩小通道数为64。
        x = self.up1(x5, x4)
        self.drop1(x)
        x = self.up2(x, x3)
        self.drop2(x)
        x = self.up3(x, x2)
        self.drop3(x)
        x = self.up4(x, x1)
        # 1*1卷积，通道由64转为类别数，即每一个类别对应一个mask
        logits = self.outc(x)
        return logits
```
### MIT
```python

class UNet(nn.Module):
    # input的维度b*1*16*1024
    def __init__(self):
        super(UNet, self).__init__()

        self.upscaling = nn.Sequential(
            Up_Block(1, 64, strides=(2, 1)),
            Up_Block(64, 64, strides=(2, 1)),
        )
        # b*64_best*64_best*1024
        self.conv1 = Conv_Block(filters, filters)
        # b*64_best*64_best*1024
        self.conv2 = nn.Sequential(
            nn.AvgPool2d(2, 2),
            Conv_Block(filters, filters * 2)
        )
        self.conv3 = nn.Sequential(
            nn.AvgPool2d(2, 2),
            nn.Dropout(dropout_rate),
            Conv_Block(filters * 2, filters * 4)
        )
        self.conv4 = nn.Sequential(
            nn.AvgPool2d(2, 2),
            nn.Dropout(dropout_rate),
            Conv_Block(filters * 4, filters * 8)
        )
        self.center = nn.Sequential(
            nn.AvgPool2d(2, 2),
            nn.Dropout(dropout_rate),
            Conv_Block(filters * 8, filters * 16),
            nn.Dropout(dropout_rate),
            Up_Block(filters * 16, filters * 8, strides=(2, 2)),
        )
        # b* 64_best/8 * 1024/8 * 64_best * 8 concatenate  b* 64_best/8 * 1024/8 * 64_best * 8 = b* 64_best/8 * 1024/8 * 64_best * 16
        self.upblk3 = nn.Sequential(
            Conv_Block(filters * 16, filters * 8),
            nn.Dropout(dropout_rate),
            Up_Block(filters * 8, filters * 4, strides=(2, 2)),
        )

        self.upblk2 = nn.Sequential(
            Conv_Block(filters * 8, filters * 4),
            nn.Dropout(dropout_rate),
            Up_Block(filters * 4, filters * 2, strides=(2, 2)),
        )

        self.upblk1 = nn.Sequential(
            Conv_Block(filters * 4, filters * 2),
            Up_Block(filters * 2, filters, strides=(2, 2)),
        )

        self.end = nn.Sequential(
            Conv_Block(filters, filters),
            nn.Conv2d(filters, 1, (1, 1)),
        )

    def forward(self, x):
        x0 = self.upscaling(x)
        x1 = self.conv1(x0)
        x2 = self.conv2(x1)
        x3 = self.conv3(x2)
        x4 = self.conv4(x3)
        y4 = self.center(x4)

        y4 = torch.cat((x4, y4), dim=1)
        y3 = self.upblk3(y4)

        y3 = torch.cat((x3, y3), dim=1)
        y2 = self.upblk2(y3)

        y2 = torch.cat((x2, y2), dim=1)
        y1 = self.upblk1(y2)

        out = F.leaky_relu(self.end(y1))

        return out
```
### CARN图像超分辨
[上采样用的诸多方法的介绍](https://blog.csdn.net/djfjkj52/article/details/123829282)

### FasterRcnn


### Pointpiller
mmdet.ppt

### PVRCNN
[PVRCNN详解(个人阅读心得并总结其他人的结论得出的文章)](https://blog.csdn.net/qq_36380978/article/details/119940262)

### YOLOV7

### VirConv
https://github.com/hailanyi/VirConv

### persuade lidar

### MVP

### 稀疏卷积
![img_17.png](img_17.png)

# CARN2000+piller实验

### CARN2000最好一次62,行周期计算
![img_3.png](img_3.png)
```
predImagesNoiseReduced[noiseLabels > predImagesNoiseReduced * 0.005] = 0  # after noise removal
```
### 直接转换不超分辨也会降
用到了反射率和体素化，反射率都是0可能有影响，地面不一样高可能影响收敛，体素化可能使得超分辨只在视觉上得到提升，检测上提升一般

### 反射率影响
![img_2.png](img_2.png) 
![img_14.png](img_14.png)
反射率影响好像并不大，16线把反射率去掉了都没再训也有75,再训79.63
![img_4.png](img_4.png)
![img_5.png](img_5.png)
![img_6.png](img_6.png)
![img_7.png](img_7.png)

### 周期计算行影响

![img_9.png](img_9.png)  
周期计算行转换回来的点云2000直接送到gt16line训练的模型，只有24.4
![img_8.png](img_8.png)  
高度差


![img_10.png](img_10.png)  
角度计算行转换回来的点云1024直接送到gt16line训练的模型，有57.7  
原gt16line训练是行2000，按理周期计算应该高，结果低很多，说明角度计算比周期好很多

![img_13.png](img_13.png)  
原16line  
![img_12.png](img_12.png)  
ang-2000-16line

###  原16线加入
![img_15.png](img_15.png)

### 统计垂直角分辨率信息
无法统计，每一线的垂直角度波动很大，不是准确的0.41


### 16线和深度图对齐
16线点云从最低的一线开始每隔4线取一线
深度图
ang_res_y = 0.41 * (64 / image_rows_high)  # vertical resolution
ang_start_y = -23.8  # bottom beam angle
也比较准所以能对上
！！！！如果不是按照这样取，转换的深度图的ang_start_y = -23.8和16线的第一线就对不上，
因为16线的最低的一线必须要是64线的最低的一线，这样才能对的上


### 去除地面点云超分的点云-置信度跳到0.005，限制距离
![img_16.png](img_16.png)

### 半径滤波

### 像MVP一样用分割滤波


