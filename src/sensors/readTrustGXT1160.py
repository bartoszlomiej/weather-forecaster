import numpy as np
import cv2
import time
from sensors.timer import Timer
from sensors.getDominantColors import getDominantColors

def getSnapshotBytes():
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        cv2.imwrite("camera_data.png", image)
        return True
    #    return image
    else:
        print("Error while capturing the image.")
        return 0

def createCameraDictionary(success_rate, time_interval, measurement_delay):
    return {"Success rate":success_rate, "Time interval": time_interval, "Delay": measurement_delay}

def repeatExperiment(time_interval=9, measurement_delay=1):
    timer = Timer()
    number_of_trials, n = 0, 0
    result = 0
    image = getSnapshotBytes()
    if image:
        result = getDominantColors("camera_data.png")
    '''
    while(timer.getTimeDifference() <= time_interval):
        image = getSnapshotBytes()
        if image:
            result = getDominantColors("camera_data.png")
            number_of_trials += 1
        n += 1
        time.sleep(measurement_delay)
    '''
    #return createCameraDictionary(number_of_tirals/n, time_interval, measurement_delay)
    return result


#getSnapshotBytes()
