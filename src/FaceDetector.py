import numpy as np
import cv2

class FaceModelLoader:
    @staticmethod
    def load(faceProto, faceModel):
        net = cv2.dnn.readNetFromCaffe(faceProto, faceModel)
        return net


class FrameProcessor:
    def __init__(self):
        self.size = 300
        self.scale = 1.0
        self.mean = (104.0, 177.0, 123.0)

    def get_blob(self, frame):
        img = frame
        (h, w) = frame.shape[:2]

        resized = cv2.resize(img, (self.size, self.size), cv2.INTER_AREA)
        blob = cv2.dnn.blobFromImage(resized, self.scale,
                                     (self.size, self.size),
                                     self.mean)
        return blob


class FaceDetector:
    def __init__(self, faceProto, faceModel):
        self.proc = FrameProcessor()
        self.net = FaceModelLoader.load(faceProto, faceModel)

    def detect(self, frame, confidThresh, single = False):
        (self.h, self.w) = frame.shape[:2]
        blob = self.proc.get_blob(frame)
        self.net.setInput(blob)
        detections = self.net.forward()
        # loop over the detections
        face_boxes = []
        confidence = []
        for i in range(0, detections.shape[2]):
            # extract the confidence and prediction
            confid = detections[0, 0, i, 2]
            # filter detections by confidence greater than the minimum
            if confid < confidThresh:
                break
            # compute the (x, y)-coordinates of the bounding box for the
            # object
            box = detections[0, 0, i, 3:7] * np.array([self.w,
                                                       self.h,
                                                       self.w,
                                                       self.h])
            (startX, startY, endX, endY) = box.astype("int")
            startX = max(0, startX - 35)
            startY = max(0, startY - 35)
            endX += 35
            endY += 35
            if single:
               return (startX, startY, endX, endY), confid
            confidence.append(confid)
            face_boxes.append((startX, startY, endX, endY))

        if len(face_boxes) > 1:
            face_boxes = tuple(face_boxes)
            confidence = tuple(confidence)
        return face_boxes, confidence

