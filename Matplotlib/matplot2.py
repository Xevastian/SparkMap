import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import serial

# Initialize the serial connection
arduinoData = serial.Serial('/dev/cu.usbmodem145101', 9600)

# Initialize the data lists
max_data_points = 100  # Maximum number of data points to display
all_value = deque(maxlen=max_data_points)
aces_value = deque(maxlen=max_data_points)
cics_value = deque(maxlen=max_data_points)
ceafad_value = deque(maxlen=max_data_points)
cit_value = deque(maxlen=max_data_points)

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

# Create empty line objects for each line to be plotted
line_all, = ax_all.plot([], [], label='Overall Consumption')
line_aces, = ax_aces.plot([], [], label='ACES')
line_cics, = ax_cics.plot([], [], label='CICS')
line_ceafad, = ax_ceafad.plot([], [], label='CEAFAD')
line_cit, = ax_cit.plot([], [], label='CIT')

# Animation update function
def update(frame):
    # Read the data from Arduino
    while arduinoData.inWaiting() == 0:
        pass
    dataPacket = arduinoData.readline().decode('utf-8').strip()
    dataArray = dataPacket.split(', ')
    overall = int(dataArray[0])
    aces = int(dataArray[1])
    cics = int(dataArray[2])
    ceafad = int(dataArray[3])
    cit = int(dataArray[4])
    
    # Append the data to the deques
    all_value.append(overall)
    aces_value.append(aces)
    cics_value.append(cics)
    ceafad_value.append(ceafad)
    cit_value.append(cit)
    
    # Update the line data for the overall consumption figure
    line_all.set_data(range(len(all_value)), all_value)
    
    # Update the line data for the aces figure
    line_aces.set_data(range(len(aces_value)), aces_value)
    
    # Update the line data for the cics figure
    line_cics.set_data(range(len(cics_value)), cics_value)
    
    # Update the line
    # Update the line data for the ceafad figure
    line_ceafad.set_data(range(len(ceafad_value)), ceafad_value)
    
    # Update the line data for the cit figure
    line_cit.set_data(range(len(cit_value)), cit_value)
    
    # Adjust the x-axis limits if needed
    ax_all.set_xlim(0, len(all_value))
    ax_aces.set_xlim(0, len(aces_value))
    ax_cics.set_xlim(0, len(cics_value))
    ax_ceafad.set_xlim(0, len(ceafad_value))
    ax_cit.set_xlim(0, len(cit_value))
    
    # Return the line objects
    return line_all, line_aces, line_cics, line_ceafad, line_cit

# Function to initialize the plots
def init():
    line_all.set_data([], [])
    line_aces.set_data([], [])
    line_cics.set_data([], [])
    line_ceafad.set_data([], [])
    line_cit.set_data([], [])
    return line_all, line_aces, line_cics, line_ceafad, line_cit

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
