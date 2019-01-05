import cv2
import numpy as np
import _pickle as cPickle
import os
from PIL import Image


def randomMask(k):
    mask = np.zeros((256, 256))
    center = np.random.randint(78, 178, size=2)
    bbx = np.random.randint(50, 128, size = 2)
    for i in range(bbx[0]):
        for j in range(bbx[1]):
            mask[center[0]+i-bbx[0]//2][center[1]+j-bbx[1]//2] = 255
    # return  mask
    cv2.imwrite("maskData/"+str(k)+".jpg", mask)

def select(img):
    cnt = 0
    img = img.resize((256,256))
    for i in range(img.size[0]):
        for j in  range(img.size[1]):
            if img.getpixel((i, j)) > 100:
                img.putpixel((i, j), 255)
                #cnt = cnt+1
    img = img.convert('1')
    if cnt < 256*256/2:
        print(111)
        return img

if __name__ == "__main__":
    '''
    maskDir = 'mask/'
    maskList = os.listdir(maskDir)
    for name in maskList:
        img = Image.open(maskDir+name)
        mask = select(img)
        if mask:
            mask.save(name)
    '''
    for i in range(1000):
        randomMask(i)
        img = Image.open("maskData/"+str(i)+".jpg")
        img = img.convert('1')
        img.save("maskData/"+str(i)+".jpg")