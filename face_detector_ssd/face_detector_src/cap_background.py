import cv2
import numpy as np
import imutils
import time

class StaticBackground:
    @staticmethod
    def capture_still():
        # Opens the Video file
        video = cv2.VideoCapture(0)
        i=0
        while i < 1:
            return_value, frame = video.read()
            cv2.imwrite('stactic_back'+str(i)+'.jpg',frame)
            i += 1
        del(video)


    def capture(timer, capture_duration):                
        # Open the camera
        video = cv2.VideoCapture(0)
        time.sleep(2.0)

        while True:
            check, frame = video.read()
            cv2.imshow("CaptureBackground", frame)

            start_time = time.time()

            while(int(time.time() - start_time) < capture_duration):
                FOI = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=30)
                
                #creating an array of frames from frames chosen above
                frames = []
                for frameOI in FOI:
                    video.set(cv2.CAP_PROP_POS_FRAMES, frameOI)
                    ret, frame = video.read()
                    frame = imutils.resize(frame,width=400)
                    frames.append(frame)

                #calculate the average
                backgroundFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
                
                cv2.imshow("backgroundFrame", backgroundFrame)

                key = cv2.waitKey(1) & 0xFF

        # do a bit of cleanup
        video.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)

        return backgroundFrame
