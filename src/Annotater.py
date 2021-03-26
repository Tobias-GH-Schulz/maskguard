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

    def recalc(self, box, ref):
        '''
        ADJUST box TO self.image ACCORDING TO ref
        Ie. used for faces that were detected in a body box, not in main frame.

        box(array) - coordinates to be adjusted
        ref(array) - reference coordinates
        '''
        x = ref[0] + box[0]
        y = ref[1] + box[1]
        x2 = x + box[2]
        y2 = y + box[3]
        return (x, y, x2, y2)

    def update(self):
        for face in self.faces:
            a = cv2.rectangle(self.annotated, face[:2], face[2:], [255,0,0], 3)
        for body in self.bodies:
            a = cv2.rectangle(self.annotated, body[:2], body[2:], [0,255,0], 3)

        for ix, status in enumerate(self.mask_statuses):
            a = cv2.putText(self.annotated, status, self.faces[ix][:2], cv2.FONT_HERSHEY_SIMPLEX,
                        1, [0, 0, 255], 3, cv2.LINE_AA)

        self.annotated = a
        return self.annotated