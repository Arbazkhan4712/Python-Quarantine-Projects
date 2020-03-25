# STANDARD LIBRARY IMPORT
import os
import sys
# THIRD PARTY LIBRARIES
import cv2
from send_mail import send_mail


def detector():

    # VideoCapture will literally capture the first camera that it sees
    # available on your raspberry!
    cap = cv2.VideoCapture(0)

    # Loads the face_cascade classifier.
    face_cascade = cv2.CascadeClassifier(os.path.dirname(sys.argv[0]) +
                                         '/haarcascade_frontalface_alt2.xml')

    # Starts the infinite loop!
    while True:
        # capture frame-by-frame
        ret, frame = cap.read()

        # If there is any face on the camera, our cascade classifier will
        # return the position of the faces (if more than one) that are in the
        # screen else returns None.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)

        # Loop over the faces and draws a Green Square of 2px on the face!
        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
            send_mail(frame=frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # If you press q, the screen will close
        # and the script will leave the loop.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done release the capture
    cap.release()
    cv2.destroyAllWindows()


detector()
