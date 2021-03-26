import cv2
import numpy as np
import imutils
import datetime
import time
from imutils.video import VideoStream
from Annotater import Annotater
from face_detector import *
from get_distance import *
from age_gender_detector import *
from person_detector import *
from MaskWarning import *
from FaceMaskClassifier import FaceMaskClassifier
from Brightness_optimizer import BrightnessOptimizer
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# set model paths
faceModel = "models/face_model/res10_300x300_ssd_iter_140000.caffemodel"
faceProto = "models/face_model/deploy.prototxt"
genderModel = "models/gender_model/gender_net.caffemodel"
genderProto = "models/gender_model/gender_deploy.prototxt"
ageProto = "models/age_model/age_deploy.prototxt"
ageModel = "models/age_model/age_net.caffemodel"
personProto = "models/person_model/mobilenet.prototxt"
personModel = "models/person_model/mobilenet.caffemodel"
maskModel = "models/mask_model/mnv2_mask_classifier_v4.pth"

warn = MaskWarning(cooldown=5)
brightOpt = BrightnessOptimizer()
# initialize detectors
face_detector = FaceDetector(faceProto, faceModel)
FACE_CONFID_THRESH = 0.3
age_gender_detector = AgeGenderDetector(ageProto, ageModel,
                                        genderProto, genderModel)
person_detector = PersonDetector(personProto, personModel)
BODY_CONFID_THRESH = 0.5
face_mask_classifier = FaceMaskClassifier(maskModel)
# initialize distance measurement
'''
FOCAL = (P x  D) / W
P = height of reference object on picture in pixels
D = distance of reference object to camera when photo was taken in cm
W = actual heigt of reference object 
'''

DIST_REF = 22
FOCAL = int((309 *  100) / DIST_REF)
dist = Distance(FOCAL, DIST_REF)

# initialize ent_time for audio_warning
end_time = datetime.datetime.now()

# initialize the video stream to get the live video frames
frame_no = 0
print("[INFO] starting video stream...")
video = cv2.VideoCapture(0)
time.sleep(2.0)
soundOn = False

def cropout(img, box):
    return img[box[1]:box[3], box[0]:box[2]]

while(video.isOpened()):
    check, frame = video.read()
    frameOpt = frame
    #frameOpt = brightOpt.optimize(frame)
    if frame is not None:
        annotater = Annotater(frame)
        face_crops = []
        face_boxes, _ = face_detector.detect(frameOpt, FACE_CONFID_THRESH)
        if len(face_boxes):
            annotater.faces += face_boxes
            face_crops = [cropout(frameOpt, face_box) for face_box in face_boxes]
        else:
            body_boxes, _ = person_detector.detect(frameOpt, BODY_CONFID_THRESH)
            if len(body_boxes) != 0:
                annotater.bodies += body_boxes
                body_crops = [cropout(frameOpt, body_box) for body_box in body_boxes]

                for body_crop, body_box in zip(body_crops, body_boxes):
                    face_box, _ = face_detector.detect(body_crop, FACE_CONFID_THRESH, single=True)
                    if len(face_box) > 0:
                        face_crops.append(cropout(body_crop, face_box))
                        annotater.faces.append(annotater.recalc(face_box, body_box))

        if len(face_crops) != 0:
            for face_crop in face_crops:
                #age, gender =
                annotater.mask_statuses.append(face_mask_classifier.predict(face_crop))

            annotater.dist_measure.append(dist.measure(annotater.faces))
            frame = annotater.update()

            if soundOn:
                warn.probe(bool("no_mask" in annotater.mask_statuses))
            # show the output frame
        cv2.imshow("Frame", frame)
        cv2.resizeWindow('Frame',800,800)
        key = cv2.waitKey(1) & 0xFF
        del annotater
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
        if key == ord("s"):
            print("Sound:", soundOn)
            soundOn = not soundOn
    else:
        break

# do a bit of cleanup
video.release()
cv2.destroyAllWindows()
cv2.waitKey(1)