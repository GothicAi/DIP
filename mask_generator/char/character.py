import cv2
import os
import random
import numpy as np
from PIL import Image

def char2sentence():
    inpath = "char/"
    outpath = "sentence/"
    imglist = os.listdir(inpath)
    for times in range(50):
        length = random.randint(4,8)
        res = cv2.imread(inpath + str(random.randint(0, 34)) + ".jpg", 0)
        for i in range(length-1):
            img = cv2.imread(inpath+str(random.randint(0,34))+".jpg", 0)
            res = np.hstack((res, img))
        cv2.imwrite(outpath+str(times)+".jpg", res)

def sentence2mask():
    inpath = "sentence/"
    outpath = "charmask/"
    imglist = os.listdir(inpath)
    for times in range(500):
        mask = np.zeros((256,256))
        img = np.random.choice(imglist)
        img = cv2.imread(inpath+img)
        img = Image.fromarray(img.astype('uint8'))
        img = img.resize((random.randint(128,200), random.randint(20,50)), Image.ANTIALIAS)
        mask = Image.fromarray(mask.astype('uint8'))
        mask.paste(img, (0, 110))
        mask = mask.rotate(random.randint(-90,90))
        mask.save(outpath+str(times)+".jpg")

if __name__ == '__main__':
    char2sentence()
    sentence2mask()