import logging
import logging.handlers
import queue
import urllib.request
from pathlib import Path
import tempfile
import base64
#from typing import List, NamedTuple

#try:
#    from typing import Literal
#except ImportError:
#    from typing_extensions import Literal  # type: ignore

import av
import cv2
import numpy as np
import streamlit as st
from streamlit_player import st_player
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
from src.StreamlitDesign import StreamlitDesign

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
    StreamlitDesign().content()
    StreamlitDesign().features()

    play_demo_video = (
        "Play demo video"
        )
    mask_detection_page = (
        "Real time demo"
    )
    video_upload_page = "Upload a video"
    st.markdown("<h1 style='text-align: left; color: black;'>Here you can choose between different app modes:</h1>", unsafe_allow_html=True)
    app_mode = st.selectbox(
        " ",
        [
            play_demo_video,
            mask_detection_page,
            video_upload_page,
        ],
    )

    StreamlitDesign().sidebar()

    if app_mode == mask_detection_page:
        st.markdown("<h4 style='text-align: center; color: black;'>DISCLAIMER: Distance measurement will not be displayed 100% correctly during demo due to lack of camera calibration. Audio alarm system is not active during live demo.</h4>", unsafe_allow_html=True)
        bgcolor = "#ff0000"
        fontcolor = "#000000"
        html_temp = """<div style="background-color:{};padding:10px"> 
                        <h2 style="color:{};text-align:center;">Try it out with your camera!</h2> 
                        </div>"""
        st.markdown(html_temp.format(bgcolor,fontcolor),unsafe_allow_html=True)
        app_mask_detection()
    elif app_mode == play_demo_video:
        st_player("https://youtu.be/dHb1PDF_VMM")
    elif app_mode == video_upload_page:
        app_video_upload()

    st.write(" ")
    st.write(" ")
    
    StreamlitDesign().timeline()
    StreamlitDesign().end()


def app_video_upload():
    """ User video upload """
    # TODO: delete existing mask_guard.avi
    legal_extensions = ["avi", "mp4"]
    uploaded_file = st.file_uploader(f"Upload a video. Mind that, the longer the video, the longer the processing time.", ["avi", "mp4"]) 
    if uploaded_file:
        st.write("Processing the video. It may take a few minutes.")
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        video = cv2.VideoCapture(tfile.name)
        assembly = ModelAssembly()
        # FOR RECORDING
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
        size = (width, height)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('mask_guard.avi', fourcc, 20.0, size)
        rval, frame = video.read()
        while rval:
            rval, frame = video.read()
            processed_frame = assembly.forwardFrame(frame)
            out.write(processed_frame)
        bin_file = 'mask_guard.avi' 
        with open(bin_file, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download video</a>' 
        
        st.markdown(href, unsafe_allow_html=True)

           
    def create_player():
        try:
            return MediaPlayer("mask_guard.avi")
        except:
            pass

    webrtc_streamer(
        key="media",
        mode=WebRtcMode.RECVONLY,
        client_settings=WEBRTC_CLIENT_SETTINGS,
        player_factory=create_player,
    )  
    
class ModelAssembly():
    def __init__(self) -> None:
        self.face_detector = FaceDetector(FACE_PROTO, FACE_MODEL)
        self.body_detector = BodyDetector(BODY_PROTO, BODY_MODEL)
        self.face_mask_classifier = FaceMaskClassifier(MASK_MODEL)

        self.DIST_REF = 22
        self.FOCAL = int((309 *  100) / self.DIST_REF)
        self.dist = Distance(self.FOCAL, self.DIST_REF)

    def __cropout(self, img, box):
        return img[box[1]:box[3], box[0]:box[2]]

    def forwardFrame(self, frame): 
        annotater = Annotater(frame)
        face_crops = []
        face_boxes, _ = self.face_detector.detect(frame, FACE_CONFID_THRESH)
        if len(face_boxes):
            annotater.faces += face_boxes
            face_crops = [self.__cropout(frame, face_box) for face_box in face_boxes]
        else:
            body_boxes, _ = self.body_detector.detect(frame, BODY_CONFID_THRESH)
            if len(body_boxes) > 0:
                annotater.bodies += body_boxes
                body_crops = [self.__cropout(frame, body_box) for body_box in body_boxes]
                for body_crop, body_box in zip(body_crops, body_boxes):
                    face_box, _ = self.face_detector.detect(body_crop, FACE_CONFID_THRESH, single=True)
                    if len(face_box) > 0:
                        face_crops.append(self.__cropout(body_crop, face_box))
                        annotater.faces.append(annotater.recalc(face_box, body_box))

        if len(face_crops) > 0:
            for face_crop in face_crops:
                annotater.mask_statuses.append(
                        self.face_mask_classifier.predict(cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB))
                        )

            annotater.dist_measure.append(
                    self.dist.measure(annotater.faces)
                    )
            frame = annotater.update()
        
        return frame 
 


def app_mask_detection():
    """ Video transforms with OpenCV """

    class OpenCVVideoTransformer(VideoTransformerBase):
        #type: Literal("bla", "bla")
        def __init__(self) -> None:
            self.assembly = ModelAssembly()    

        def transform(self, frame: av.VideoFrame) -> av.VideoFrame:
            img = frame.to_ndarray(format="bgr24") ## PIL ?
           
            return self.assembly.forwardFrame(img)

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
