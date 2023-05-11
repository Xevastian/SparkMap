import time
import matplotlib.pyplot as plt
import serial
from drawnow import *
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt

all_value = []
aces_value = []
cics_value = []
ceafad_value = []
cit_value = []

arduinoData = serial.Serial('COM3',9600)

cnt=0

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
for ax, color in zip([ax1, ax2, ax3, ax4], ['green', 'red', 'yellow', 'blue']):
    plt.setp(ax.spines.values(), color=color)
    ax.plot([0, 7], c=color)
    plt.setp([ax.get_xticklines(), ax.get_yticklines()], color=color)

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
    plt.show()

#plt.show()
arduinoData.close()
 
#fig, (ax1,ax2) = plt.subplots(2,1)
#ax1.plot([1, 2, 3, 4], [1, 4, 2, 3])
#ax2.plot([1, 2, 3, 4], [3, 1, 2, 4])
class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.add_widget(FigureCanvasKivyAgg(figure=fig1))

class MyApp(App):
    def build(self):
        return MyLayout()

MyApp().run()