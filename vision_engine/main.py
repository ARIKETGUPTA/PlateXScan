import cv2
import numpy as np
import pandas as pd

# cap = cv2.VideoCapture(0)

# while True:
#     success , frame = cap.read()

#     if not success :
#         print("unable to open camera")
#         break

#     cv2.rectangle(frame , (100 , 100) , (200 , 200) ,(255 , 255 , 255)  , 4)

#     cv2.imshow("face selected image",frame)

#     if cv2.waitKey(1) & 0xff == ord('q') :
#         break

# cap.release()
# cv2.destroyAllWindows()


# 1. Open the camera stream
cap = cv2.VideoCapture(0)

print("Camera Active! Position something (like a phone or paper) inside the box.")
print("Press 'q' to close the program.")

while True:
    success, frame = cap.read()
    if not success:
        print("Error reading frame.")
        break
        
    # Get the camera dimensions dynamically
    height, width, _ = frame.shape
    
    # 2. Define the box coordinates (Let's make a clear box right in the middle)
    x_start, y_start = int(width * 0.35), int(height * 0.4)
    x_end, y_end = int(width * 0.65), int(height * 0.6)
    
    # 3. CROP the area *BEFORE* drawing the line 
    # (If we draw the line first, the crop will include the green box border!)
    # Remember the golden rule: NumPy arrays are sliced as [Y_axes, X_axes]
    cropped_roi = frame[y_start:y_end, x_start:x_end]
    
    # 4. DRAW the green target box on the main frame for you to see
    cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
    
    # 5. Show both windows simultaneously
    cv2.imshow("Main Camera View", frame)
    cv2.imshow("Live Cropped Preview (ROI)", cropped_roi)
    
    # Break loop safely if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources cleanly
cap.release()
cv2.destroyAllWindows()