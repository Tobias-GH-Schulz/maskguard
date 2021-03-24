import cv2
import math

genderModel="../face_detector_model/gender_net.caffemodel"
genderProto="../face_detector_model/gender_deploy.prototxt"
genderList=['Male','Female']
MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)

genderNet=cv2.dnn.readNet(genderModel,genderProto)

def get_gender(frame, face_boxes):
    gender = dict()
    for i in range(0, len(face_boxes)):
        (startX, startY, endX, endY) = face_boxes[i]
        face = frame[startY:endY, startX:endX]
        blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds=genderNet.forward()
        gender[i]=genderList[genderPreds[0].argmax()]
        print(f'Gender: {gender[i]}')
    
    return gender