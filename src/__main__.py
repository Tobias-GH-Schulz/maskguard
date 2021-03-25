import cv2
import numpy as np
import imutils
import time
from imutils.video import VideoStream
from Annotater import Annotater
from face_detector import *
from get_distance import *
from age_gender_detector import *
from person_detector import *
from FaceMaskClassifier import FaceMaskClassifier

# set model paths
faceModel = "models/face_model/res10_300x300_ssd_iter_140000.caffemodel"
faceProto = "models/face_model/deploy.prototxt"
genderModel = "models/gender_model/gender_net.caffemodel"
genderProto = "models/gender_model/gender_deploy.prototxt"
ageProto = "models/age_model/age_deploy.prototxt"
ageModel = "models/age_model/age_net.caffemodel"
personProto = "models/person_model/mobilenet.prototxt"
personModel = "models/person_model/mobilenet.caffemodel"
maskModel = "models/mask_model/mnv2_mask_classifier_v2.pth"
# initialize detectors
face_detector = FaceDetector(faceProto, faceModel)
FACE_CONFID_THRESH = 0.6
age_gender_detector = AgeGenderDetector(ageProto, ageModel,
                                        genderProto, genderModel)
person_detector = PersonDetector(personProto, personModel)
BODY_CONFID_THRESH = 0.9
face_mask_classifier = FaceMaskClassifier(maskModel)
# initialize distance measurement
FOCAL = 290
DIST_REF = 22
dist = Distance(FOCAL, DIST_REF)

# initialize the video stream to get the live video frames
frame_no = 0
print("[INFO] starting video stream...")
video = cv2.VideoCapture(0)
time.sleep(2.0)

def cropout(img, box):
    print("BOX:", box)
    return img[box[1]:box[3], box[0]:box[2]]

while(video.isOpened()):
    check, frame = video.read()
    if frame is not None:
        annotater = Annotater(frame)
        frame_no += 1
        #Get the frame from the video stream and resize to 300 px
        #frame = imutils.resize(frame,width=300)

        face_boxes, _ = face_detector.detect(frame, FACE_CONFID_THRESH)
        annotater.faces += face_boxes
        face_crops = [cropout(frame, face_box) for face_box in face_boxes]
        body_boxes, _ = person_detector.detect(frame, BODY_CONFID_THRESH)

        if len(body_boxes) != 0:
            annotater.bodies += body_boxes
            body_crops = [cropout(frame, body_box) for body_box in body_boxes]

            face_boxes = [face_detector.detect(body_crop, FACE_CONFID_THRESH)[0] for body_crop in body_crops]
            face_crops += [cropout(body_crop, face_box) for body_crop, face_box in zip(body_crops, face_boxes)]
            for face_box, body_box in zip(face_boxes, body_boxes):
                annotater.faces += annotater.recalc(face_box, body_box)

        if len(face_crops) != 0:
            for face_crop in face_crops:
                #age, gender =
                annotater.mask_statuses.append(face_mask_classifier.predict(face_crop))

            pos_dict, close_objects = dist.measure(annotater.faces)
            frame = annotater.update()

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