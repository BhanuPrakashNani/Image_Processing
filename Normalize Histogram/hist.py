import cv2 as cv
path = 'hist.png'
img = cv.imread(path)
img = cv.resize(img, (800, 800))
cv.normalize(img, None, 0, 255, cv.NORM_L1)
cv.imshow('dst_rt', img)
cv.imwrite('norm.png', img)
cv.waitKey(0)
cv.destroyAllWindows()