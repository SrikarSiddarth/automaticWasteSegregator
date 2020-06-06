import cv2 as cv
import numpy as np
import requests
# if you are using ip webcam, then uncomment the following, other wise comment it
# url= "http://192.168.1.3:8080/shot.jpg"

# if you are using wired camera, uncomment the following, otherwise comment it
cap = cv.VideoCapture(0)

frame = None
k = 0
while(True):
	# if you are using ip webcam, then uncomment the following, other wise comment it
	# img_resp = requests.get(url)
	# im_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
	# frame = cv.imdecode(im_arr, -1)

	# if you are using wired camera, uncomment the following as well as cap.release() found at the end of the code, otherwise comment it
	ret, frame = cap.read()
	if frame is not None and k==0:
		img1 = frame
		k=1
		continue
	elif k==1:
		input('press any key to capture second image...')
		img2 = frame
		break

# Our operations on the frame come here

img1 = cv.resize(img1, (1080, 1080))
img2 = cv.resize(img2, (1080, 1080))

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