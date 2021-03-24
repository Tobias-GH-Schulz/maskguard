import cv2
import numpy as np        

def annotate_persons(persons_frame, persons_boxes, confidence):
    persons_frame_copy = persons_frame.copy()
    if persons_boxes and confidence is not None:
        for i in range(0, len(confidence)):
            (startX, startY, endX, endY) = persons_boxes[i]
            text = "{:.2f}%".format(confidence[i] * 100)
            y = endY + 20 if endY + 20 > 10 else endY - 10
            cv2.rectangle(persons_frame, (startX, startY), (endX, endY),
                            (0, 0, 255), 2)
            cv2.putText(persons_frame, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1)
        return persons_frame
    else:
        return persons_frame_copy

def annotate_heads(heads_frame, face_boxes, confidence):
    heads_frame_copy = heads_frame.copy()
    if face_boxes and confidence is not None:
        for i in range(0, len(confidence)):
            (startX, startY, endX, endY) = face_boxes[i]
            text = "{:.2f}%".format(confidence[i] * 100)
            y = endY + 20 if endY + 20 > 10 else endY - 10
            cv2.rectangle(heads_frame, (startX, startY), (endX, endY),
                            (0, 0, 255), 2)
            cv2.putText(heads_frame, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1)
        return heads_frame
    else:
        return heads_frame_copy
        
def annotate_distance(dist_frame, face_boxes, pos_dict, close_objects):        
    dist_frame_copy = dist_frame.copy()
    if face_boxes and pos_dict is not None:
        for i in pos_dict.keys():
            if i in close_objects:
                COLOR = [0,0,255]
            else:
                COLOR = [0,255,0]
            (startX, startY, endX, endY) = face_boxes[i]
            cv2.rectangle(dist_frame, (startX, startY), (endX, endY), COLOR, 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            # Convert cms to feet
            cv2.putText(dist_frame, 'Dist. to cam: {i} cm'.format(i=round(pos_dict[i][2],4)), (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR, 1)
        return dist_frame
    else:
        return dist_frame_copy

def annotate_age_gender(frame, face_boxes, age, gender):
    frame_copy = frame.copy()
    if face_boxes and age and gender is not None:
        for i in range(0, len(face_boxes)):
            (startX, startY, endX, endY) = face_boxes[i]
            text = f"{gender[i]}, {age[i]}"
            y = startY - 35 if startY - 35 > 10 else startY + 35
            cv2.putText(frame, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
        return frame
    else:
        return frame_copy
        