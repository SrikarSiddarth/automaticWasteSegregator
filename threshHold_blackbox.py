import cv2 as cv
import numpy as np

img1 = cv.imread('/home/srikarsiddarth/projects/garbageSegregator/a3.jpeg')
img2 = cv.imread('/home/srikarsiddarth/projects/garbageSegregator/b3.jpeg')

def preprocess(img):
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	ret, thresh = cv.threshold(gray, 180, 255, cv.THRESH_BINARY)
	_, cont, _ = cv.findContours(thresh, 1, 3)
	
	area = 0
	for i in range(len(cont)):
		if cv.contourArea(cont[i])>area:
			area = cv.contourArea(cont[i])
			k=i
	M = cv.moments(cont[k])
	print(cv.contourArea(cont[k]))
	cv.drawContours(img, [cont[k]], 0, (255,255,0), 5)
	cv.imshow('d', img)
	cv.waitKey(0)
	if M['m00']!=0:
		x = (M['m10']/M['m00'])
		y = (M['m01']/M['m00'])
		return x,y
	else:
		return None, None
x1, y1 = preprocess(img1)
x2, y2 = preprocess(img2)
dist = np.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))


print('displacement of bright contour : '+str(dist))
if dist> 0.15: 
	shine="Shiny"
	print('This is a shiny object.')
else :
	shine="Dull"
	print('This is a dull object.')

# When everything done, release the capture
cap.release()
cv.imwrite('img1.png', img1)
cv.imwrite('img2.png',img2)
cv.destroyAllWindows()
