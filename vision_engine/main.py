import cv2
import numpy as np
import pandas as pd

cap = cv2.VideoCapture(0)

while True:
    success , frame = cap.read()

    if not success :
        print("unable to open camera")
        break

    cv2.rectangle(frame , (100 , 100) , (200 , 200) ,(255 , 255 , 255)  , 4)

    cv2.imshow("face selected image",frame)

    if cv2.waitKey(1) & 0xff == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()