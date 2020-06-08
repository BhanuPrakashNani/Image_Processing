import cv2
import numpy as np

img = cv2.imread('block.png')
(h,w) = img.shape[:2]
center = (w/2, h/2)
angle45 = 45
scale = 1.0

M = cv2.getRotationMatrix2D(center, angle45, scale)


abs_cos = abs(M[0,0]) 
abs_sin = abs(M[0,1])


bound_w = int(h * abs_sin + w * abs_cos)
bound_h = int(h * abs_cos + w * abs_sin)

M[0, 2] += bound_w/2 - center[0]
M[1, 2] += bound_h/2 - center[1]

rotated30 = cv2.warpAffine(img, M, (bound_w,bound_h))

# cv2.imshow('Original Image', img)
# cv2.imshow('Rotated by 30', rotated30)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


scale_percent = 110
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

scaled = cv2.resize(img, dim, interpolation=cv2.INTER_NEAREST)
scaled1 = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)
scaled2 = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Nearest Neighbour", scaled)
cv2.imshow("Bilinear", scaled)
cv2.imshow("Bicubic", scaled)
cv2.waitKey(0)
cv2.destroyAllWindows() 