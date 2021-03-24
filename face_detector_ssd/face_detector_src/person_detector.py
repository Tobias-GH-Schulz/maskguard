import numpy as np
import cv2

personModel = "../face_detector_model/person_model/mobilenet.caffemodel"
personProto = "../face_detector_model/person_model/mobilenet.prototxt"

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
    personNet.setInput(blob)
    detections = personNet.forward()    

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence and prediction
        confid_all = detections[0, 0, i, 2]
        obj_class = detections[0, 0, i, 1]

        if obj_class == person_class:
            continue
        # filter detections by confidence greater than the minimum
        if confid_all > 0.5:
            continue

        # compute the (x, y)-coordinates of the bounding box for the
        # object
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        print(confid_all)
        (startX, startY, endX, endY) = box.astype("int")
        startX -= 15
        startY -= 15
        endX += 15
        endY += 15
        if startX < 0:
            startX = 0
        if startY < 0:
            startY = 0
        if endX > w:
            endX = w
        if endY > h:
            endY = h

        # Save confidence and coordinates for each detected face
        confidence[i] = confid_all
        person_boxes[i] = (startX, startY, endX, endY)

    return person_boxes, confidence       
