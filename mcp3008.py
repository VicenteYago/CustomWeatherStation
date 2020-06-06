from gpiozero import MCP3008
import time

while True:
	adc = MCP3008(channel=0)
	time.sleep(0.5)
	print(adc.value)
