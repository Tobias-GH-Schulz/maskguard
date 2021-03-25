from mask_data_loader import AnnotatedDataset
MASK_DS = AnnotatedDataset('dataset_cropped/all.csv', 'dataset_cropped/imgs_3class')
for i in range(len(MASK_DS)):
    try:
        MASK_DS.crop_out(i, inPlace = True)
    except:
        pass
