import serial
import time

arduinoTest = serial.Serial("com9", 9600) # 9600 baud from serial
time.sleep(1)

while True:
    # Checking if there is any data from the arduino
    while(arduinoTest.inWaiting() == 0):
        pass

    dataPacket = arduinoTest.readline().decode('utf-8').strip()
    print(dataPacket)


