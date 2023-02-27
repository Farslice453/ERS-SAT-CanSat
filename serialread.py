import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange 
from drawnow import drawnow
import numpy as np


port = '/dev/ttyUSB0'
baud = 2000000
ser = serial.Serial(port, baud)

#if ser.is_open == True:
    #print("Connected to port: ", port)
    #print("Connection established, WHOOOH!")

uptime = int(0)

def make_fig():
    a = int(2)
    b = int(2)
    plt.subplot(a, b, 1)
    plt.plot(x, y)

    plt.subplot(a, b, 2)
    plt.plot(x1, y1)

    plt.subplot(a, b, 3)
    plt.plot(x2, y2)

    plt.subplot(a, b, 4)
    plt.plot(x3, y3)






#def make_fig1():

plt.ion() 
fig = plt.figure()  
x = list()
y = list()
x1 = list()
y1 = list()
x2 = list()
y2 = list()
x3 = list()
y3 = list()


for uptime in range(10000):
    getData = ser.readline()
    dataString = getData.decode('utf-8')
    temp = float(dataString[0:9])
    press = float(dataString[10:16])
    packages = float(dataString[17:23])
    rssi = int(dataString[25:29])
    uptime = int(uptime + 1)



    x.append(uptime)
    y.append(temp)

    x1.append(uptime)
    y1.append(press)

    x2.append(uptime)
    y2.append(rssi)

    x3.append(uptime)
    y3.append(packages)


    uptime += 1
    drawnow(make_fig)

    #print(temp, press, packages, rssi, uptime)

