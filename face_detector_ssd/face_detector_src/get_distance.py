import numpy as np
import cv2

class Distance:
    def __init__(self, focal, distRef):
        self.focal = focal
        self.distRef = distRef 
        
    def measure(self, face_boxes):
        # initialize dict for object positions
        pos_dict = dict()
        
        for i in range(0, len(face_boxes)):
            (startX, startY, endX, endY) = face_boxes[i]
            startX += 15
            startY += 15
            endX -= 15
            endY -= 15

            # Mid point of bounding box
            x_mid = round((startX+endX)/2,4)
            y_mid = round((startY+endY)/2,4)

            height = round(endY-startY,4)

            # Distance from camera based on triangle similarity
            distance = (self.distRef * self.focal)/height

            # Mid-point of bounding boxes (in cm) based 
            # on triangle similarity technique
            x_mid_cm = (x_mid * distance) / self.focal
            y_mid_cm = (y_mid * distance) / self.focal
            pos_dict[i] = (x_mid_cm,y_mid_cm,distance)

        if pos_dict is not None:
            # Distance between every object detected in a frame
            close_objects = set()
            for i in pos_dict.keys():
                for j in pos_dict.keys():
                    if i < j:
                        dist = np.sqrt(pow(pos_dict[i][0]-pos_dict[j][0],2) + 
                        pow(pos_dict[i][1]-pos_dict[j][1],2) + 
                        pow(pos_dict[i][2]-pos_dict[j][2],2))

                        # Check if distance less than 1 
                        # metres or 100 centimetres
                        if dist < 100:
                            close_objects.add(i)
                            close_objects.add(j)

        return pos_dict, close_objects

