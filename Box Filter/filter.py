# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('panda1.jpg',0)
# x = int(input())

# kernel = np.ones((x,x),np.float32)/pow(x,2)
# dst = cv2.blur(img,0,kernel,img,(-1,-1),False,cv2.BORDER_DEFAULT)
# #cv2.imwrite('dts.png', dst)
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('panda1.jpg')

blur = cv2.blur(img,(5,5))

plt.imshow(img),plt.title('Original')
plt.show()
cv2.imwrite('orig.png', img)
plt.xticks([]), plt.yticks([])
plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
cv2.imwrite('boxfil.png', blur)