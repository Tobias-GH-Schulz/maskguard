import cv2
import numpy as np        
        
def annotate_heads(frame, face_boxes, confidence):
    frame_copy = frame.copy()
    for i in range(0, len(confidence)):
        (startX, startY, endX, endY) = face_boxes[i]
        if (np.array([startX, startY, endX, endY])>0).all():
            print('Coordinates in annotate heads:', (startX, startY, endX, endY))
            text = "{:.2f}%".format(confidence[i] * 100)
            y = endY + 20 if endY + 20 > 10 else endY - 10
            cv2.rectangle(frame, (startX, startY), (endX, endY),
                            (0, 0, 255), 2)
            cv2.putText(frame, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1)
            return frame
        else:
            return frame_copy
        
def annotate_distance(frame, face_boxes, pos_dict, close_objects):        
    frame_copy = frame.copy()
    for i in pos_dict.keys():
        if i in close_objects:
            COLOR = [0,0,255]
        else:
            COLOR = [0,255,0]
        (startX, startY, endX, endY) = face_boxes[i]
        if (np.array([startX, startY, endX, endY])>0).all():
            print('Coordinates in annotate distance:', (startX, startY, endX, endY))
            cv2.rectangle(frame, (startX, startY), (endX, endY), COLOR, 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            # Convert cms to feet

            cv2.putText(frame, 'Dist. to cam: {i} cm'.format(i=round(pos_dict[i][2],4)), (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR, 1)
            return frame
        else:
            return frame_copy

def annotate_age_gender(frame, face_boxes, age, gender):
    frame_copy = frame.copy()
    for i in range(0, len(face_boxes)):
        (startX, startY, endX, endY) = face_boxes[i]
        if (np.array([startX, startY, endX, endY])>0).all():
            print('Coordinates in annotate age:', (startX, startY, endX, endY))
            text = f"{gender[i]}, {age[i]}"
            y = startY - 35 if startY - 35 > 10 else startY + 35
            cv2.putText(frame, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
            return frame
        else:
            return frame_copy
        