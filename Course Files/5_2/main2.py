import os
from PIL import Image

class ImageDataset:
    def __init__(self,root):
        self.root = root
        self.filenames = os.listdir(self.root)
        
    def __getitem__(self,idx):
        # return self.filenames[idx]
        img= Image.open(self.root+'/'+self.filenames[idx])
        return img
    
        
ds = ImageDataset("images")
# print(ds.filenames)
ds[10].show()
