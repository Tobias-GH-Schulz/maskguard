import cv2
import numpy as np
import imutils
import time
from imutils.video import VideoStream
from face_detector import face_detector


frame_no = 0

# initialize the video stream to get the live video frames
print("[INFO] starting video stream...")
video = cv2.VideoCapture(0)
time.sleep(2.0)

while(video.isOpened()):
    check, frame = video.read()
    if frame is not None:
        frame_no += 1

        #Get the frame from the video stream and resize to 400 px
        frame = imutils.resize(frame,width=400)

        coordinates, confidence = face_detector(frame)




        # just for checking -> will be in extra module
        for i in range(0, len(confidence)):
            (startX, startY, endX, endY) = coordinates[i]
            text = "{:.2f}%".format(confidence[i] * 100)
            y = endY + 20 if endY + 20 > 10 else endY - 10
            cv2.rectangle(frame, (startX, startY), (endX, endY),
                            (0, 0, 255), 2)
            cv2.putText(frame, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

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