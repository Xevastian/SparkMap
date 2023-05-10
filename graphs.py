import time
import matplotlib.pyplot as plt
import serial
from drawnow import *


all_value = []
aces_value = []
cics_value = []
ceafad_value = []
cit_value = []


arduinoData = serial.Serial('COM9',9600)


plt.ion()
cnt=0


def AllFig():
    plt.ylim(-1,15)
    plt.title("Overall Electric Consumption")
    plt.grid(True)
    plt.ylabel("Voltage")
    plt.plot(all_value, label="Voltage V")
    plt.legend


def ACESFig():
    plt.ylim(-1,15)
    plt.title("ACES Electric Consumption")
    plt.grid(True)
    plt.ylabel("Voltage")
    plt.plot(aces_value, label="Voltage V")
    plt.legend


# Start the infinite loop
while True:
    # Generate the new data point
    while (arduinoData.inWaiting()==0):
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket,'utf-8')
    dataPacket = dataPacket.strip('\r\n')
    dataArray = dataPacket.split(', ')
    print(dataArray)
    overall = int(dataArray[0])
    aces = int(dataArray[1])
    cics = int(dataArray[2])
    ceafad = int(dataArray[3])
    cit = int(dataArray[4])
    all_value.append(overall)
    aces_value.append(aces)
   
    drawnow(AllFig,ACESFig)
    plt.pause(0.00001)
    cnt = cnt + 1
    if cnt > 50:
        all_value.pop(0)
        aces_value.pop(0)


plt.show()
ser.close()

