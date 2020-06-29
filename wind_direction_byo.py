from gpiozero import MCP3008
import time
import math

adc = MCP3008(channel=0)
count = 0
values = []
volts  = [0.4, 1.4, 1.2, 2.8,
          2.9, 2.2, 2.5, 1.8,
          2.0, 0.7, 0.8, 0.1,
          0.3, 0.2, 0.6, 2.7]
          
volts2 = [2.8, 1.9, 2.0, 0.52,
          0.57, 0.4, 1.0, 0.7,
          1.4, 1.3, 2.5, 2.4, 
          3.1, 2.9, 3.0, 2.7]

volts_dic = {
    0.4: 0.0,
    1.4: 22.5,
    1.2: 45.0, 
    2.8: 67.5,
    2.7: 90.5,
    2.9: 112.5, 
    2.2: 135.0, 
    2.5: 157.5,
    1.8: 180.0,
    2.0: 202.5, 
    0.7: 225.0, 
    0.8: 247.5, 
    0.1: 270.0, 
    0.3: 292.5,
    0.2: 315.0, 
    0.6: 337.5
    }


def get_average(angles):
    sin_sum = 0.0
    cos_sum = 0.0

    for angle in angles:
        r = math.radians(angle)
        sin_sum += math.sin(r)
        cos_sum += math.cos(r)

    flen = float(len(angles))
    s = sin_sum / flen
    c = cos_sum / flen
    arc = math.degrees(math.atan(s / c))
    average = 0.0

    if s > 0 and c > 0:
        average = arc
    elif c < 0:
        average = arc + 180
    elif s < 0 and c > 0:
        average = arc + 360

    return 0.0 if average == 360 else average

while True:
        wind = round(adc.value*3.3,1)
        if not wind in volts_dic:
          print("Unknown value :", str(wind))
        else:
          print('found: ' + str(wind) + ' ' + str(volts_dic[wind])) 

