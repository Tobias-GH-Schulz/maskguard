import logging
import logging.handlers
import queue
import urllib.request
from pathlib import Path
import tempfile
import base64
import subprocess as sp
#TODO: dist calibration as type of transfer class
from typing import List, NamedTuple

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal  # type: ignore

import av
import cv2
import numpy as np
import streamlit as st
from imutils.video import FileVideoStream
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
from src.BrightnessOptimizer import BrightnessOptimizer

FACE_MODEL = "src/models/face_model/res10_300x300_ssd_iter_140000.caffemodel"
FACE_PROTO = "src/models/face_model/deploy.prototxt"
BODY_MODEL = "src/models/body_model/mobilenet.caffemodel"
BODY_PROTO = "src/models/body_model/mobilenet.prototxt"
MASK_MODEL = "src/models/mask_model/mnv2_mask_classifier_v3.pth"
FACE_CONFID_THRESH = 0.5
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

FFMPEG_BIN = "ffmpeg"

def main():
    StreamlitDesign().content() 
    StreamlitDesign().sidebar()
    StreamlitDesign().features()

    st.markdown("<h1 style='text-align: left; color: black;'>Demos</h1>", unsafe_allow_html=True)
  
    st_player("https://youtu.be/dHb1PDF_VMM")

    st.write(" ")
    st.write(" ")
    st.markdown(
            """<h2><a style='display: block; text-align: center; color: green' href="https://maskguard1.ew.r.appspot.com/">Upload a video or test it with your camera!</a></h2>
    """,
    unsafe_allow_html=True,
    )
    StreamlitDesign().timeline()
    StreamlitDesign().end()

def app_video_upload():
    """ User video upload """
    legal_extensions = ["avi", "mp4"]
    uploaded_file = st.file_uploader(f"Upload a video. Mind that, the longer the video, the longer the processing time.", ["avi", "mp4"]) 
    if uploaded_file:
        with st.spinner("Processing the video. It may take a few minutes."):
            prog = 0
            bar = st.progress(prog)
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())
            fvs = FileVideoStream(tfile.name).start()
            video_in = fvs.stream
            frame_width = int(video_in.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(video_in.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = video_in.get(cv2.CAP_PROP_FPS)
            frame_count = int(video_in.get(cv2.CAP_PROP_FRAME_COUNT))
            assembly = ModelAssembly()
            
            # See http://zulko.github.io/blog/2013/09/27/read-and-write-video-frames-in-python-using-ffmpeg/
            command = ['ffmpeg',
                       '-loglevel', 'error',
                       '-y',
                       # Input
                       '-f', 'rawvideo',
                       '-vcodec', 'rawvideo',
                       '-pix_fmt', 'bgr24',
                       '-s', str(frame_width) + 'x' + str(frame_height),
                       '-r', str(fps),
                       # Output
                       '-i', '-',
                       '-an',
                       '-vcodec', 'h264',
                       '-r', str(fps),
                       '-pix_fmt', 'rgb24',
                       "mask_guard.mp4"
                       ]
            pipe = sp.Popen(command, stdin=sp.PIPE)        
            while fvs.more():
                frame = fvs.read()
                if frame is not None:
                    processed_frame = assembly.forwardFrame(frame)
                    pipe.stdin.write(processed_frame.tobytes())
                    prog += 1
                    bar.progress(prog / frame_count)
            pipe.stdin.close()
            pipe.wait() 
            bin_file = 'mask_guard.mp4' 
            with open(bin_file, 'rb') as f:
                data = f.read()
            bin_str = base64.b64encode(data).decode()
            href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download video</a>' 
            
        st.markdown(href, unsafe_allow_html=True)
    
class ModelAssembly():
    def __init__(self) -> None:
        self.face_detector = FaceDetector(FACE_PROTO, FACE_MODEL)
        self.body_detector = BodyDetector(BODY_PROTO, BODY_MODEL)
        self.face_mask_classifier = FaceMaskClassifier(MASK_MODEL)
        self.warn = MaskWarning(cooldown=6)
        self.optimizer = BrightnessOptimizer()

        self.DIST_REF = 22
        self.FOCAL = int((309 *  100) / self.DIST_REF)
        self.dist = Distance(self.FOCAL, self.DIST_REF)

    def __cropout(self, img, box):
        return img[box[1]:box[3], box[0]:box[2]]

    def forwardFrame(self, frame, soundOn = False):
        frame = self.optimizer.optimize(frame)
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
            if soundOn:
                self.warn.probe(bool("no_mask" in annotater.mask_statuses))
       
        return frame 
 


def app_mask_detection():
    """ Video transforms with OpenCV """

    class OpenCVVideoTransformer(VideoTransformerBase):
        type: Literal["basic", "sound_warnings"]
        def __init__(self) -> None:
            self.type = "basic"
            self.assembly = ModelAssembly()    

        def transform(self, frame: av.VideoFrame) -> av.VideoFrame:
            img = frame.to_ndarray(format="bgr24") ## PIL ?
           
            return self.assembly.forwardFrame(img, soundOn = (self.type == "sound_warnings"))
# TODO: audio play, camera focal calibration
   # transformer_type = st.radio(
   #     "Select features", ("basic", "sound_warnings", "cam_calib")
   # )

    webrtc_ctx = webrtc_streamer(
        key="opencv-filter",
        mode=WebRtcMode.SENDRECV,
        client_settings=WEBRTC_CLIENT_SETTINGS,
        video_transformer_factory=OpenCVVideoTransformer,
        async_transform=True,
    )

   # if webrtc_ctx.video_transformer:
   #     webrtc_ctx.video_transformer.type = transformer_type

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
