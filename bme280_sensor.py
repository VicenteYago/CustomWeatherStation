import bme280
import smbus2
from time import sleep

port = 1
addres = 0x77
bus = smbus2.SMBus(port)


def read_all():
	bme280_data = bme280.sample(bus,addres)
	return bme280_data.humidity, bme280_data.pressure, bme280_data.temperature

bme280.load_calibration_params(bus, addres)

while True :
    print(read_all())
    sleep(2)

