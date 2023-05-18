# SparkMap 
CS121 - Advanced Computer Programming Project

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
- Adapter

#### Software Components
- Arduino C++
- Arduino IDE

### Program (Python) Components
#### Python version
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

To create a virtual environment, run the following command in your terminal or command prompt:

python3 -m venv myenv


Replace "myenv" with the name you want to give to your virtual environment.

To activate the virtual environment on macOS/Linux, run:

source myenv/bin/activate


On Windows, run:

myenv\Scripts\activate


By creating a virtual environment, you can isolate your Python project's dependencies from the system-wide Python installation.

The required libraries can be installed using pip, which is the standard package manager for Python. If your Python version is 3.4 or later, pip is already bundled with Python. However, if you have an older version, pip may need to be installed separately. It is recommended to upgrade pip to the latest version by running:

pip install --upgrade pip


Once pip is up to date, you can install the required libraries by running the following commands:

pip install kivy
pip install kivyMD
pip install pyserial
pip install mysql


To run the real-time plotted graphs, execute the file `matplot.py`, which shows all the axes in a single figure.

To run the axes in each figure individually, execute the files `matplot2.py` or `matplot3.py`.

The main program can be run by executing the file `main.py`.

## Features
### Live Data Tracker
- The core functionality of the program revolves around real-time data tracking.
- In the prototype, live data from Arduino to Python was made possible through pyserial.

### Graphical Representations
- This library enables the creation of interactive and visually appealing graphical representations, including line plots, bar charts, scatter plots, and more.
- Users can easily interpret the data through these visualizations, gaining valuable insights into their energy consumption patterns.

### Electrical Unit Conversions
- Users can seamlessly convert various units of electrical measurements such as volts, amps, watts, ohms, and more. This functionality eliminates the need for manual calculations and streamlines the analysis process, allowing users to work with different units effortlessly.

Historical Data
By accessing and visualizing historical data, users can track their energy usage patterns, identify trends, and make informed decisions to optimize their energy consumption.
Contributors

Contributors:

Abril, Danielle Ziac
Evangelista, Aeron
Medina, Carle Francis
Sumang, Vex Ivan
Instructor:

Agdon, Fatima Marie
