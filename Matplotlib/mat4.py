import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import serial

# Initialize the serial connection
arduinoData = serial.Serial('/dev/cu.usbmodem145101', 9600)

# Initialize the data lists
max_data_points = 100  # Maximum number of data points to display
data_queues = [
    deque(maxlen=max_data_points) for _ in range(5)
]  # Create deque for each data type

# Create the figures and axes
fig_all, ax_all = plt.subplots()
fig_aces, ax_aces = plt.subplots()
fig_cics, ax_cics = plt.subplots()
fig_ceafad, ax_ceafad = plt.subplots()
fig_cit, ax_cit = plt.subplots()

# Set the plot limits and labels for the overall consumption figure
ax_all.set_ylim(-1, 13)
ax_all.set_ylabel("Voltage")
ax_all.grid(True)

# Set the plot limits and labels for the aces figure
ax_aces.set_ylim(-1, 4)
ax_aces.set_ylabel("Voltage")
ax_aces.grid(True)

# Set the plot limits and labels for the cics figure
ax_cics.set_ylim(-1, 4)
ax_cics.set_ylabel("Voltage")
ax_cics.grid(True)

# Set the plot limits and labels for the ceafad figure
ax_ceafad.set_ylim(-1, 4)
ax_ceafad.set_ylabel("Voltage")
ax_ceafad.grid(True)

# Set the plot limits and labels for the cit figure
ax_cit.set_ylim(-1, 4)
ax_cit.set_ylabel("Voltage")
ax_cit.grid(True)

line_objects = []  # Store line objects for each plot
labels = ['Overall Consumption', 'ACES', 'CICS', 'CEAFAD', 'CIT']

# Create empty line objects for each line to be plotted
line_all, = ax_all.plot([], [], label=labels[0])
line_aces, = ax_aces.plot([], [], label=labels[1])
line_cics, = ax_cics.plot([], [], label=labels[2])
line_ceafad, = ax_ceafad.plot([], [], label=labels[3])
line_cit, = ax_cit.plot([], [], label=labels[4])

line_objects = [line_all, line_aces, line_cics, line_ceafad, line_cit]

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
    line_all.set_data(range(len(data_queues[0])), data_queues[0])
    line_aces.set_data(range(len(data_queues[1])), data_queues[1])
    line_cics.set_data(range(len(data_queues[2])), data_queues[2])
    line_ceafad.set_data(range(len(data_queues[3])), data_queues[3])
    line_cit.set_data(range(len(data_queues[4])), data_queues[4])
    
    # Adjust the x-axis limits if needed
    ax_all.set_xlim(0, len(data_queues[0]))
    ax_aces.set_xlim(0, len(data_queues[1]))
    ax_cics.set_xlim(0, len(data_queues[2]))
    ax_ceafad.set_xlim(0, len(data_queues[3]))
    ax_cit.set_xlim(0, len(data_queues[4]))
    
    # Return the line objects
    return line_objects

# Function to initialize the plots
def init():
    for line in line_objects:
        line.set_data([], [])
    return line_objects

# Create the animations
ani_all = animation.FuncAnimation(fig_all, update, frames=None, init_func=init, blit=True, interval=1)
ani_aces = animation.FuncAnimation(fig_aces, update, frames=None, init_func=init, blit=True, interval=1)
ani_cics = animation.FuncAnimation(fig_cics, update, frames=None, init_func=init, blit=True, interval=1)
ani_ceafad = animation.FuncAnimation(fig_ceafad, update, frames=None, init_func=init, blit=True, interval=1)
ani_cit = animation.FuncAnimation(fig_cit, update, frames=None, init_func=init, blit=True, interval=1)

# Display the plots
ax_all.legend()
ax_aces.legend()
ax_cics.legend()
ax_ceafad.legend()
ax_cit.legend()
plt.show()

# Close the serial connection
arduinoData.close()
