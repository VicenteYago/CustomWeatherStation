from gpiozero import Button
import math
import time
import bme280_sensor
import wind_direction_byo
import statistics
import dsb1820_therm

radius = 9.0 / 100 # in meters
wind_interval_sec = 5 
anemometer_adjustment = 1.18

def spin():
    global wind_count
    wind_count = wind_count + 1
    print("spin " + str(wind_count))

def getWindSpeed(t):
    circunference = (2.0*math.pi)*radius
    dist = circunference*(wind_count/2) # each rotation takes 2 counts
    speed = dist/t
    return speed*anemometer_adjustment

wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin # call spin() each time event occurs

while True :
    wind_count = 0
    time.sleep(wind_interval_sec)
    print(getWindSpeed(wind_interval_sec), "m/s")
    
    
