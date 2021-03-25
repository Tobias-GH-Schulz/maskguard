import cv2
import numpy as np
import imutils
import time

class Background:
    @staticmethod
    def capture(capture_duration):        
        # Open the camera
        video = cv2.VideoCapture(0)
        time.sleep(2.0)
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
