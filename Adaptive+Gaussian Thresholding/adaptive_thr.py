import cv2
import numpy as np

img = cv2.imread('page.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray', img)

blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('blur', blur)

ret,th1 = cv2.threshold(blur,150,255,cv2.THRESH_BINARY)
cv2.imshow('Global', th1)
cv2.imwrite('Global.jpg',th1)


th2 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('Adaptive Mean', th2)
cv2.imwrite('AM.jpg',th2)


th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('Adaptive Gaussian', th3)
cv2.imwrite('AG.jpg',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
