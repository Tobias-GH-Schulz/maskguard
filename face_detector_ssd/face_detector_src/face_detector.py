# import the necessary packages
import numpy as np
import argparse
import cv2

# defining prototext and caffemodel paths
caffeModel = "/Users/tobiasschulz/Documents/GitHub/mask-detector/face_detector_model/res10_300x300_ssd_iter_140000.caffemodel"
prototextPath = "/Users/tobiasschulz/Documents/GitHub/mask-detector/face_detector_model/deploy.prototxt"

# Load Model
print("Loading model...................")
net = cv2.dnn.readNetFromCaffe(prototextPath,caffeModel)

def face_detector(image):

    # extract the dimensions , Resize image into 300x300 and converting image into blobFromImage
    (h,w) = image.shape[:2]
    # blobImage convert RGB (104.0, 177.0, 123.0)
    blob = cv2.dnn.blobFromImage(cv2.resize(image,(300,300)),1.0,(300,300),(104.0, 177.0, 123.0))

    # passing blob through the network to detect and pridiction
    net.setInput(blob)
    detections = net.forward()

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence and prediction
        confidence = detections[0, 0, i, 2]

        # filter detections by confidence greater than the minimum     #confidence
        print(confidence)
        if confidence > 0.5:
            # compute the (x, y)-coordinates of the bounding box for the
            # object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # draw the bounding box of the face along Confidance
            # probability
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(image, (startX, startY), (endX, endY),
                        (0, 0, 255), 2)
            cv2.putText(image, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

