import numpy as np
import cv2
import time

def getSnapshotBytes():
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        cv2.imwrite("TestCamery.png", image)
        return image
    else:
        print("Error while capturing the image.")
        return 0

def repeatExperiment(time_interval=900, measurement_delay=10):
    timer = Timer()
    number_of_trials, n = 0, 0
    while(timer.getTimeDifference() <= time_interval):
        if getSnapshotBytes():
            number_of_tirals += 1
        n += 1
        time.sleep(measurement_delay)
    return number_of_tirals, n

getSnapshotBytes()
