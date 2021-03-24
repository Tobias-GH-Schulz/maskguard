import cv2
import numpy as np
import imutils
import time
from imutils.video import VideoStream
from face_detector import face_detector
from distance_measurement import get_distance
from annotations import *
from age_gender_detector import get_age_gender

frame_no = 0

# initialize the video stream to get the live video frames
print("[INFO] starting video stream...")
video = cv2.VideoCapture(0)
time.sleep(2.0)

while(video.isOpened()):
    check, frame = video.read()
    if frame is not None:
        frame_no += 1
        frame_copy = frame.copy()

        #Get the frame from the video stream and resize to 400 px
        frame = imutils.resize(frame,width=400)

        # get persons in the picture
        
        # get coordinates and confidence for each detected face
        face_boxes, confidence = face_detector(frame)
        # get distance to cam and close objects 
        pos_dict, close_objects = get_distance(face_boxes)
        # get age and gender
        age, gender = get_age_gender(frame, face_boxes)

        # annotations
        frame_head = annotate_heads(frame, face_boxes, confidence)
        frame_dist = annotate_distance(frame_head, face_boxes, pos_dict, close_objects)
        frame_age = annotate_age_gender(frame_dist, face_boxes, age, gender)
        
        # show the output frame
        cv2.imshow("Frame", frame_age)
        cv2.resizeWindow('Frame',800,800)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
    else:
        break

# do a bit of cleanup
video.release()
cv2.destroyAllWindows()
cv2.waitKey(1)