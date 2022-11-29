#!/usr/bin/python3
from timer import Timer
import RPi.GPIO as GPIO
import dht11
import time

#pin denotes the GPIO pin
PIN = 24

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

def createDHTDictionary(avg_temperature, avg_humidity, success_rate,
                        time_interval, measurement_delay):
    return {"Temperature":avg_temperature, "Humidity":avg_humidity, "Success rate":success_rate, "Time interval": time_interval, "Delay": measurement_delay}

def readAverage(pin, dht_result, time_interval=900, measurement_delay=10):
    #reads average of the sensor's data in the given time interval
    timer = Timer()
    temperature_sum, humidity_sum = 0, 0
    number_of_trials, n = 0, 0 
    while(timer.getTimeDifference() <= time_interval):
        temperature_sum, humidity_sum, number_of_trials = checkDataValidity(pin, temperature_sum, humidity_sum, \
                                                                            number_of_trials)
        time.sleep(measurement_delay)
        n += 1
    dht_result = createDHTDictionary(temperature_sum / number_of_trials, humidity_sum / number_of_trials,
                               number_of_trials/n, time_interval, measurement_delay)

if __name__ == "__main__":
    initialize(PIN)
    readAverage(PIN)
