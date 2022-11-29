from sensors.readDHT11 import initialize, readAverage
from sensors.readTrustGXT1160 import repeatExperiment
#from readDHT11 import initialize, readAverage
#from readTrustGXT1160 import repeatExperiment
from sensors.ReturnValueThread import ReturnValueThread
from cloud.sendData import sendData

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
    y = ReturnValueThread(target=repeatExperiment, args=(time_interval, measurement_delay))
    return y
    
def createDHTThread(PIN, time_interval, measurement_delay):
    x = ReturnValueThread(target=readAverage, args=(PIN, time_interval, measurement_delay))    
    return x
    
def createThreads():
    threads = list()
    x = createDHTThread(PIN, 40, 10)
    y = createCameraThread(40, 20)
    threads.append(x)
    threads.append(y)
    return threads

def runThreads():
    threads  = createThreads()
    for thread in threads:
        thread.start()
    dht_result = threads[0].join()
    camera_result = threads[1].join()
    
    del threads
    return dht_result, camera_result

def main():
    initialize(PIN)
    connection = Connection()
    for i in range(10):
        dht_result, camera_result = runThreads()
        connection.getSensorData(dht_result, camera_result)
        
if __name__ == "__main__":
    main()
