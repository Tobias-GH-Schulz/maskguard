import cv2
import numpy as np
import imutils
import time
from imutils.video import VideoStream
from face_detector import *
from get_distance import *
from annotations import *
from age_gender_detector import *
from person_detector import *

# set model paths
personModel = "../face_detector_model/person_model/mobilenet.caffemodel"
personProto = "../face_detector_model/person_model/mobilenet.prototxt"
faceModel = "../face_detector_model/face_model/res10_300x300_ssd_iter_140000.caffemodel"
faceProto = "../face_detector_model/face_model/deploy.prototxt"
genderModel = "../face_detector_model/gender_model/gender_net.caffemodel"
genderProto = "../face_detector_model/gender_model/gender_deploy.prototxt"
ageProto = "../face_detector_model/age_model/age_deploy.prototxt"
ageModel = "../face_detector_model/age_model/age_net.caffemodel"

# initialize detectors
person_detector = PersonDetector(personProto, personModel)
face_detector = FaceDetector(faceProto, faceModel)
age_gender_detector = AgeGenderDetector(ageProto, ageModel, 
                                        genderProto, genderModel)
# initialize distance measurement
focal = 290
distRef = 22   
dist = Distance(focal, distRef) 

# initialize the video stream to get the live video frames
frame_no = 0
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

        person_boxes, person_confidence = person_detector.detect(frame, 0.95)
        # get coordinates and confidence for each detected face
        face_boxes, face_confidence = face_detector.detect(frame, 0.5) 
        # get distance to cam and close objects 
        pos_dict, close_objects = dist.measure(face_boxes)
        # get age and gender
        #age, gender = age_gender_detector(face)
        
        # annotations
        frame_person = annotate_heads(frame, person_boxes, person_confidence)
        frame_head = annotate_heads(frame, face_boxes, face_confidence)
        frame_dist = annotate_distance(frame, face_boxes, pos_dict, close_objects)
        #frame_age = annotate_age_gender(frame_dist, face_boxes, age, gender)
        
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