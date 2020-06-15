import cv2
import numpy as np

img = cv2.imread('8.jpg')
(h,w) = img.shape[:2]
center = (w/2, h/2)
angle45 = 45
angle90 = 90
scale = 1.0

M = cv2.getRotationMatrix2D(center, angle45, scale)
M2 = cv2.getRotationMatrix2D(center, angle90, scale)

abs_cos = abs(M[0,0]) 
abs_sin = abs(M[0,1])

abs_cos = abs(M2[0,0]) 
abs_sin = abs(M2[0,1])

bound_w = int(h * abs_sin + w * abs_cos)
bound_h = int(h * abs_cos + w * abs_sin)

M[0, 2] += bound_w/2 - center[0]
M[1, 2] += bound_h/2 - center[1]

M2[0, 2] += bound_w/2 - center[0]
M2[1, 2] += bound_h/2 - center[1]

rotated45 = cv2.warpAffine(img, M, (bound_w,bound_h))

for i in range(7):
	rotated45 = cv2.warpAffine(rotated45, M, (bound_w,bound_h))

rotated90 = cv2.warpAffine(img, M2, (bound_w,bound_h))

for i in range(3):
	rotated90 = cv2.warpAffine(rotated90, M2, (bound_w,bound_h))

cv2.imshow('Rotated by 45 8 times', rotated45)
cv2.imshow('Rotated by 90 4 times', rotated90)
cv2.imwrite('rotated45.jpg',rotated45)
cv2.imwrite('rotated90.jpg',rotated90)
cv2.waitKey(0)
cv2.destroyAllWindows()