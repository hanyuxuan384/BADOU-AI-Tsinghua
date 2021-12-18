import cv2 #利用opencv读取图像
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from PIL import Image

img=cv2.imread("lenna.png")  #读取图像
#显示cv读取的图像
plt.subplot(221)
plt.imshow(img)

#显示GBR改为RGB后的三通道灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.subplot(222)
plt.imshow(img_gray)  #plt显示图像默认三通道，不是单灰
#plt.axis('off')

#显示灰度图
plt.subplot(223)
plt.imshow(img_gray, cmap='gray')

'''二值化'''
img_binary = np.where(img_gray >= 127, 255, 0)
plt.subplot(224)
plt.imshow(img_binary, cmap='gray')
plt.show()
