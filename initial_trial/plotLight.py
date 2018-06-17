
# coding: utf-8


import serial
import matplotlib.pyplot as plt
from drawnow import * #Used to plot live data

def plot_func():
    plt.title("Light")
    plt.ylim(500,800) #Can vary depending upon the resistor value
    plt.xlabel("Time (sec)")
    plt.plot(light)
    plt.show()


arduino = serial.Serial('/dev/ttyACM0',9600) #Creating an object to Fetch the value from Serial Port
plt.ion()                                    #Used to plot live data in a single frame
cnt=0
light=[]                                    #Where the data is stored
while True:
    if arduino.inWaiting()>1:
        myData = arduino.readline()
        myData = float(myData)
        light.append(myData)
        drawnow(plot_func)
        cnt = cnt+1
        if cnt>50:                          #Can change the number depending upon the number of values you want to be plotted
            light.pop(0)                    #Removing the previous value to keep the plot till 50 values

