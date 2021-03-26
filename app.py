import streamlit as st
import cv2
import numpy as np
import pandas as pd
import os 
import base64
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
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

#Background
main_bg = '/Users/aderemifayoyiwa/Downloads/back.jpg'
main_bg_ext = 'jpg'

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

#Title
st.title('Mask Detector')

#Creating sidebar
expander = st.sidebar.beta_expander('Ready to check our model?')
expander.write('All you need is a device with camera')

expander = st.sidebar.beta_expander('The team')
expander.write('Marcin Szleszynski')
expander.write('Aderemi Fayoyiwa')
expander.write('Tobias Schulz')


#Creating expanders for different sections
st.markdown('## **Introduction**')
st.write("In this present time, it is important to consider one's own \nsafety and the safety of others by wearing a face mask. \nOur model is trained not only to detect if people wear masks \nbut also if they wear them correctly.")

st.markdown('## **Technologies**')
expander = st.beta_expander('Technologies used')
expander.write('Github')
expander.write('Streamlit')
expander.write('Pytorch')

st.markdown('## **Model training**')
expander = st.beta_expander('Model')
expander.write('Method: mobilenetV2')

st.markdown('## **Model functions**')
expander = st.beta_expander('Functions')
expander.markdown('\n * Detect face \n * Check for mask \n * Give warning if need be')

st.markdown('## **Data collection and analysis**')
expander = st.beta_expander('Data')
expander.write('Source: ')

st.markdown('## **Model demo**')
st.markdown('### **Displayed distance might differ**')
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Click for demo')
if pressed:
	st.markdown('**_Check the run box for demo and uncheck when done_**')
    

# set model paths
faceModel = "models/face_model/res10_300x300_ssd_iter_140000.caffemodel"
faceProto = "models/face_model/deploy.prototxt"
genderModel = "models/gender_model/gender_net.caffemodel"
genderProto = "models/gender_model/gender_deploy.prototxt"
ageProto = "models/age_model/age_deploy.prototxt"
ageModel = "models/age_model/age_net.caffemodel"
personProto = "models/person_model/mobilenet.prototxt"
personModel = "models/person_model/mobilenet.caffemodel"
maskModel = "models/mask_model/mnv2_mask_classifier_v3.pth"

# initialize detectors
face_detector = FaceDetector(faceProto, faceModel)
FACE_CONFID_THRESH = 0.3
age_gender_detector = AgeGenderDetector(ageProto, ageModel,
                                        genderProto, genderModel)
person_detector = PersonDetector(personProto, personModel)
BODY_CONFID_THRESH = 0.5
face_mask_classifier = FaceMaskClassifier(maskModel)
# initialize distance measurement
#'''
#FOCAL = (P x  D) / W
#P = height of reference object on picture in pixels
#D = distance of reference object to camera when photo was taken in cm
#W = actual heigt of reference object 
#'''

DIST_REF = 22
FOCAL = int((309 *  100) / DIST_REF)
dist = Distance(FOCAL, DIST_REF)

# initialize ent_time for audio_warning
end_time = datetime.datetime.now()

# initialize the video stream to get the live video frames
frame_no = 0
#print("[INFO] starting video stream...")
video = cv2.VideoCapture(0)
time.sleep(2.0)

def cropout(img, box):
    print("BOX", box)
    return img[box[1]:box[3], box[0]:box[2]]

#Setting video feed
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])

while run:
    check, frame = video.read()
    if frame is not None:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        annotater = Annotater(frame)
        face_crops = []
        face_boxes, _ = face_detector.detect(frame, FACE_CONFID_THRESH)
        if len(face_boxes):
            annotater.faces += face_boxes
            face_crops = [cropout(frame, face_box) for face_box in face_boxes]
        else:
            body_boxes, _ = person_detector.detect(frame, BODY_CONFID_THRESH)
            print(body_boxes)
            if len(body_boxes) != 0:
                annotater.bodies += body_boxes
                body_crops = [cropout(frame, body_box) for body_box in body_boxes]

                for body_crop, body_box in zip(body_crops, body_boxes):
                    face_box, _ = face_detector.detect(body_crop, FACE_CONFID_THRESH, single=True)
                    if len(face_box) > 0:
                        print("DET", face_box)
                        face_crops.append(cropout(body_crop, face_box))
                        annotater.faces.append(annotater.recalc(face_box, body_box))

        if len(face_crops) != 0:
            for face_crop in face_crops:
                #age, gender =
                annotater.mask_statuses.append(face_mask_classifier.predict(face_crop))

            annotater.dist_measure.append(dist.measure(annotater.faces))
            frame = annotater.update()

        '''
        # play warning
        if len(face_crops) > 0:
            state = "mask"
        else:
            state = "no mask"
        start_time = datetime.datetime.now()
        warn = MaskWarning(start_time, end_time)
        end_time= warn.play_sound(state)
        '''

        # show the output frame
        FRAME_WINDOW.image(frame)
        #cv2.imshow("Frame", frame)
        #cv2.resizeWindow('Frame',800,800)
        key = cv2.waitKey(1) & 0xFF
        del annotater
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
    else:
        break
st.markdown('**_Impressed? I bet!_**')

# do a bit of cleanup
video.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
