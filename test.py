from HandTrackingModule import HandDetector
import cv2
import os
import numpy as np

# Variables
width, height = 1280, 720
folderPath = "Presentation"
imgNumber = 0
hs, ws = int(120 * 1), int(213 * 1)

# camera capture 
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)


# Get the list of Presentation images 
pathImages = sorted(os.listdir(folderPath), key = len)
print(pathImages)

while True:
    # Import Images
    success, img = cap.read()
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)
    
    
    # Adding webcam image on slides
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws: w] = imgSmall
    
    
    cv2.imshow("Image", img)
    cv2.imshow("Presentation", imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break