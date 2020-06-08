import matplotlib.pyplot as plt
import cv2
import numpy as np
import collections
# img = plt.read('hist.png')
# plt.hist(n_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

img = cv2.imread('hist.png',0) 
arr = np.array(img).flatten()
# cnt = []
# cnt = collections.Counter(arr)
x = []
for i in range(0,256):
	x.append(i)
# print(y)

plt.hist(arr, bins=50, orientation = 'vertical',normed=1)
#plt.swap_axes()
plt.show()