from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial

# Initialize the serial connection
arduinoData = serial.Serial('com3', 9600)

# Initialize the data lists
max_data_points = 100  # Maximum number of data points to display
data_queues = [
    deque(maxlen=max_data_points) for _ in range(5)
]  # Create deque for each data type

# Create the figures and axes
fig, (ax_all, ax_aces, ax_cics, ax_ceafad, ax_cit) = plt.subplots(5, 1, figsize=(8, 12))
axes = [ax_all, ax_aces, ax_cics, ax_ceafad, ax_cit]
line_objects = []  # Store line objects for each plot
labels = ['Overall Consumption', 'ACES', 'CICS', 'CEAFAD', 'CIT']
y_lims = [(-1, 13), (-1, 4), (-1, 4), (-1, 4), (-1, 4)]

# Set the plot limits and labels for each figure
for ax, label, y_lim in zip(axes, labels, y_lims):
    ax.set_ylim(y_lim)  # Adjust ylim as needed
    ax.set_ylabel("Voltage")
    ax.grid(True)
    line, = ax.plot([], [], label=label)
    line_objects.append(line)

# Animation update function
def update(frame):
    # Read the data from Arduino
    while arduinoData.inWaiting() == 0:
        pass
    dataPacket = arduinoData.readline().decode('utf-8').strip()
    dataArray = list(map(int, dataPacket.split(', ')))
    
    # Append the data to the deques
    for i, data in enumerate(dataArray):
        data_queues[i].append(data)
    
    # Update the line data for each figure
    for i, line in enumerate(line_objects):
        line.set_data(range(len(data_queues[i])), data_queues[i])
    
    # Adjust the x-axis limits if neeed
    for ax in axes:
        ax.set_xlim(0, len(data_queues[0]))
    
    # Return the line objects
    return line_objects

# Function to initialize the plots
def init():
    for line in line_objects:
        line.set_data([], [])
    return line_objects

# Create the animations
animations = [
    animation.FuncAnimation(fig, update, frames=None, init_func=init, blit=True, interval=1)
    for fig in [fig]
]

# Display the plots
for ax in axes:
    ax.legend()

class MyApp(App):

    def build(self):
        box = BoxLayout()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return box

MyApp().run()