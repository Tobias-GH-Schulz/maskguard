import cv2, time, pandas
from datetime import datetime
import numpy as np

class Motion:
    @staticmethod
    def capture_background():
        print("Press c to capture background")
        video = cv2.VideoCapture(0)
        while(video.isOpened()):
            frame = video.read()[1]
            cv2.imshow("Capturing",frame)
            key = cv2.waitKey(1)
            if key == ord('c'):
                captured_frame = video.read()[1]
                print("Background captured")
                break
        video.release()
        cv2.destroyAllWindows 
        cv2.waitKey(1)
        return captured_frame

    def detector(frame, static_back):
        print("Motion detector active")
        motion_boxes = []
        # Converting color image to gray_scale image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        static_back_gray = cv2.cvtColor(static_back, cv2.COLOR_BGR2GRAY)

        # Difference between static background and current frame
        diff_frame = cv2.absdiff(static_back_gray, gray)

        # If change in between static background and
        # current frame is greater than 50 it will show white color(255)
        thresh_frame = cv2.threshold(diff_frame, 50, 255, cv2.THRESH_BINARY)[1]
                
        kernel = np.ones((9,9),np.uint8)
        opened_frame = cv2.morphologyEx(thresh_frame, cv2.MORPH_OPEN, kernel)
        dil_frame = cv2.dilate(opened_frame, None, iterations = 30)


        # Finding contour of moving object
        cnts,_ = cv2.findContours(thresh_frame.copy(), 
                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                print(cv2.contourArea(contour))
                continue
            
            (x, y, w, h) = cv2.boundingRect(contour)
            startX, startY, endX, endY = x, y, x+w, y+h
            motion_boxes.append((startX, startY, endX, endY))
        print(len(motion_boxes))
        print(motion_boxes)
        if len(motion_boxes) > 1:
            motion_boxes = tuple(motion_boxes)
        
        return motion_boxes, dil_frame, opened_frame, thresh_frame, diff_frame
