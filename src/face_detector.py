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

    def detect(self, frame, confidThresh):
        (self.h, self.w) = frame.shape[:2]
        blob = self.proc.get_blob(frame)
        self.net.setInput(blob)
        detections = self.net.forward()
        # loop over the detections
        face_boxes = []
        confidence = []
        for i in range(0, detections.shape[2]):
            # extract the confidence and prediction
            confid_all = detections[0, 0, i, 2]

            # filter detections by confidence greater than the minimum
            if confid_all < confidThresh:
                continue
            # compute the (x, y)-coordinates of the bounding box for the
            # object
            box = detections[0, 0, i, 3:7] * np.array([self.w,
                                                       self.h,
                                                       self.w,
                                                       self.h])
            (startX, startY, endX, endY) = box.astype("int")
            startX = max(0, startX - 15)
            startY = max(0, startY - 15)
            endX += 15
            endY += 15

            confidence.append(confid_all)
            face_boxes.append((startX, startY, endX, endY))

        return tuple(face_boxes), tuple(confidence)