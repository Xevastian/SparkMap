# SparkMap 
CS121[Advance Computer Programing] Project

# Introduction
  Welcome to the project that offers electricity tools and resources. 
  The team is dedicated to creating an electricity consumption map for Batangas State University and The National Engineering University – Alangilan Campus. 
  By monitoring consumption and promoting sustainable practices, they aim to minimize waste and improve efficiency. 
  This initiative aligns with Sustainable Development Goal 12, emphasizing the importance of sustainable consumption and production patterns. 
  Through their prototype, the team aims to understand building electricity consumption, enabling informed decisions and contributing to a sustainable future. 
  Join them on this journey towards responsible electricity consumption for a brighter future.

## Table of Contents
  - [Project Scheme](#1)
  - [Installation](#2)
  - [Features](#3)
  - [Contributors](#4)

### Project Scheme {#1}
  Project Objectives:
    The main objective of this project is to understand the fundamentals of determining the electricity consumption of a building through the development of a prototype.
    
  Arduino Prototype Components:
      Materials:
        - Arduino UNO
        - Breadboard
        - LED Lights
        - Solid Wires
        - Resistors (220,1000,10000)
        - Power Source (laptop)
        - Adaptor
        
      Software Components:
        - Arduino C++
        - Arduino IDE
      
   Program (Python) Components:
     Python version: 
        - 3.10.5
        
     Libraries:
        - Pyserial
        - Matplotlib
        - Kivy
        - MySQL
        
      Compiler:
        - Visual Studio Code

### Installation {#2}
  This program wwas made possible through Python 3.10.5.
  To install this, go to https://www.python.org/ and follow the installation instructions
  
  Run the following command to create a virtual environment:
  Navigate to the directory where you want to create the virtual environment. 
  You can use the cd command to change directories.
  Then run:
      python3 -m venv myenv
  whereas "myenv" is the name of your virtual environment.
  
  To activate on macOS/Linux, run:
     source myenv/bin/activate
  
  Onwindows, run:
      myenv\Scripts\activate
    
  By creating a virtual environment, you can isolate your Python project's dependencies from the system-wide Python installation. 
  
  The libraries used was then installed through the standard manager for Python. 
  Pip is bundled with Python starting from Python 3.4 and later versions. For older versions of Python, pip may need to be installed separately. 
  It is highly recommended to upgrade pip to the latest version using: 
      pip install --upgrade pip 
  to ensure you have the most recent features and bug fixes.
  
   The libraries can now be installed with:
      pip install kivy
      pip install kivyMD
      pip install pyserial
      pip install mysql
      
  To run the real-time plotted graphs, run the file: matplot.py
  This shows all the axis in a single figure. 
  
  To run the axis in each figures, run the files: matplot2.py or matplot3.py
  
  The program itself can be run through the file: main.py

### Features {#3}
  Live Data Tracker
  - The core functionality of the program revolves around real-time data tracking. 
  - In the protoype, live data from arduino to python was made possible through pyserial. 

  Graphical Representations
  - This library enables the creation of interactive and visually appealing graphical representations, including line plots, bar charts, scatter plots, and more. 
  - Users can easily interpret the data through these visualizations, gaining valuable insights into their energy consumption patterns.
  
  Electrical Unit Conversions
  - Users can seamlessly convert various units of electrical measurements such as volts, amps, watts, ohms, and more. 
  - This functionality eliminates the need for manual calculations and streamlines the analysis process, allowing users to work with different units effortlessly.  
  
  Historical Data
  - By accessing and visualizing this historical data, users can track their energy usage patterns, identify trends, and make informed decisions to optimize their energy consumption.
  
### Contributors {#4}

  Contributors:
    - Abril, Danielle Ziac 
    - Evangelista, Aeron
    - Medina, Carle Francis
    - Sumang, Vex Ivan

  Instructor:
    - Agdon, Fatima Marie 
