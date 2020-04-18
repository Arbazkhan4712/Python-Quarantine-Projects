# Capture video from webcam 
import cv2


# Load the Haar cascades

face_cascade = cv2.CascadeClassifier('faces.xml')
eyes_cascade = cv2.CascadeClassifier('eyes.xml')

# Define function that will do detection
def detect(gray, frame):
  """ Input = greyscale image or frame from video stream
      Output = Image with rectangle box in the face
  """
  # Now get the tuples that detect the faces using above cascade
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  # faces are the tuples of 4 numbers
  # x,y => upperleft corner coordinates of face
  # width(w) of rectangle in the face
  # height(h) of rectangle in the face
  # grey means the input image to the detector
  # 1.3 is the kernel size or size of image reduced when applying the detection
  # 5 is the number of neighbors after which we accept that is a face
  
  # Now iterate over the faces and detect eyes
  for (x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    # Arguements => image, top-left coordinates, bottomright coordinates, color, rectangle border thickness
    
    # we now need two region of interests(ROI) grey and color for eyes one to detect and another to draw rectangle
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    # Detect eyes now
    eyes = eyes_cascade.detectMultiScale(roi_gray, 1.1, 3)
    # Now draw rectangle over the eyes
    for (ex, ey, ew, eh) in eyes:
      cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)
      
  return frame


video_capture = cv2.VideoCapture(0)
# Run the infinite loop
while True:
  # Read each frame
  _, frame = video_capture.read()
  # Convert frame to grey because cascading only works with greyscale image
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Call the detect function with grey image and colored frame
  canvas = detect(gray, frame)
  # Show the image in the screen
  cv2.imshow("Video", canvas)
  # Put the condition which triggers the end of program
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
video_capture.release()
cv2.destroyAllWindows()

