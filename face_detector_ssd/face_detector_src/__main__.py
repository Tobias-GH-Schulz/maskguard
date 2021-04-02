import cv2
import numpy as np
import imutils
import time
import datetime
from imutils.video import VideoStream
from face_detector import *
from get_distance import *
from annotations import *
from age_gender_detector import *
from person_detector import *
from cap_background import *
from person_mask import *
from Brightness_optimizer import *
from warning import *
from MotionDetector import *

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
# capture background from first 30 frames
# backgroundFrame = Background().capture(capture_duration = 2)
# initialize the background mask
# keep person out of video for the first video shot
# mask = Mask(backgroundFrame)

# initialize ent_time for audio_warning
#end_time = datetime.datetime.now()

# initialize the video stream to get the live video frames

print("[INFO] starting video stream...")
video = cv2.VideoCapture(0)
time.sleep(2.0)

BACKGROUND = Motion.capture_background()

while(video.isOpened()):
    check, frame = video.read()
    if frame is not None:

        #Get the frame from the video stream and resize to 400 px
        #frame = imutils.resize(frame,width=400)
        frame_copy = frame.copy()
        
        # brightness optimizing
        frame_optimized = BrightnessOptimizer().optimize(frame)
        #frame_agwcd = BrightnessOptimizer().image_agcwd(frame)
        frame_a_g_c = BrightnessOptimizer().a_g_c(frame)
        (Im,th,th1,cls,g,RGB) = BrightnessOptimizer().ContrastStretching(frame)
        #streched_contrast = BrightnessOptimizer().ContrastStretching2(frame, 60)
        
        # masking
        #masked_frame = mask.create(frame_copy, 11)
        body_boxes, dil_frame, opened_frame, thresh_frame, diff_frame = Motion.detector(frame, BACKGROUND)
        #person_boxes, person_confidence = person_detector.detect(frame, 0.95)
        # get coordinates and confidence for each detected face
        face_boxes, face_confidence = face_detector.detect(frame, 0.3) 
        # get distance to cam and close objects 
        pos_dict, close_objects = dist.measure(face_boxes)
        # get age and gender
        #age, gender = age_gender_detector(face)
        
        # annotations
        #frame_person = annotate_heads(frame, person_boxes, person_confidence)
        frame_head = annotate_heads(frame, face_boxes, face_confidence)
        #frame_dist = annotate_distance(frame, face_boxes, pos_dict, close_objects)
        #frame_age = annotate_age_gender(frame_dist, face_boxes, age, gender)
        
        '''
        # play warning
        if len(face_boxes) > 0:
            state = "mask"
        else:
            state = "no mask"
        start_time = datetime.datetime.now()
        warn = MaskWarning(start_time, end_time)
        end_time= warn.play_sound(state)
        '''

        # show the output frame
        cv2.imshow("BACKGROUND", BACKGROUND)
        cv2.imshow("Dilated frame", dil_frame)
        cv2.imshow("Opened frame", opened_frame)
        cv2.imshow("Thresholded frame", thresh_frame)
        cv2.imshow("Differenced frame", diff_frame)
        cv2.imshow("Frame", frame)
        #cv2.imshow("Frame optimized", frame_optimized)
        #cv2.imshow("Frame agwcd", frame_agwcd)
        #cv2.imshow("Frame a_g_c", frame_a_g_c)
        #cv2.imshow("Frame Im", Im)
        #cv2.imshow("Frame Strechted2", Im)

        #cv2.imshow("Masked Back", masked_frame)
        cv2.resizeWindow('Frame',300,300)
        cv2.resizeWindow('BACKGROUND',300,300)
        cv2.resizeWindow('Dilated frame',300,300)
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