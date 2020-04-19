def face_count(imagepath):
	import cv2 
	import sys  

	cascPath = "haarcascade_frontalface_default.xml"


	faceCascade = cv2.CascadeClassifier(cascPath)
	image = cv2.imread(imagepath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	faces = faceCascade.detectMultiScale(
	    gray,
	    scaleFactor=1.1,
	    minNeighbors=3,        # to tune the face count
	    minSize=(30, 30)
	)

	print("Found {0} faces!".format(len(faces)))

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
	    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

	cv2.imshow("Faces found", image)
	cv2.waitKey(0)


img_path="F:\\ComputerVision\\Faces_Count\\Images\\crowd-1.jpg"
face_count(img_path)


