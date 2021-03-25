# mask-detector assembly plan


### PSEUDO - CODE for __main__.py 

```python
person_detector = PersonDetector(pd_model_path)
face_detector = FaceDetector(fd_model_path)
age_gender_detector = AgeGenderDetector(agd_model_path)
face_mask_classifier = FaceMaskClassifier(fmc_model_path)

for frame in video:
  annotater = Annotater(frame)

  # detect() returns tuple of indices of type slice(), indices indicate how to slice the input image to crop the detected object
  face_boxes = face_detector.detect(frame) 
  annotater.faces += face_boxes # look below this snippet to see Annotater() fields
  face_crops = [frame[face_box] for face_box in face_boxes]
  
  # let's try to find bodies
  body_boxes = person_detector.detect(frame)
  if body_boxes.empty() and face_boxes.empty():
    # found nothing - continue to the next frame

  annotater.bodies += body_boxes

  # crop out the bodies
  body_crops = [frame[body_box] for body_box in body_boxes]

  # try to detect faces in the cropped bodies
  face_boxes = [face_detector(crop) for crop in body_crops]
  face_crops += [crop[face_box] for crop, face_box in zip(body_crops, face_boxes)]
  for face_box, body_box in zip(face_boxes, body_boxes):
    annotater.faces += annotater.adjust(face_box, body_box) # adjusting indices to frame, see adjust() method

  
  for face_crop in face_crops:
    age, gender = age_gender_detector.predict(face_crop)
    mask_status = face_mask_classifier.predict(face_crop)
    annotater.ages.append(age) 
    annotater.genders.append(gender)
    annotater.mask_statuses.append(mask_status)
 
  annotated_frame = annotater.update()
  imshow(annotated_frame)
```


__PersonDetector(pd_model_path)__ 
```
def detect(image):
  
  slices = (slice(detected_box) for detected_box in detected_boxes)
  
  return (tuple)slices
```

__FaceDetector(fd_model_path)__
```
def detect(image):
  
  slices = (slice(detected_box) for detected_box in detected_boxes)
  
  return (tuple)slices
```
  
__AgeGenderClassifier(agd_model_path)__  << probably should be two classifiers
```
def predict(image):
  
  return (string)age, (string)gender
```

__FaceMaskClassifier(fmc_model_path)__
```
def predict(image):
  
  return (string)mask_state
```
__Annotater(image)__
```python
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
