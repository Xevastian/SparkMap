# SparkMap
CS121 - Advance Computer Programming Project

## Introduction
Welcome to the project that offers electricity tools and resources. The team is dedicated to creating an electricity consumption map for Batangas State University and The National Engineering University – Alangilan Campus. By monitoring consumption and promoting sustainable practices, they aim to minimize waste and improve efficiency. This initiative aligns with Sustainable Development Goal 12, emphasizing the importance of sustainable consumption and production patterns. Through their prototype, the team aims to understand building electricity consumption, enabling informed decisions and contributing to a sustainable future. Join them on this journey towards responsible electricity consumption for a brighter future.

## Table of Contents
- [Project Scheme](#project-scheme)
- [Installation](#installation)
- [Features](#features)
- [Contributors](#contributors)

## Project Scheme
### Project Objectives
The main objective of this project is to understand the fundamentals of determining the electricity consumption of a building through the development of a prototype.

### Arduino Prototype Components
#### Materials
- Arduino UNO
- Breadboard
- LED Lights
- Solid Wires
- Resistors (220, 1000, 10000)
- Power Source (laptop)
- Adaptor

#### Software Components
- Arduino C++
- Arduino IDE

### Program (Python) Components
#### Python Version
- 3.10.5

#### Libraries
- Pyserial
- Matplotlib
- Kivy
- MySQL

#### Compiler
- Visual Studio Code

## Installation
This program was made possible through Python 3.10.5. To install Python, visit the [Python website](https://www.python.org/) and follow the installation instructions.

To create a virtual environment, follow these steps:

1. Navigate to the directory where you want to create the virtual environment using the `cd` command.
2. Run the following command to create the virtual environment named "myenv":
    ```
    python3 -m venv myenv
    ```
3. Activate the virtual environment. On macOS/Linux, run:
    ```
    source myenv/bin/activate
    ```
   On Windows, run:
    ```
    myenv\Scripts\activate
    ```

By creating a virtual environment, you can isolate your Python project's dependencies from the system-wide Python installation.

To install the required libraries, use the following commands:

    pip install kivy
    pip install kivyMD
    pip install pyserial
    pip install mysql
    

To run the real-time plotted graphs, execute the file `matplot.py`. This will show all the axes in a single figure.

To run the axes in each figure individually, run the files `matplot2.py` or `matplot3.py`.

The program itself can be run using the file `main.py`.

## Features
### Live Data Tracker
- The core functionality of the program revolves around real-time data tracking.
- In the prototype, live data from Arduino to Python was made possible through Pyserial.

### Graphical Representations
- This library enables the creation of interactive and visually appealing graphical representations, including line plots, bar charts, scatter plots, and more.
- Users can easily interpret the data through these visualizations, gaining valuable insights into their energy consumption patterns.

### Electrical Unit Conversions
- Users can seamlessly convert various units of electrical measurements such as volts, amps, watts, ohms, and more.
- This functionality eliminates the need for manual calculations and streamlines the analysis process, allowing users to work with different units effortlessly.

### Historical Data
- By accessing and visualizing this historical data, users can track their energy usage patterns, identify trends, and make informed decisions to optimize their energy consumption.

## Contributors
Contributors:
- Abril, Danielle Ziac
- Evangelista, Aeron
- Medina, Carle Francis
- Sumang, Vex Ivan

Instructor:
- Agdon, Fatima Marie

