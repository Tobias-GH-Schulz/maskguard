import logging
import logging.handlers
import queue
import urllib.request
from pathlib import Path
#from typing import List, NamedTuple

#try:
#    from typing import Literal
#except ImportError:
#    from typing_extensions import Literal  # type: ignore

import av
import cv2
import numpy as np
import streamlit as st
from aiortc.contrib.media import MediaPlayer
from PIL import Image
import pandas as pd
import os 

from src.Annotater import Annotater
from src.FaceDetector import *
from src.GetDistance import *
from src.BodyDetector import *
from src.MaskWarning import *
from src.FaceMaskClassifier import FaceMaskClassifier

FACE_MODEL = "src/models/face_model/res10_300x300_ssd_iter_140000.caffemodel"
FACE_PROTO = "src/models/face_model/deploy.prototxt"
BODY_MODEL = "src/models/body_model/mobilenet.caffemodel"
BODY_PROTO = "src/models/body_model/mobilenet.prototxt"
MASK_MODEL = "src/models/mask_model/mnv2_mask_classifier_v3.pth"
FACE_CONFID_THRESH = 0.3
BODY_CONFID_THRESH = 0.5

from streamlit_webrtc import (
    ClientSettings,
    VideoTransformerBase,
    WebRtcMode,
    webrtc_streamer,
)

HERE = Path(__file__).parent

logger = logging.getLogger(__name__)

WEBRTC_CLIENT_SETTINGS = ClientSettings(
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
)


def main():
    content()

    mask_detection_page = (
        "Real time demo"
    )
    video_upload_page = "Upload a video"
    app_mode = st.sidebar.selectbox(
        "Choose the app mode",
        [
            mask_detection_page,
            video_upload_page,
        ],
    )

    sidebar()

    st.subheader(app_mode)

    if app_mode == mask_detection_page:
        app_mask_detection()
    elif app_mode == video_upload_page:
        app_video_upload()

def content():
    icon = Image.open("images/logo_symbol.png")
    st.set_page_config(
        page_title="MASK GUARD",
        page_icon=icon,
        layout="wide",
        initial_sidebar_state="auto",
        )

    col1, col2, col3 = st.beta_columns([1,3,1])

    image1 = Image.open("images/logo_large.png")
    col1.header(" ")

    col2.header(" ")
    col2.image(image1, use_column_width = True)

    col3.header(" ")

    st.write(" ")
    st.markdown("<h2 style='text-align: center; color: black;'>Are you looking for a way to make your business a safer place during this corona pandemic?</h2>", unsafe_allow_html=True)
    st.write(" ")

    col1, col2, col3 = st.beta_columns([2,3,1])

    col1.header(" ")

    col2.header(" ")
    col2.markdown("![Gif](https://media.giphy.com/media/vhy6Rp04tynvmeu2Nl/giphy.gif)")

    col3.header(" ")
    

    st.title("Why Mask Guard?")
    st.markdown("""
                We are living in the dangerous and uncertain time of a pandemic.
                A huge amount of SMBs has been closed down by the authorities 
                during the pandemic. Do you also want to be one of them because your 
                business has been declared a super spreader location? 
                Of course not! And thats why we invented the Mask Gurad, a Mask-No-Mask 
                detector that detects if your customers are wearing a mask or not and only 
                lets them enter your business if they are wearing one. 
                Our highly educated team put all their knowledge in deep learning and computer vision 
                together to create a tool that gives you one thing that lets you and also your customers
                sleep well at night: SECURITY!
                """)

    st.subheader("Together we will make the world a saver and healthier place")

    features()

    #st.markdown("With our freshly created set of CSV files we need to work some pandas magic and "
    #            "wrangle this into something useful. Cleaning data was key, although much of this had been done in scraping, then we needed to make some dataframes for analysis. We wanted to explore how the ratings played a role im the rankings, so we performed some normalisations on the ratings data.")
    #st.markdown("The code we used for this process can be found [here]("
    #            "<https://github.com/jobyid/strive_build_good_reads/blob/main/good_reads_preprocessing.py>) ")    


def sidebar():
    with st.sidebar.beta_container():
        #st.subheader("The Team of MASK GUARD")
        #st.markdown("[**Aderemi Fayoyiwa**](<https://github.com/AderemiF>)")
        #st.image("images/aderemi.png",use_column_width=True)
        #st.markdown("[**Tobias Schulz**](<https://github.com/Tobias-GH-Schulz>)")
        #st.image("images/Tobi.png",use_column_width=True)
        #st.markdown("""[**Marcin Szleszynski**](<https://github.com/martinezpl>)""")
        #st.image("images/Marcin.png",use_column_width=True)
        team1, team2, team3 = st.beta_columns(3)
        with team1:
            st.markdown("[**Aderemi Fayoyiwa**](<https://github.com/AderemiF>)")
            st.image("images/aderemi.png",use_column_width=True)
        with team3:
            st.markdown("[**Tobias Schulz**](<https://github.com/Tobias-GH-Schulz>)")
            st.image("images/Tobi.png",use_column_width=True)
        with team2:
            st.markdown("""[**Marcin Szleszynski**](<https://github.com/martinezpl>)""")
            st.image("images/Marcin.png",use_column_width=True)
            #st.markdown("[**Mask Guard**](<https://github.com/Tobias-GH-Schulz/mask-detector>)")
            #st.image("images/logo_symbol.png",use_column_width=True)

def features():
    col1, col2 = st.beta_columns([1, 2])
    st.markdown("<h1 style='text-align: left; color: black;'>Features</h1>", unsafe_allow_html=True)
    bgcolor = "#ffffff"
    fontcolor = "#ff0000"
    html_line = """
    <hr style="height:1px;border-width:0;color:{};background-color:{}">
    """
    st.markdown(html_line.format(bgcolor,fontcolor),unsafe_allow_html=True)
    sceme = Image.open("images/Mask_detector_sceme.png")
    st.image(sceme)

    st.markdown("<h2 style='text-align: left; color: black;'>1. Image optimizer</h2>", unsafe_allow_html=True)
    with st.beta_expander("Read about it:"):
        st.write("TEST")

    st.markdown("<h2 style='text-align: left; color: black;'>2. Motion Detector</h2>", unsafe_allow_html=True)
    with st.beta_expander("Read about it:"):
        st.write("TEST")

def app_video_upload():
    """ User video upload """
    webrtc_streamer(
        key="loopback",
        mode=WebRtcMode.SENDRECV,
        client_settings=WEBRTC_CLIENT_SETTINGS,
        video_transformer_factory=None,  # NoOp
    )


def app_mask_detection():
    """ Video transforms with OpenCV """

    class OpenCVVideoTransformer(VideoTransformerBase):
        #type: Literal("bla", "bla")
        def __init__(self) -> None:
            self.face_detector = FaceDetector(FACE_PROTO, FACE_MODEL)
            self.body_detector = BodyDetector(BODY_PROTO, BODY_MODEL)
            self.face_mask_classifier = FaceMaskClassifier(MASK_MODEL)

            self.DIST_REF = 22
            self.FOCAL = int((309 *  100) / self.DIST_REF)
            self.dist = Distance(self.FOCAL, self.DIST_REF)

        def __cropout(self, img, box):
            return img[box[1]:box[3], box[0]:box[2]]

        def transform(self, frame: av.VideoFrame) -> av.VideoFrame:
            img = frame.to_ndarray(format="bgr24") ## PIL ?
            
            annotater = Annotater(img)
            #frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            frame = img
            face_crops = []
            face_boxes, _ = self.face_detector.detect(frame, FACE_CONFID_THRESH)
            if len(face_boxes):
                annotater.faces += face_boxes
                face_crops = [self.__cropout(frame, face_box) for face_box in face_boxes]
            else:
                body_boxes, _ = self.body_detector.detect(frame, BODY_CONFID_THRESH)
                if len(body_boxes) != 0:
                    annotater.bodies += body_boxes
                    body_crops = [self.__cropout(frame, body_box) for body_box in body_boxes]
                    for body_crop, body_box in zip(body_crops, body_boxes):
                        face_box, _ = self.face_detector.detect(body_crop, FACE_CONFID_THRESH, single=True)
                        if len(face_box) > 0:
                            face_crops.append(self.__cropout(body_crop, face_box))
                            annotater.faces.append(annotater.recalc(face_box, body_box))

            if len(face_crops) != 0:
                for face_crop in face_crops:
                    annotater.mask_statuses.append(self.face_mask_classifier.predict(cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)))

                annotater.dist_measure.append(self.dist.measure(annotater.faces))
                frame = annotater.update()
            
            return frame 
            
    webrtc_ctx = webrtc_streamer(
        key="opencv-filter",
        mode=WebRtcMode.SENDRECV,
        client_settings=WEBRTC_CLIENT_SETTINGS,
        video_transformer_factory=OpenCVVideoTransformer,
        async_transform=True,
    )

    #transform_type = st.radio(
    #    "Select transform type", ("noop", "cartoon", "edges", "rotate")
    #)
    #if webrtc_ctx.video_transformer:
    #    webrtc_ctx.video_transformer.type = transform_type

if __name__ == "__main__":
    logging.basicConfig(
        format="[%(asctime)s] %(levelname)7s from %(name)s in %(filename)s:%(lineno)d: "
        "%(message)s",
        force=True,
    )

    logger.setLevel(level=logging.DEBUG)

    st_webrtc_logger = logging.getLogger("streamlit_webrtc")
    st_webrtc_logger.setLevel(logging.DEBUG)

    main()
