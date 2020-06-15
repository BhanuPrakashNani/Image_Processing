import cv2
import numpy
import math 

a=math.pi/4

img = cv2.imread("pexels.jpeg")
dim = img.shape

imgt = numpy.zeros((int(abs(dim[0]*math.cos(a))+abs(dim[1]*math.sin(a))),int(abs(dim[0]*math.sin(a))+abs(dim[1]*math.cos(a))),3), numpy.uint8)
dimt = imgt.shape

imgf = numpy.zeros((int(abs(dimt[0]*math.cos(a))+abs(dimt[1]*math.sin(a)))+1,int(abs(dimt[0]*math.sin(a))+abs(dimt[1]*math.cos(a)))+1,3), numpy.uint8)
dimf = imgf.shape

org=[0,0]
org[0]=((dimf[0]-dim[0]-1)//2)
org[1]=((dimf[1]-dim[1]-1)//2)

for i in range(dim[0]):
	for j in range(dim[1]):
		imgf[i+org[0]][j+org[1]]=img[i][j]

pos = numpy.zeros((dimt[0]*dimt[1],2), numpy.uint16)

k=0
for i in range(dimt[0]):
	for j in range(dimt[1]):
		pos[k]=[i,j]
		k+=1

mat = numpy.array([[math.cos(-a),-math.sin(-a)],[math.sin(-a),math.cos(-a)]])
newPos=numpy.dot(pos,mat)
pos=newPos.copy()

minx=pos.min(axis=0)

#1
for i in range(k):
	pos[i][0]+=(-minx[0])
	pos[i][1]+=(-minx[1])
	pos[i][0]=(round(pos[i][0]))
	pos[i][1]=(round(pos[i][1]))
	k-=1

pos=pos.astype(int)

k=0
for i in range(dimt[0]):
	for j in range(dimt[1]):
		imgt[i][j]=imgf[pos[k][0]][pos[k][1]]
		k+=1

cv2.imshow("original",img)
cv2.imshow("NearestNeighbour",imgt)

cv2.imwrite("original.jpg",img)
cv2.imwrite("NearestNeighbour.jpg",imgt)

#2
for i in range(k):
	newPos[i][0]+=(-minx[0])
	newPos[i][1]+=(-minx[1])
	k-=1

k=0
for i in range(dimt[0]):
	for j in range(dimt[1]):
		if math.ceil(newPos[k][0])==newPos[k][0]:
			x=numpy.array([[0.5,0.5]])
		else:
			x=numpy.array([[ math.ceil(newPos[k][0])-newPos[k][0] , newPos[k][0]-math.floor(newPos[k][0])]])
		
		if math.ceil(newPos[k][1])==newPos[k][1]:
			y=numpy.array([	[0.5],[0.5] ])
		else:
			y=numpy.array([	[math.ceil(newPos[k][1])-newPos[k][1]],
						[newPos[k][1]-math.floor(newPos[k][1])] ])
		
		points=numpy.array([ 
					[imgf[math.floor(newPos[k][0])][math.floor(newPos[k][1])], imgf[math.floor(newPos[k][0])][math.ceil(newPos[k][1])]], 
					[imgf[math.ceil (newPos[k][0])][math.floor(newPos[k][1])], imgf[math.ceil (newPos[k][0])][math.ceil(newPos[k][1])]]
			   ])

		val=numpy.dot(x,points)

		for l in range(3):
			imgt[i][j][l]=numpy.dot(val[:,:,l],y)
		k+=1

cv2.imshow("bilinear",imgt)
cv2.imshow("bilinear.jpg",imgt)
cv2.waitKey(0)
cv2.destroyAllWindows()
