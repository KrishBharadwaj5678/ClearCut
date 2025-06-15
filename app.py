import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
segmentor = SelfiSegmentation()
imgBg = cv2.imread("Images/img1.jpg")
imgBg = cv2.resize(imgBg,(640,480))
while True:
    success, img = cap.read()
    img = segmentor.removeBG(img,imgBg,cutThreshold=0.7)
    cv2.imshow("Camera Feed",img)
    cv2.waitKey(1)