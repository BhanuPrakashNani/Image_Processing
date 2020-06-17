import cv2 
import numpy as np 

img = cv2.imread('log.jpg')  
c = 255/(np.log(1 + np.max(img))) 
log_transformed = c * np.log(1 + img) 
  
# Specify the data type. 
log_transformed = np.array(log_transformed, dtype = np.uint8) 
  
cv2.imwrite('log_transformed.jpg', log_transformed)

cv2.imshow('log_transformed',log_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
