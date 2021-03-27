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
from FaceDetector import *
from GetDistance import *
from AgeGenderDetector import *
from PersonDetector import *
#from MaskWarning import *
from FaceMaskClassifier import FaceMaskClassifier
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

#Background
#main_bg = '/Users/aderemifayoyiwa/Downloads/back.jpg'
#main_bg_ext = 'jpg'

#st.markdown(
#    f"""
#    <style>
#    .reportview-container {{
#        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
#    }}
#    </style>
#    """,
#    unsafe_allow_html=True
#)

#Title
st.title('Mask-NoMask-Detector')
#st.image('/Users/aderemifayoyiwa/Downloads/face_mask.jpeg')

#Creating sidebar
expander = st.sidebar.beta_expander('Impressed and interested?')
expander.write("Contact M.A.T and let's make your business a safer place")

expander = st.sidebar.beta_expander('The team')
expander.write('Marcin Szleszynski')
expander.write('Aderemi Fayoyiwa')
expander.write('Tobias Schulz')


#Creating expanders for different sections
st.markdown('## **Introduction**')
st.write("In this present time, it is important to consider one's own \nsafety and the safety of others by wearing a face mask. \nCorona virus is still spreading and causing a lot of \nfinancial problems and health issues.")
st.markdown("\n * an estimate of 26 perecent of SMBs have been closed down by the authorities during the pandemic.")
st.markdown('\n * In order to help keep SMBs afloat, we at M.A.T invented the MNMD, a Mask-NoMask Detector that detects if your customers are wearing masks or not and only lets them enter your business if they are wearing one')
st.markdown('\n * Our highly educated team put all their knowledge in deep learning and computer vision together to create a tool that gives you one less thing to worry about in this trying times')

st.markdown('## **Technologies**')
expander = st.beta_expander('Technologies used')
expander.write('- Pytorch')
expander.write('- OpenCV')
expander.write('- Github')
expander.write('- Streamlit')

st.markdown('## **Model training**')
expander = st.beta_expander('Model')
expander.write('Method1: Transfer learning (MobileNetV2)')
expander.write('Method2: Computer vision')

st.markdown('## **Dataset**')
expander = st.beta_expander('Data')
expander.write('Source: Custom dataset from Strive School and Chinese dataset')
expander.write('Training: 2348')
expander.write('Validation: 784')
expander.write('Test: 784')

st.markdown('## **Application features**')
expander = st.beta_expander('Features')
expander.write('- EFD (enhanced face detection)')
expander.write('- The MNMD uses a unique two stage multidetector to detect faces in the image:')
expander.markdown('\n * - Single Shot Multibox Detector (SSD) based on a pretrained RESNET10 which directly detects faces \n * - if the first SSD fails to detect a face the second stage gets activated and tries to detect persons using a pre-trained MOBILENET if a person is detected the area of the person gets cropped from the image and is then passed to the first stage SSD')
expander.write('- Well trained Mask-NoMask Classifier')
expander.write('- Brightness optimizer')
expander.write('- Safe distance Measurement')
expander.write('- Customizable alarm system ')


st.markdown('## **What next?**')
expander = st.beta_expander('Proposed adjustments')
expander.write('- Motion detector to optimize the face detection')
expander.write('- Enhance the alarm system')
expander.write('- Further brightness and image optimization')


st.markdown('## **Model demo**')
st.markdown('**Please note that displayed distance might differ**')
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

       

        # show the output frame
        FRAME_WINDOW.image(frame)

        key = cv2.waitKey(1) & 0xFF
        del annotater
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
    else:
        break
st.markdown('**_Impressed? We bet!_**')

# do a bit of cleanup
#video.release()
#cv2.destroyAllWindows()
#cv2.waitKey(1)
