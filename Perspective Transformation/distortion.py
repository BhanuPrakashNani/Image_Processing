import cv2
import numpy

imgtrn = cv2.imread("chDistorted.jpeg")
dimtrn = imgtrn.shape

imgray = cv2.cvtColor(imgtrn, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(imgray, 60, 255, 0)
cv2.imshow("binary",binary)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours.remove(contours[0])

contours = max(contours, key=cv2.contourArea)

br=[0,0]
tl=[dimtrn[0],dimtrn[1]]
tr=[0,dimtrn[1]]
bl=[dimtrn[0],0]
for i in contours:
	for j in i:
		if br[0]+br[1]<j[0]+j[1]:
			br=j
		if tl[0]+tl[1]>j[0]+j[1]:
			tl=j
		if tr[0]-tr[1]<j[0]-j[1]:
			tr=j
		if -bl[0]+bl[1]<-j[0]+j[1]:
			bl=j

x=numpy.float32(tr)
y=numpy.float32(bl)

pts1=numpy.float32([[0,0],[0,dimtrn[1]],[dimtrn[0],0],[dimtrn[0],dimtrn[1]]])
pts2=numpy.float32([tl,y,x,br])

m = cv2.getPerspectiveTransform(pts2,pts1)
img = cv2.warpPerspective(imgtrn,m,(dimtrn[0],dimtrn[1]))

cv2.imshow("transformed",img)
cv2.drawContours(imgtrn, contours, -1, (0,255,0), 1)
cv2.imshow("turned",imgtrn)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("ch.jpg",img)