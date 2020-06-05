import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

<<<<<<< HEAD

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindo
qws()
=======
# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
>>>>>>> c476dc85e1e5552366a169f069ea40783fb9c2a1
