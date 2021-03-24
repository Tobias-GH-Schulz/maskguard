import numpy as np
import cv2

personModel = "../face_detector_model/person_model/res10_300x300_ssd_iter_140000.caffemodel"
prersonProto = "../face_detector_model/person_model/deploy.prototxt"

personNet=cv2.dnn.readNet(personModel,personProto)


def person_detector(image):
    person_boxes = dict()
    confidence = dict()
    person_class = 15

    # extract the original dimensions
    (h,w) = image.shape[:2]
    # Resize image to 300x300 and 
    # convert image into blobFromImage
    # blobImage convert RGB (104.0, 177.0, 123.0)
    blob = cv2.dnn.blobFromImage(cv2.resize(
                                image,(300,300)),
                                1.0,(300,300),
                                (104.0, 177.0, 123.0))

    # passing blob through the network to detect and predict
    net.setInput(blob)
    detections = net.forward()    

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence and prediction
        confid_all = detections[0, 0, i, :]

        # filter detections by confidence greater than the minimum
        if confid_all < 0.5:
            continue
        
        # Save confidence and coordinates for each detected face
        confidence[i] = confid_all

        	  k = detections.shape[2]
    	  obj_data = []
    	  for i in np.arange(0, k):
            obj = detections[0, 0, i, :]
            obj_data.append(obj)