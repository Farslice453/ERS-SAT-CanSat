import serial
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange 
from drawnow import drawnow
import numpy as np
import math


port = '/dev/ttyUSB0'
baud = 2000000
ser = serial.Serial(port, baud)

if ser.is_open == True:
    print("Connected to port: ", port)
    print("Connection established, WHOOOH!")

upt = int(0)

def make_fig():
    a = int(2)
    b = int(4)
    plt.subplot(a, b, 1)
    plt.plot(x, y)
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (Celsius)")

    plt.subplot(a, b, 2)
    plt.plot(x1, y1)
    plt.xlabel("Time (s)")
    plt.ylabel("Pressure (hPa)")

    plt.subplot(a, b, 3)
    plt.plot(x2, y2)
    plt.xlabel("Time (s)")
    plt.xlabel("RSSI")

    plt.subplot(a, b, 4)
    plt.plot(x3, y3)
    plt.xlabel("Time (s)")
    plt.xlabel("Uptime")
    
    plt.subplot(a, b, 5)
    plt.plot(x4, y4)
    plt.xlabel("Time (s)")
    plt.xlabel("X (g)")
    
    plt.subplot(a, b, 6)
    plt.plot(x5, y5)
    plt.xlabel("Time (s)")
    plt.xlabel("Y (g)")
    
    plt.subplot(a, b, 6)
    plt.plot(x6, y6)
    plt.xlabel("Time (s)")
    plt.xlabel("Z (g)")
    
    

fig = plt.figure()  
x = list()
y = list()
x1 = list()
y1 = list()
x2 = list()
y2 = list()
x3 = list()
y3 = list()
x4 = list()
y4 = list()
x5 = list()
y5 = list()
x6 = list()
y6 = list()


for uptime in range(10000):
    time.sleep(25)
    getData = ser.readline()
    dataString = getData.decode('utf-8')
    
    datos = dataString.split(", ")
    
    largo = len(datos)
    
    temp = float(datos[1])
    press = float(datos[2])
    packages = float(datos[3])
    x = float(datos[4])
    y = float(datos[5])
    z = float(datos[6])
    rssi = datos[7]
    
    if(largo >= 9):
        latitud = float(datos[9])
        def make_fig2():
            plt.subplot(a, b, 7)
            plt.plot(x7, y7)
            plt.xlabel("Time (s)")
            plt.xlabel("Latitud (degress)")
            
        x7 = list()
        y7 = list()
        x7.append(uptime)
        y7.append(latitud)
        drawnow(make_fig2)
        
        
    if(largo >= 10):
        longitud = float(datos[10])
        def make_fig3():
            plt.subplot(a, b, 8)
            plt.plot(x8, y8)
            plt.xlabel("Time (s)")
            plt.xlabel("Longitud (degress)")
            
        x8 = list()
        y8 = list()
        x8.append(uptime)
        y8.append(longitud)
        drawnow(make_fig3)
    
    
    
    
    print(temp, press, packages, x, y, z)
    
    #temp = float(dataString[0:9])
    #press = float(dataString[10:+16])
    #packages = float(dataString[17:23])
    #x = float()
    #y = float()
    #z = float()
    #rssi = int(dataString[25:29])
    #uptime = int(uptime + 1)



    x.append(upt)
    y.append(temp)

    x1.append(upt)
    y1.append(press)

    x2.append(upt)
    y2.append(rssi)

    x3.append(upt)
    y3.append(packages)
    
    x4.append(upt)
    y4.append(x)
    
    x5.append(upt)
    y5.append(y)
    
    x6.append(upt)
    y6.append(z)
    
    
    
    upt += 1
    drawnow(make_fig)

    #print(temp, press, packages, rssi, uptime)


