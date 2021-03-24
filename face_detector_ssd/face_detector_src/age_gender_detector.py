import cv2
import math
import numpy as np

genderModel="../face_detector_model/gender_model/gender_net.caffemodel"
genderProto="../face_detector_model/gender_model/gender_deploy.prototxt"
ageProto="../face_detector_model/age_model/age_deploy.prototxt"
ageModel="../face_detector_model/age_model/age_net.caffemodel"
genderList=['Male','Female']
ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)

ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)

def get_age_gender(frame, face_boxes):
    gender = dict()
    age = dict()
    for i in range(0, len(face_boxes)):
        (startX, startY, endX, endY) = face_boxes[i]
        if (np.array([startX, startY, endX, endY])>0).all():
            face = frame[startY:endY, startX:endX]
            blob=cv2.dnn.blobFromImage(face, 
                                        1.0, 
                                        (227,227), 
                                        MODEL_MEAN_VALUES, 
                                        swapRB=False)
            genderNet.setInput(blob)
            genderPreds = genderNet.forward()
            gender[i] = genderList[genderPreds[0].argmax()]
            #print(f'Gender: {gender[i]}')

            ageNet.setInput(blob)
            agePreds = ageNet.forward()
            age[i] = ageList[agePreds[0].argmax()]
            #print(f'Age: {age[1:-1]} years')
        
    return age, gender 