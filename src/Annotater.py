import cv2

class Annotater():
    def __init__(self, image):
        self.image = image
        self.annotated = image.copy()
        self.faces = []
        self.bodies = []
        self.ages = []
        self.genders = []
        self.mask_statuses = []
        self.dist_measure = []

    def recalc(self, box, ref):
        '''
        ADJUST box TO self.image ACCORDING TO ref
        Ie. used for faces that were detected in a body box, not in main frame.

        box(array) - coordinates to be adjusted
        ref(array) - reference coordinates
        '''
        x = ref[0] + box[0]
        y = ref[1] + box[1]
        x2 = x + box[3]
        y2 = y + box[3]
        return (x, y, x2, y2)

    def update(self):
        pos_dic, close_objects = self.dist_measure[0]
        print(pos_dic)
        for index, face in enumerate(self.faces):
            if index in close_objects:
                COLOR = [0,0,255]
            else:
                COLOR = [0,255,0]
            y = face[1] - 27 if face[1] - 27 > 15 else face[3] + 27
            # Convert cms to feet
            a = cv2.putText(self.annotated, 'Dist. to cam: {i} cm'.format(
                                    i=round(pos_dic[index][2],2)), (face[0], y),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, COLOR, 2)
            a = cv2.rectangle(self.annotated, face[:2], face[2:], COLOR, 3)

        for body in self.bodies:
            a = cv2.rectangle(self.annotated, body[:2], body[2:], [255,0,0], 3)

        for ix, status in enumerate(self.mask_statuses):
            y = self.faces[ix][1] - 70 if self.faces[ix][1] - 70 > 15 else self.faces[ix][3] + 70
            if status == "mask":
                COLOR_MASK = [0, 255, 0]
            else:
                COLOR_MASK = [0, 0, 255]
            a = cv2.putText(self.annotated, status, (self.faces[ix][0], y), cv2.FONT_HERSHEY_SIMPLEX,
                        1.3, COLOR_MASK, 2)        
        
        self.annotated = a
        return self.annotated