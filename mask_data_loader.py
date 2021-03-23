import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import torch
# we'll be inheriting this and overriding __len__ and __getitem__ 
from torch.utils.data import Dataset 
import os 
from skimage import io, transform

def show_annotations(sample):
    """
    Helper function to show annotations. 
    Args:
        sample(AnnotatedDataset.__get__ output)
    """
    image = sample['image']
    ann = sample['annotations']
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.imshow(image)
    rect = pat.Rectangle((ann[0], ann[1]), ann[2], ann[3], fill = 0, color='g')
    plt.scatter(ann[4], ann[5])
    plt.scatter(ann[6], ann[7])
    ax.add_patch(rect)


def toTensor(sample):
    image, landmarks = sample['image'], sample['landmarks']

    # swap color axis because
    # numpy image: H x W x C
    # torch image: C X H X W
    image = image.transpose((2, 0, 1))
    return {'image': torch.from_numpy(image),
            'landmarks': torch.from_numpy(landmarks)}


class AnnotatedDataset(Dataset):
    
    def __init__(self, csv_file, root_dir, transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.annotations = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform
        
    def __len__(self):
        return len(self.annotations)
    
    def __getitem__(self, idx):
        if isinstance(idx, torch.Tensor):
            idx = idx.tolist()
        
        img_name = os.path.join(self.root_dir, self.annotations.iloc[idx, 0])
        image = io.imread(img_name)
        anno = self.annotations.iloc[idx, 2:] # name, class , ....
        anno = np.array([anno]).astype('float').reshape(-1, 8)
        sample = {'image': image, 'annotations': anno}
        
        if self.transform:
            sample = self.transform(sample)
        
        return sample

class Rescale(object):
    """Rescale the image in a sample to a given size.

    Args:
        output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
    """

    def __init__(self, output_size):
        assert isinstance(output_size, (int, tuple))
        self.output_size = output_size

    def __call__(self, sample):
        image, landmarks = sample['image'], sample['landmarks']

        h, w = image.shape[:2]
        if isinstance(self.output_size, int):
            if h > w:
                new_h, new_w = self.output_size * h / w, self.output_size
            else:
                new_h, new_w = self.output_size, self.output_size * w / h
        else:
            new_h, new_w = self.output_size

        new_h, new_w = int(new_h), int(new_w)

        img = transform.resize(image, (new_h, new_w))

        # h and w are swapped for landmarks because for images,
        # x and y axes are axis 1 and 0 respectively
        landmarks = landmarks * [new_w / w, new_h / h]

        return {'image': img, 'landmarks': landmarks}

if __name__ == '__main__':
    MASK_DS = AnnotatedDataset('dataset/mask_df_merged.csv', 'dataset')
    print(len(MASK_DS))
    show_annotations(MASK_DS[0])
    x = toTensor(MASK_DS[0])
    scaler = Rescale((400, 400))
    scaled = scaler(MASK_DS[0])
    scaled = toTensor(scaled)
    show_annotations(scaled)