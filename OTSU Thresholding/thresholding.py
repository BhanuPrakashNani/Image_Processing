import cv2 
import numpy as np

img = cv2.imread('noisy_leaf.jpg', cv2.IMREAD_GRAYSCALE)  
cv2.imshow('gray', img)
cv2.imwrite('gray1.jpg',img)

blur = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('blur', img)
cv2.imwrite('blur1.jpg',img)

x,threshold = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY) 
cv2.imshow('Binary threshold', threshold)
cv2.imwrite('binarythresh1.jpg',img)

ret2,th2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsus Thresholding', th2)
cv2.imwrite('Otsus.jpg',img)

cv2.waitKey(0)
