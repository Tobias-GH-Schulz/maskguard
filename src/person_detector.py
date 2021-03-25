# import the necessary packages
import numpy as np
import cv2

class CaffeModelLoader:	
    @staticmethod
    def load():
        personModel = "../face_detector_model/person_model/mobilenet.caffemodel"
        personProto = "../face_detector_model/person_model/mobilenet.prototxt"
        net = cv2.dnn.readNetFromCaffe(personProto, personModel)
        return net
 
class FrameProcessor:	
    def __init__(self, size, scale, mean):
    	self.size = size
    	self.scale = scale
    	self.mean = mean
	
    def get_blob(self, frame):
        img = frame
        (h, w, c) = frame.shape
        
        resized = cv2.resize(img, (self.size, self.size), cv2.INTER_AREA)
        blob = cv2.dnn.blobFromImage(resized, self.scale,
                                    (self.size, self.size),
                                    self.mean)
        return blob

class SSD:	
    def __init__(self, frame_proc, ssd_net):
        self.proc = frame_proc
        self.net = ssd_net
	
    def detect(self, frame):
        blob = self.proc.get_blob(frame)
        self.net.setInput(blob)
        detections = self.net.forward()
        # detected object count
        k = detections.shape[2]
        obj_data = []
        for i in np.arange(0, k):
            obj = detections[0, 0, i, :]
            obj_data.append(obj)
        return obj_data

    def get_objects(self, frame, obj_data, class_num, min_confidence):
        objects = []
        for (i, data) in enumerate(obj_data):
            obj_class = int(data[1])
            obj_confidence = data[2]
            if obj_class==class_num and obj_confidence>=min_confidence:
                obj = self.get_object(frame, data)
                objects.append(obj)
                
        return objects
 
    def get_object(self, frame, data):
        confidence = int(data[2]*100.0)
        (h, w, c) = frame.shape
        r_x = int(data[3]*h)
        r_y = int(data[4]*h)
        r_w = int((data[5]-data[3])*h)
        r_h = int((data[6]-data[4])*h)
        
        obj_rect = (r_x, r_y, r_w, r_h)
        
        return (confidence, obj_rect)


class Utils:	
    @staticmethod
    def draw_object(obj, label, color, frame):
        (confidence, (x1, y1, w, h)) =  obj
        x2 = x1+w
        y2 = y1+h
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        y3 = y1-12
        text = label + " " + str(confidence)+"%"
        cv2.putText(frame, text, (x1, y3), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 1, cv2.LINE_AA)
    	
    @staticmethod
    def draw_objects(objects, label, color, frame):
        for (i, obj) in enumerate(objects):
            Utils.draw_object(obj, label, color, frame)
