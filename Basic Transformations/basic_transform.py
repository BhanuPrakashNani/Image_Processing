import cv2 
import numpy as np 

image = cv2.imread('calvinHobbes.jpeg') 


height, width = image.shape[:2] 
quarter_height, quarter_width = height/4, width/4

T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]]) 
img_translation = cv2.warpAffine(image, T, (width, height)) 

cv2.imshow("Originalimage", image) 
cv2.imshow('Translation', img_translation)
cv2.imwrite('Translation.jpg', img_translation) 
cv2.waitKey() 

cv2.destroyAllWindows() 


# cv2.imshow("Nearest Neighbour", scaled)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow("Bilinear", scaled)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow("Bicubic", scaled)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
