#最近邻插值

# import cv2
# import numpy as np
# def function(img,w,h):  #w*h是目标图大小
#     height,width,channels =img.shape
#     emptyImage=np.zeros((h,w,channels),dtype=np.uint8)
#     sh=h/height
#     sw=w/width
#     for i in range(h):
#         for j in range(w):
#             x=int(i/sh)
#             y=int(j/sw)
#             emptyImage[i,j]=img[x,y]
#     return emptyImage
#
# img=cv2.imread("lenna.png")
# h = 800;
# w = 800;
# zoom=function(img,w,h)
# print(zoom)# 输出矩阵
# print(zoom.shape)# (800,800,3)  高，宽，通道数
# cv2.imshow("nearest interp",zoom)
# cv2.imshow("image",img)
# cv2.waitKey(0)

import numpy as np
import cv2

def NERTFunction(img,img_shape,tar_shape):
    ratioH=tar_shape[0]/img_shape[0]
    ratioW=tar_shape[1]/img_shape[1]
    tarimg=np.zeros((int(tar_shape[0]),int(tar_shape[1]),3))
    for h in range(int(tar_shape[0])):
        for w in range(int(tar_shape[1])):
            srch = int(h/ratioH)
            srcw = int(w/ratioW)
            tarimg[h][w] = img[srch][srcw]
        return tarimg

img=cv2.imread("lenna.png")
img_shape=(img.shape[0],img.shape[1])
tar_shape=(img.shape[0]*2,img.shape[1]*2)
tarimg=NERTFunction(img,img_shape,tar_shape)
cv2.imshow("nearest interp",tarimg)

