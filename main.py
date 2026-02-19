import cv2
import numpy as np
import math

def detect_hand_gesture():
    # start webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        
        roi = frame[100:300, 100:300]
        
        cv2.rectangle(frame, (100,100), (300, 300), (0, 255,0), 2)
        
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (35, 35), 0)
        
        _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            contour = max(contours, key=cv2.contourArea)
            
            hull = cv2.convexHull(contour)
            
            cv2.drawContours(roi, [contour], -1, (0, 255, 0), 2)
            cv2.drawContours(roi, [hull], -1, (0, 255, 0),2 )
            
            hull_indices = cv2.convexHull(contour, returnPoints=False)
            defects = cv2.convexityDefects(contour, hull_indices)
            
            if defects is not None:
                finger_count = 0 
                
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(contour[s][0])
                    end = tuple(contour[e][0])
                    far = tuple(contour[f][0])
                    
                    a = math.dist(start, end)
                    b = math.dist(start, far)
                    c = math.dist(end, far)
                    
                    angle = math.acos((b**2 + c**2 - a**2) / (2 * b * c)) * 57
                    
                    if angle < 90:
                        finger_count += 1
                        cv2.putText(frame, f"Fingers: {finger_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                cv2.putText(frame, f"Fingers: {finger_count + 1}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
                
        cv2.imshow("Hand Gesture Recognition", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

detect_hand_gesture()