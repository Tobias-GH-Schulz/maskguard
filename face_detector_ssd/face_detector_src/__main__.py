import cv2
import numpy as np
import imutils
import time
from imutils.video import VideoStream
from face_detector import face_detector
from distance_measurement import get_distance
from annotations import *
from gender_detector import get_gender

frame_no = 0

# initialize the video stream to get the live video frames
print("[INFO] starting video stream...")
video = cv2.VideoCapture(0)
time.sleep(2.0)

while(video.isOpened()):
    check, frame = video.read()
    if frame is not None:
        frame_no += 1

        #Get the frame from the video stream and resize to 400 px
        frame = imutils.resize(frame,width=400)

        face_boxes, confidence = face_detector(frame)
        pos_dict, close_objects = get_distance(face_boxes)
        gender = get_gender(frame, face_boxes)
        # get the faces

        # annotations
        frame = annotate_heads(frame, face_boxes, confidence)
        frame = annotate_distance(frame, face_boxes, pos_dict, close_objects)
        frame = annotate_gender(frame, face_boxes, gender)

        # show the output frame
        cv2.imshow("Frame", frame)
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