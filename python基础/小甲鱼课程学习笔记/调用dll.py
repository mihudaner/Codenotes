from ctypes import *
import time
#MvCamCtrldll = WinDLL("C:\\Program Files (x86)\\Common Files\\MVS\\Runtime\\Win32_i86\\MvCameraControl.dll")
#MvCamCtrldll = WinDLL("C:\\Program Files (x86)\\Common Files\\MVS\\Runtime\\Win64_x64\\MvCameraControl.dll")
VecterCtrldll = WinDLL("C:\\Users\\wangkai\\Desktop\\pythonwork\\移动转台\\三维重建\\三维重建\\移动平台控制器P027\\DLL\\vector_generator.dll")#调用了这个dll
VecterCtrldll.SetComPortn(c_uint(3))
VecterCtrldll.SetSpeed(c_uint(0),c_uint(1000))
time.sleep(2)
#VecterCtrldll.CloseCommPort(c_uint(3))
print("over")