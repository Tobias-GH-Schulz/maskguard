import cv2
import numpy as np 

class BrightnessOptimizer:
    def optimize(self, frame):
        self.frame = frame
        self.frame_copy = frame

        hsv = cv2.cvtColor(self.frame_copy, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        if np.mean(v) > 120:
            return self.frame
        
        elif np.mean(v) > 100:
            alpha = 2
            beta = 10

        elif np.mean(v) > 80:
            alpha = 2
            beta = 20

        elif np.mean(v) > 60:
            alpha = 2
            beta = 30

        else:
            alpha = 2
            beta = 70
        
        new_image = cv2.addWeighted(self.frame, alpha, np.zeros(self.frame.shape, 
                                    self.frame.dtype), 0, beta)
        return new_image
    
        