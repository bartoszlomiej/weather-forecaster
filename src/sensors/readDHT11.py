#!/usr/bin/python3
import RPi.GPIO as GPIO
import dht11
import time

#pin denotes the GPIO pin
PIN = 24

class Timer:
    def __init__(self):
        self.ref_time = int(time.time())
        self.current_time = 0

    def __setCurrentTime(self):
        self.current_time = int(time.time())

    def getTimeDifference(self):
        self.__setCurrentTime()
        return self.current_time - self.ref_time

def initialize(pin):
    GPIO.setmode(GPIO.BCM)

def readData(pin):
    sensor = dht11.DHT11(pin = PIN)
    result = sensor.read()
    if result.is_valid():
        return result.temperature, result.humidity
        #        print("Temperature: %-3.1f C" % result.temperature)
        #        print("Humidity: %-3.1f %%" % result.humidity)
    else:
        raise Exception("Error of the sensor occured %d" % result.error_code)

def checkDataValidity(pin, temperature_sum, humidity_sum, number_of_trials):
    try:
        temperature, humidity = readData(pin)
        return temperature_sum + temperature, humidity_sum + humidity, number_of_trials + 1
    except Exception:
        return temperature_sum, humidity_sum, number_of_trials
        
def convertToSeconds(minutes): #useful for time_interval 
    return minutes * 60
    
def readAverage(pin, time_interval=900, measurement_delay=10):
    #reads average of the sensor's data in the given time interval
    timer = Timer()
    temperature_sum, humidity_sum = 0, 0
    number_of_trials, n = 0, 0 
    while(timer.getTimeDifference() <= time_interval):
        readData(pin)
        time.sleep(measurement_delay)
        temperature_sum, humidity_sum, number_of_trials = checkDataValidity(pin, temperature_sum, humidity_sum, \
                                                                            number_of_trials)
        n += 1
    return temperature_sum / number_of_trials, humidity_sum / number_of_trials, number_of_trials, n

if __name__ == "__main__":    
    initialize(PIN)
    readAverage(PIN)
