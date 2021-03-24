# mask-detector

__PersonDetector(pd_model_path)__ 
```
def detect(image):
  
  slices = (slice(detected_box) for detected_box in detected_boxes)
  
  return slices(tuple)
```

__FaceDetector(fd_model_path)__
```
def detect(image):
  
  slices = (slice(detected_box) for detected_box in detected_boxes)
  
  return slices(tuple)
```
  
__AgeGenderClassifier(agd_model_path)__  << probably should be two classifiers
```
def predict(image):
  
  return age(string), gender(string)
```

__FaceMaskClassifier(fmc_model_path)__
```
def predict(image):
  
  return mask_state(string)
```
__Annotater(image)__
```
def __init__(image):
  self.image = image
  self.annotated = None
  self.faces = []
  self.bodies = []
  self.ages = []
  self.genders = []
  self.mask_statuses = []

def adjust(self, box, ref):
  
  '''
  ADJUST box TO self.image ACCORDING TO ref
  Ie. used for faces that were detected in a body box, not in main frame.
  
  box(array) - coordinates to be adjusted
  ref(array) - reference coordinates 
  '''
  
  return slice()
  
def update(self):
  '''
  ANNOTATE EVERYTHING ON self.image
  '''
  self.annotated = annotated
  return annotated
 ``` 
### PSEUDO - CODE for __main__.py 

```
person_detector = PersonDetector(pd_model_path)
face_detector = FaceDetector(fd_model_path)
age_gender_detector = AgeGenderDetector(agd_model_path)
face_mask_classifier = FaceMaskClassifier(fmc_model_path)

for frame in video:
  annotater = Annotater(frame)

  face_boxes_f = face_detector.detect(frame)
  face_crops = [frame[face_box_f] for face_box_f in face_boxes_f]
  annotater.faces += face_boxes_f

  if face_boxes.empty():
    body_boxes = person_detector.detect(frame)
    annotater.bodies += body_boxes
    if body_boxes.empty():
      return

    body_crops = [frame[body_box] for body_box in body_boxes]

    face_boxes_b = [face_detector(body_crop) for body_crop in body_crops]
    face_crops = [body_crop[face_box] for body_crop, face_box in zip(body_crops, face_boxes_b)]
    for face_box_b, body_box in zip(face_boxes_b, body_boxes):
      annotater.faces += annotater.adjust(face_box_b, body_box)

  for face_crop in face_crops:
    age, gender = age_gender_detector.predict(face_crop)
    mask_status = face_mask_classifier.predict(face_crop)
    annotater.ages.append(age) 
    annotater.genders.append(gender)
    annotater.mask_statuses.append(mask_status)
 
  annotated_frame = annotater.update()
  imshow(annotated_frame)
```
