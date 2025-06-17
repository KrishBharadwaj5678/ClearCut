import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
segmentor = SelfiSegmentation()

listImg = os.listdir("Images")
imgList = []
for imgPath in listImg:
    img = cv2.imread(f"Images/{imgPath}")
    img = cv2.resize(img, (640, 480))
    imgList.append(img)

indexImg = 0

while True:
    success, img = cap.read()
    img = segmentor.removeBG(img,imgList[indexImg],cutThreshold=0.6)
    cv2.imshow("Camera Feed",img)
    key = cv2.waitKey(1)
    if key == ord("a"):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord("d"):
        if indexImg < len(imgList) - 1:
            indexImg += 1
    elif key == ord("q"):
        break