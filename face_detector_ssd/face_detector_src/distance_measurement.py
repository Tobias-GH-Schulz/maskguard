# import the necessary packages
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import torch

def get_distance(coordinates):
    # Focal length
    F = 290
    # initialize dict for object positions
    pos_dict = dict()

    print("Coordinates in distance: ", coordinates)

    for i in range(0, len(coordinates)):
        (startX, startY, endX, endY) = coordinates[i]
        
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

    return pos_dict, close_objects