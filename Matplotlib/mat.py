import time
import matplotlib.pyplot as plt
import serial
from drawnow import *

all_value = []
aces_value = []
cics_value = []
ceafad_value = []
cit_value = []

arduinoData = serial.Serial('COM3',9600)

cnt=0

def AllFig():
    plt.figure('Overall Consumption')
    plt.ylim(-1,15)
    plt.grid(True)
    plt.ylabel("Voltage")
    plt.plot(all_value, label="Voltage V")
    plt.figure('ACES Electric Consumption')
    plt.ylim(-1,15)
    plt.grid(True)
    plt.ylabel("Voltage")
    plt.plot(aces_value, label="Voltage V")
    




# Start the infinite loop
while True:
    # Generate the new data point
    while (arduinoData.inWaiting()==0):
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket,'utf-8')
    dataPacket = dataPacket.strip('\r\n')
    dataArray = dataPacket.split(', ')
    overall = int(dataArray[0])
    aces = int(dataArray[1])
    cics = int(dataArray[2])
    ceafad = int(dataArray[3])
    cit = int(dataArray[4])
    all_value.append(overall)
    aces_value.append(aces)
    
    plt.pause(0.00001)
    cnt = cnt + 1
    if cnt > 50:
        all_value.pop(0)
        aces_value.pop(0)
    drawnow(AllFig)


plt.show()
arduinoData.close()
    
    
