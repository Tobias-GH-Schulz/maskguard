from mask_data_loader import AnnotatedDataset
MASK_DS = AnnotatedDataset('dataset_cropped/mask_df_merged.csv', 'dataset_cropped
')
for i in range(len(MASK_DS)):
    try:
        MASK_DS.crop_out(i, inPlace = True)
    except:
        pass
