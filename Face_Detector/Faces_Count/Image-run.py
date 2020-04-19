import cv2
 
vc = cv2.VideoCapture('sample.mp4')
c=1
fps = 24
 
if vc.isOpened():
	rval , frame = vc.read()
else:
	rval = False
 
while rval:
	rval, frame = vc.read()
	cv2.imshow("Result",frame)
	cv2.waitKey(1000 / fps);
	vc.release()