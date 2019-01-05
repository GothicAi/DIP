import cv2
import numpy as np

ori_img = cv2.imread("VOC/out/000007.jpg")
img = cv2.imread("VOC/out/000007.jpg", 0)
mask = cv2.imread("VOC/mask/000007.jpg", 0)
img = img*(mask//254)
cv2.imshow("img", ori_img)
cv2.waitKey()

canny = cv2.Canny(img, 80, 100)
cv2.imwrite("canny.jpg", canny)
cv2.imshow("canny", cv2.imread("canny.jpg"))
cv2.waitKey()

mask = cv2.imread("canny.jpg", 0)
kernel = np.ones((2,2),np.uint8)
mask = cv2.dilate(mask, kernel, iterations = 1)
cv2.imshow("mask", mask)
cv2.waitKey()

res = cv2.inpaint(ori_img, mask, 1, cv2.INPAINT_NS)
cv2.imshow("res", res)
cv2.waitKey()

cv2.destroyAllWindows()


'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

cv2.namedWindow('res')

cv2.createTrackbar('max','res',0,255,nothing)
cv2.createTrackbar('min','res',0,255,nothing)

img = cv2.imread('VOC/out/000007.jpg',0)
mask = cv2.imread("VOC/mask/000007.jpg",0)
img = img*(mask//254)

maxVal=200
minVal=100

while (1):

    if cv2.waitKey(20) & 0xFF==27:
        break
    maxVal = cv2.getTrackbarPos('min','res')
    minVal = cv2.getTrackbarPos('max','res')
    if minVal < maxVal:
        edge = cv2.Canny(img,100,200)
        cv2.imshow('res',edge)
    else:
        edge = cv2.Canny(img,minVal,maxVal)
        cv2.imshow('res',edge)
cv2.destoryAllWindows()
'''