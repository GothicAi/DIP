from PIL import Image
import cv2
import numpy as np
import os

def dirct_blend(img1, img2, alpha):
    return img1 * alpha + img2 * (1 - alpha)


def stage_blend(img1, img2, mask, stage, alpha):
    resc = cv2.split(img1)
    img2c = cv2.split(img2)
    for i in range(stage):
        for i in range(3):
            resc[i] = ((resc[i] * alpha + img2c[i] * (1 - alpha)) * mask/255) + (resc[i] * (1 - mask/255))
        mask = erode(mask, 4)
    res = cv2.merge(resc)
    return res


def erode(img, kernel_size=10):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    return cv2.erode(img, kernel)

def inpaint(img, mask):
    dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
    return dst

if __name__ == "__main__":
    '''
    with open("res1_flist_path.txt", "r") as f:
        res1list = f.read().splitlines()
    with open("res2_flist_path.txt", "r") as f:
        res2list = f.read().splitlines()
    with open("mask_flist_path.txt", "r") as f:
        masklist = f.read().splitlines()
    '''
    image = os.listdir("VOC/res3")
    for i in image:
        # img = cv2.imread("VOC/img/"+i)
        img1 = cv2.imread("VOC/res1/"+i)
        img2 = cv2.imread("VOC/res3/"+i)
        mask = cv2.imread("VOC/mask/"+i, 0)
        # dst = inpaint(img, mask)
        # cv2.imwrite("VOC/res2/"+i, dst)
        # img1 = cv2.imread(res1list[i])
        # img2 = cv2.imread(res2list[i])
        # mask = cv2.imread(masklist[i], 0)
        res = stage_blend(img1, img2, mask, 10, 0.9)
        cv2.imwrite("VOC/out/" + "new" + ".jpg", res)
