#from sensors.readDHT11 import initialize, readAverage
#from sensors.readTrustGXT1160 import repeatExperiment
from readDHT11 import initialize, readAverage
from readTrustGXT1160 import repeatExperiment
#from cloud.sendData import sendData

import threading
import time

'''
read data from sensors, save it to a file (e.g. synchronize to cloud in every 10 minutes. gathered data save. In case of not connecting to the cloud -> write to a file. Update log file.

'''
PIN = 24

def saveLogFile(avg_temp, avg_hum, success_rate_dht, success_rate_cam):
    if success_rate < 0.5:
        pass #raise alarm
    pass

def getSensorsData(time_interval=900, measurement_delay=10):
    avg_temperature,  avg_humidity, h_n_trials, h_n = readData(PIN, time_interval, measurement_delay)
    c_n_trials, c_n = repeatExperiment(time_interval, measurement_delay)
    #send it to the server
    #save to log file

def createCameraThread(time_interval, measurement_delay):
    camera_result = {}
    y = threading.Thread(target=repeatExperiment, args=(camera_result, time_interval, measurement_delay))
    return camera_result, y
    
def createDHTThread(PIN, time_interval, measurement_delay):
    dht_result = {}
    x = threading.Thread(target=readAverage, args=(PIN, dht_result, time_interval, measurement_delay))
    print("DHT:", dht_result)
    return dht_result, x
    
def createThreads():
    threads = list()
    dht_result, x = createDHTThread(PIN, 40, 10)
    camera_result, y = createCameraThread(40, 20)
    threads.append(x)
    threads.append(y)
    return threads, dht_result, camera_result

def runThreads():
    threads, dht_result, camera_result = createThreads()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    del threads
    return dht_result, camera_result

def main():
    initialize(PIN)
    for i in range(10):
        dht_result, camera_result = runThreads()
        print(dht_result)
        print(camera_result)
        
if __name__ == "__main__":
    main()
p
