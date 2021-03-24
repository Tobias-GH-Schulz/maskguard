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
        F = 290

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

            face = frame[startY:endY, startX:endX]

            # draw the bounding box of the face along with the associated
            text = "{:.2f}%".format(confidence * 100)
            y = endY + 20 if endY + 20 > 10 else endY - 10
            cv2.rectangle(frame, (startX, startY), (endX, endY),
                            (0, 0, 255), 2)
            cv2.putText(frame, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

            coordinates[i] = (startX, startY, endX, endY)

            # Mid point of bounding box
            x_mid = round((startX+endX)/2,4)
            y_mid = round((startY+endY)/2,4)

            height = round(endY-startY,4)

            # Distance from camera based on triangle similarity
            distance = (22 * F)/height
            print("Distance(cm):{dist}\n".format(dist=distance))

            # Mid-point of bounding boxes (in cm) based on triangle similarity technique
            x_mid_cm = (x_mid * distance) / F
            y_mid_cm = (y_mid * distance) / F
            pos_dict[i] = (x_mid_cm,y_mid_cm,distance)

        # Distance between every object detected in a frame
        close_objects = set()
        for i in pos_dict.keys():
            for j in pos_dict.keys():
                if i < j:
                    dist = np.sqrt(pow(pos_dict[i][0]-pos_dict[j][0],2) + pow(pos_dict[i][1]-pos_dict[j][1],2) + pow(pos_dict[i][2]-pos_dict[j][2],2))

                    # Check if distance less than 1 metres or 100 centimetres
                    if dist < 100:
                        close_objects.add(i)
                        close_objects.add(j)
                    
        for i in pos_dict.keys():
            if i in close_objects:
                COLOR = [0,0,255]
            else:
                COLOR = [0,255,0]
            (startX, startY, endX, endY) = coordinates[i]

            cv2.rectangle(frame, (startX, startY), (endX, endY), COLOR, 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            # Convert cms to feet
            cv2.putText(frame, 'Dist. to cam: {i} cm'.format(i=round(pos_dict[i][2],4)), (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR, 2)




        # show the output frame
        cv2.imshow("Frame", frame)
        cv2.imshow("Face", face)
        cv2.resizeWindow('Frame',800,800)
        cv2.resizeWindow('Face',800,800)
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