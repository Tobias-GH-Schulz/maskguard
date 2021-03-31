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
    media_stream_constraints={"video": True, "audio": True},
)


def main():
    st.header("Our product")

    mask_detection_page = (
        "Real time demo"
    )
    loopback_page = "Simple video loopback (sendrecv)"
    app_mode = st.sidebar.selectbox(
        "Choose the app mode",
        [
            mask_detection_page,
            loopback_page,
        ],
    )
    st.subheader(app_mode)

    if app_mode == mask_detection_page:
        app_mask_detection()
    elif app_mode == loopback_page:
        app_loopback()


def app_loopback():
    """ Simple video loopback """
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
