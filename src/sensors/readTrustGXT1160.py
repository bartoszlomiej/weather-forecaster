import numpy as np
import cv2
import time
from timer import Timer

def getSnapshotBytes():
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        cv2.imwrite(f"camera_data_{time.time()}.png", image)
        return image
    else:
        print("Error while capturing the image.")
        return 0

def createCameraDictionary(success_rate, time_interval, measurement_delay):
    return {"Success rate":success_rate, "Time interval": time_interval, "Delay": measurement_delay}

def repeatExperiment(time_interval=900, measurement_delay=10):
    timer = Timer()
    number_of_trials, n = 0, 0
    while(timer.getTimeDifference() <= time_interval):
        if getSnapshotBytes():
            number_of_tirals += 1
        n += 1
        time.sleep(measurement_delay)
    return createCameraDictionary(number_of_tirals/n, time_interval, measurement_delay)
    
#getSnapshotBytes()
