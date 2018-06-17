
# coding: utf-8

# In[2]:


import serial
import matplotlib.pyplot as plt
from drawnow import *


# In[3]:


def plot_func():
    plt.title("Light")
    plt.ylim(500,800)
    plt.xlabel("Time (sec)")
    plt.plot(light)
    plt.show()


# In[5]:


arduino = serial.Serial('/dev/ttyACM0',9600)
plt.ion()
cnt=0
light=[]
while True:
    if arduino.inWaiting()>1:
        myData = arduino.readline()
        myData = float(myData)
        light.append(myData)
        drawnow(plot_func)
        cnt = cnt+1
        if cnt>50:
            light.pop(0)

