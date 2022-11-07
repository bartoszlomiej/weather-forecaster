import numpy as np
import cv2

def getSnapshotBytes():
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        cv2.imwrite("TestCamery.png", image)
        return image
    else:
        print("Error while capturing the image.")
        
getSnapshotBytes()
