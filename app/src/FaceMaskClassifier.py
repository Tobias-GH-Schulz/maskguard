import torch
from torchvision import transforms
from skimage import io
import numpy as np
from PIL import Image

class FaceMaskClassifier():
    def __init__(self, model_path, transformations = None, device='cpu'):
        self.model = torch.load(model_path, map_location=device)
        self.labels = ['mask', 'no_mask']

        if transformations:
            self.transformations = transformations
        else:
            self.transformations = transforms.Compose([
                transforms.Resize((300,300)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ])

    def __preprocess(self, img):
        if not isinstance(img, Image.Image):
            input_image = Image.fromarray(img)

        input_tensor = self.transformations(input_image)
        input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model
        return input_batch

    def predict(self, face_image):
        processed_img = self.__preprocess(face_image)
        with torch.no_grad():
            output = self.model(processed_img)
        # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        _, pred = torch.max(output, 1)
        return self.labels[pred]

if __name__ == "__main__":
    model_path = "models/mnv2_mask_classifier_v2.pth"
    classifier = FaceMaskClassifier(model_path)
    img = io.imread('../training/dataset_cropped/imgs_2class/mask/kim_1616409549.jpg')
    classifier.predict(img)
    print('All good in the hood!')
