import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hls= cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    xyz = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('hls', hls)
    cv2.imshow('xyz', xyz)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()