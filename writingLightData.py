
# coding: utf-8

# In[2]:


import pandas
import serial
import datetime


# In[10]:


df = pandas.DataFrame(columns=('sl','time','light'))
arduino = serial.Serial('/dev/ttyACM0',9600)
cnt=0
cout=0
while True:
    if arduino.inWaiting()>1:
        time = str(datetime.datetime.now())
        myData = arduino.readline()
        myData = float(myData)
        df.loc[cnt] = cnt,time,myData
        cnt = cnt+1
        if cnt==8000:
            df.to_csv('out'+str(cout)+'.csv',sep=',',encoding='utf-8')
            cout = cout+1
            cnt = 0
        

