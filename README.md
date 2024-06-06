可能遇到的问题如下：
1.anaconda的安装
  教程：https://www.bilibili.com/video/BV1Fy4y1878z/
  
2.cuda、cudnn的安装
  教程：https://www.bilibili.com/video/BV1fY411y7Xq/
  
  首先查看pytorch支持的最高版本
  
  PyTorch网址:https://pytorch.org/

  然后查看N卡系统支持最高的版本
  
  然后权衡下载支持最高版本的CUDA和cuDNN

  CUDA工具包： https://developer.nvidia.cn/zh-cn/cuda-toolkit

  cuDNN：https://developer.nvidia.com/rdp/cudnn-download

  配置对应的环境变量

  nvcc -V：查看版本CUDA

  安装项目依赖

  pip install -e ultralytics

  pip install ultralytics

  pip install yolo

3.安装CPU版本pytorch和torchvision
  打开pytorch官网
  找到对应CUDA版本的下载链接





卸载项目依赖为你，，使用对应命令下载GPU版本
