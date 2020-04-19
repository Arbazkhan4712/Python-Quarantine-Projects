import cv2
import sys

face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
vc = cv2.VideoCapture('sample.mp4')

if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False
    roi = [0,0,0,0]
 
while rval:
    rval, frame = vc.read()
     
    # resize frame for speed.
    frame = cv2.resize(frame, (300,200))
     
    # face detection.
    faces = face_cascade.detectMultiScale(frame, 1.8, 2)
    nfaces = 0
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        nfaces = nfaces + 1
        roi = [x,y,w,h]
         
    # undetected face, show old on position.
    if nfaces == 0:
        cv2.rectangle(frame,(roi[0],roi[1]),(roi[0]+roi[2],roi[1]+roi[3]),(0,0,255),2)
     
    # show result
    cv2.imshow("Result",frame)
    cv2.waitKey(1);
    vc.release()
