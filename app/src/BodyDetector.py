import numpy as np
import cv2

class BodyModelLoader:	
    @staticmethod
    def load(bodyProto, bodyModel):
        net = cv2.dnn.readNetFromCaffe(bodyProto, bodyModel)
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

class BodyDetector:
    def __init__(self, bodyProto, bodyModel):
        self.proc = FrameProcessor()
        self.bodyNet = BodyModelLoader.load(bodyProto, bodyModel)
        self.class_num = 15

    def detect(self, frame, confidThresh):
        (self.h, self.w) = frame.shape[:2]
        blob = self.proc.get_blob(frame)
        self.bodyNet.setInput(blob)
        detections = self.bodyNet.forward()
        # loop over the detections
        body_boxes = []
        confidence = []
        for i in range(0, detections.shape[2]):
            # extract the confidence and prediction
            confid_all = detections[0, 0, i, 2]
            class_all = detections[0, 0, i, 1]
            # filter detections by confidence greater than the minimum
            if class_all == self.class_num and confid_all>=confidThresh:
                # compute the (x, y)-coordinates of the bounding box for the
                # object
                box = detections[0, 0, i, 3:7] * np.array([self.w, 
                                                            self.h, 
                                                            self.w, 
                                                            self.h])
                (startX, startY, endX, endY) = box.astype("int")
                startX = max(0, startX - 15)
                startY = max(0, startY - 15)
                endX = min(self.w, endX + 15)
                endY = min(self.h, endX + 15)

                confidence.append(confid_all)
                body_boxes.append((startX, startY, endX, endY))
            else:
                break

        if len(body_boxes) > 1:
            body_boxes = tuple(body_boxes)
            confidence = tuple(confidence)

        return body_boxes, confidence
