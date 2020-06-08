import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi.jpg')
cv2.imshow('img', img)

mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (70,65,400,290)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img_cut = img*mask2[:,:,np.newaxis]

cv2.imshow('img_cut', img_cut)
cv2.imwrite('cut_messi.jpg', img_cut)
cv2.waitKey(0)