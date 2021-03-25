import numpy as np
import cv2

class PersonModelLoader:	
    @staticmethod
    def load(personProto, personModel):
        net = cv2.dnn.readNetFromCaffe(personProto, personModel)
        return net

class FrameProcessor:	
    def __init__(self):
    	self.size = 300
    	self.scale = 0.007843
    	self.mean = 127
	
    def get_blob(self, frame):
        img = frame
        (h, w) = frame.shape[:2]
        
        resized = cv2.resize(img, (self.size, self.size), cv2.INTER_AREA)
        blob = cv2.dnn.blobFromImage(resized, self.scale,
                                    (self.size, self.size),
                                    self.mean)
        return blob

class PersonDetector:
    def __init__(self, personProto, personModel):
        self.proc = FrameProcessor()
        self.personNet = PersonModelLoader.load(personProto, personModel)
        self.class_num = 15

    def detect(self, frame, confidThresh):
        (self.h, self.w) = frame.shape[:2]
        blob = self.proc.get_blob(frame)
        self.personNet.setInput(blob)
        detections = self.personNet.forward()
        # loop over the detections
        person_boxes = []
        confidence = []
        for i in range(0, detections.shape[2]):
            # extract the confidence and prediction
            confid_all = detections[0, 0, i, 2]
            class_all = detections[0, 0, i, 1]
            # filter detections by confidence greater than the minimum
            if class_all == self.class_num and confid_all>=confidThresh:
            #if confid_all>=confidThresh:

                # compute the (x, y)-coordinates of the bounding box for the
                # object
                box = detections[0, 0, i, 3:7] * np.array([self.w, 
                                                            self.h, 
                                                            self.w, 
                                                            self.h])
                (startX, startY, endX, endY) = box.astype("int")
                startX -= 15
                startY -= 15
                endX += 15
                endY += 15
                startX = max(0, startX)
                startY = max(0, startY)
                endX = max(0, endX)
                endY = max(0, endY)

                confidence.append(confid_all)
                person_boxes.append((startX, startY, endX, endY))       
            
        return tuple(person_boxes), tuple(confidence)