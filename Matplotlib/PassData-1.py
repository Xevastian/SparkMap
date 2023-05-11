import time
import serial

arduinoData = serial.Serial('com3',9600)
time.sleep(2)
while True:
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

