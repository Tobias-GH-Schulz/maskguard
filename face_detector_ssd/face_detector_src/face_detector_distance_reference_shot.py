# import the necessary packages
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2

#defining prototext and caffemodel paths
caffeModel = "/Users/tobiasschulz/Documents/GitHub/mask-detector/face_detector_ssd/face_detector_model/res10_300x300_ssd_iter_140000.caffemodel"
prototextPath = "/Users/tobiasschulz/Documents/GitHub/mask-detector/face_detector_ssd/face_detector_model/deploy.prototxt"

#Load Model
print("Loading model...................")
net = cv2.dnn.readNetFromCaffe(prototextPath,caffeModel)

frame_no = 0

# initialize the video stream to get the live video frames
print("[INFO] starting video stream...")
video = cv2.VideoCapture(0)
time.sleep(2.0)

while(video.isOpened()):
    check, frame = video.read()
    if frame is not None:
        while frame_no < 2:
            frame_no += 1

            #Get the frams from the video stream and resize to 400 px
            frame = imutils.resize(frame,width=400)

            # extract the dimensions , Resize image into 300x300 and converting image into blobFromImage
            (h, w) = frame.shape[:2]
            # blobImage convert RGB (104.0, 177.0, 123.0)
            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                        (300, 300), (104.0, 177.0, 123.0))
            

            # passing blob through the network to detect and pridiction
            net.setInput(blob)
            detections = net.forward()

            pos_dict = dict()
            coordinates = dict()

            # Focal length
            F = 615

            for i in range(0, detections.shape[2]):
                # extract the confidence and prediction

                confidence = detections[0, 0, i, 2]

                # filter detections by confidence greater than the minimum confidence
                if confidence < 0.5 :
                    continue

                # Determine the (x, y)-coordinates of the bounding box for the
                # object
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # draw the bounding box of the face along with the associated
                text = "{:.2f}%".format(confidence * 100)
                y = endY + 20 if endY + 20 > 10 else endY - 10
                cv2.rectangle(frame, (startX, startY), (endX, endY),
                                (0, 0, 255), 2)
                cv2.putText(frame, text, (startX, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

                cv2.imwrite("/Users/tobiasschulz/Documents/GitHub/mask-detector/face_detector_ssd/test_image/reference.jpg", frame)

        # show the output frame
        cv2.imshow("Frame", frame)
        cv2.resizeWindow('Frame',800,800)

        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
    else:
        break

# do a bit of cleanup
video.release()
cv2.destroyAllWindows()
cv2.waitKey(1)