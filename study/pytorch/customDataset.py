import os
import pandas as pd
import numpy as np

# import torch
from torch.utils.data import Dataset
from torchvision.io import read_image

'''
Dataset : 흉부 X-Ray 전/후방 이미지
Target : 정상 = 1 / 세균성 폐렴 = 0 / 바이러스성 폐렴 = 2
'''

def MakeAnnotationFile(dirPath, fileName):
    dataDic = {'name':[], 'class':[], 'path':[]}
    
    try:
        targets = os.listdir(dirPath)

        for i, target in enumerate(targets):
            imgName = os.listdir(os.path.join(dirPath, target))
            imgClass = np.full((len(imgName), ), i)
            imgPath = [os.path.join(dirPath, target, name) for name in imgName]

            dataDic['name'].extend(imgName)
            dataDic['class'].extend(imgClass)
            dataDic['path'].extend(imgPath)

        df = pd.DataFrame(dataDic)
        df = pd.get_dummies(df, columns=['class'])
        df.to_csv(os.path.join(dirPath, fileName))
    except Exception as e:
        print(e)

class CustomImageDataset(Dataset):
    def __init__(self, fileDir):
        self.imgInfo = pd.read_csv(fileDir, index_col=0)
        # self.transform = transform

    def __len__(self):
        return len(self.imgInfo)

    def __getitem__(self, idx):
        imgPath = self.imgInfo.iloc[idx, 2]
        image = read_image(imgPath)
        target = self.imgInfo.iloc[idx, -3:].values

        # if self.transform:
        #     augmented = self.transform(image=image)
        #     image = augmented['image']

        return image, target
