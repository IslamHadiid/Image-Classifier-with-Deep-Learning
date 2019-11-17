import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import nn
from torch import tensor
from torch import optim
import torch.nn.functional as F
from torch.autograd import Variable
from torchvision import datasets, transforms
import torchvision.models as models
from collections import OrderedDict
import json
import PIL
from PIL import Image
import argparse

import train

ap = argparse.ArgumentParser(description='Predict.py')

ap.add_argument('--input', default='./flowers/test/1/image_06752.jpg', nargs='?', action="store", type = str)
ap.add_argument('--dir', action="store",dest="data_dir", default="./flowers/")
ap.add_argument('--checkpoint', default='checkpoint.pth', nargs='?', action="store", type = str)
ap.add_argument('--top_k', default=5, dest="top_k", action="store", type=int)
ap.add_argument('--category_names', dest="category_names", action="store", default = 'cat_to_name.json')
ap.add_argument('--gpu', default="gpu", action="store", dest="gpu")

pa = ap.parse_args()
path_image = pa.input
top_k = pa.top_k
device = pa.gpu
cat_names = pa.category_names
path = pa.checkpoint

pa = ap.parse_args()

def main():
    model=train.load_checkpoint(path)
    with open(cat_names, 'r') as json_file:
        cat_to_name = json.load(json_file)
    probabilities = train.predict(path_image, model, top_k, device)
    labels = [cat_to_name[str(index + 1)] for index in np.array(probabilities[1][0])]
    probability = np.array(probabilities[0][0])
    i=0
    while i < top_k:
        print("{} it`s probability {}".format(labels[i], probability[i]))
        i += 1
    print("predect is done!")

    
if __name__== "__main__":
    main()
