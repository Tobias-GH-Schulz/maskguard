import cv2
import math
import numpy as np

class AgeModelLoader:	
    @staticmethod
    def load(ageProto, ageModel):
        ageNet = cv2.dnn.readNetFromCaffe(ageProto, ageModel)
        return ageNet

class GenderModelLoader:	
    @staticmethod
    def load(genderProto, genderModel):
        ageNet = cv2.dnn.readNetFromCaffe(genderProto, genderModel)
        return ageNet

class FrameProcessor:	
    def __init__(self):
    	self.size = 300
    	self.scale = 1.0
    	self.mean = (78.4263377603, 87.7689143744, 114.895847746)
	
    def get_blob(self, frame):
        img = frame
        (h, w) = frame.shape[:2]
        
        resized = cv2.resize(img, (self.size, self.size), cv2.INTER_AREA)
        blob = cv2.dnn.blobFromImage(resized, self.scale,
                                    (self.size, self.size),
                                    self.mean, swapRB=False)
        return blob

class AgeGenderDetector:
    def __init__(self, ageProto, ageModel, genderProto, genderModel):
        self.proc = FrameProcessor()
        self.ageNet = AgeModelLoader.load(ageProto, ageModel)
        self.ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', 
                        '(25-32)', '(38-43)', '(48-53)', '(60-100)']
        self.genderNet = GenderModelLoader.load(genderProto, genderModel)
        self.genderList = ['Male','Female']

def detect(face):
    blob = self.proc.get_blob(frame)
    blob=cv2.dnn.blobFromImage(face, 
                                1.0, 
                                (227,227), 
                                MODEL_MEAN_VALUES, 
                                swapRB=False)
    self.genderNet.setInput(blob)
    genderPreds = self.genderNet.forward()
    gender = self.genderList[genderPreds[0].argmax()]

    self.ageNet.setInput(blob)
    agePreds = self.ageNet.forward()
    age = self.ageList[agePreds[0].argmax()]

    return age, gender 