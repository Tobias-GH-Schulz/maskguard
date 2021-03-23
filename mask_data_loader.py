### import pandas as pd
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
    ann = sample['annotations'][0]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.imshow(image)
    rect = pat.Rectangle((ann[0], ann[1]), ann[3], ann[2], fill = 0, color='g')
    plt.scatter(ann[4], ann[5])
    plt.scatter(ann[6], ann[7])
    ax.add_patch(rect)


def toTensor(sample):
    image, annotations = sample['image'], sample['annotations']

    # swap color axis because
    # numpy image: H x W x C
    # torch image: C X H X W
    image = image.transpose((2, 0, 1))
    return {'image': torch.from_numpy(image),
            'annotations': torch.from_numpy(annotations)}


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
        print(anno)
        anno = np.array([anno]).astype('float').reshape(-1, 8)
        print(anno)
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
        image, annotations = sample['image'], sample['annotations']

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

        # by default it's [annotations]
        annotations = annotations[0]
        annotations = [
            #bbox_x
            annotations[0] * new_w / w,
            #bbox_y
            annotations[1] * new_h / h,
            #bbox_width (seems like height)
            annotations[2] * new_h / h,
            #bbox_heigth (seems like width)
            annotations[3] * new_w / w,
            #kp1_x
            annotations[4] * new_w / w,
            #kp1_y
            annotations[5] * new_h / h,
            #kp2_x
            annotations[6] * new_w / w,
            #kp2_y
            annotations[7] * new_h / h
        ]
        return {'image': img, 'annotations': np.array([annotations]).astype('float').reshape(-1, 8)}

if __name__ == '__main__':
    MASK_DS = AnnotatedDataset('dataset/mask_df_merged.csv', 'dataset')
    print(len(MASK_DS))
    show_annotations(MASK_DS[324])
    x = toTensor(MASK_DS[0])
    scaler = Rescale((400, 400))
    scaled = scaler(MASK_DS[324])
    show_annotations(scaled)