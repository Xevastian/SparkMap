# Import from Arduino
import serial
import mysql.connector
from datetime import datetime, date

# Kivy import   
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.clock import Clock 

ser = serial.Serial("COM9", 9600)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "carlemedina",
    database = "arduino_data"
)

class MainApp(MDApp):
    def build(self):

        # Define Screen
        screen = Screen()
        now = datetime.now()

        # Define Table 
        table = MDDataTable(
            pos_hint = {"center_x": 0.5, "center_y": 0.5}, 
            size_hint = (.9, .6),
            column_data = [
                ("Date", dp(30)),
                ("Time", dp(30)),
                ("Overall", dp(30)),
                ("ACES", dp(30)),
                ("CICS", dp(30)),
                ("CEAFAD", dp(30)),
                ("CIT", dp(30))
            ],

            # INSERT INTO TABLE
            row_data = []
        )

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Add table to screen
        screen.add_widget(table)

        def update_table(self):
            # Read data from serial port
            data = ser.readline().decode("utf-8").rstrip()
            
            # Split data into separate values
            values = data.split(',')

            # Check if there are 5 values (overall, ACES, CICS, CEAFAD, CIT)
            if len(values) == 5:
                Overall, ACES, CICS, CEAFAD, CIT = values

                # Insert data into MySQL database
                cursor = db.cursor()
                now = datetime.now()
                query = "INSERT into data (date, time, Overall, ACES, CICS, CEAFAD, CIT) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (now.date(), now.time(), Overall, ACES, CICS, CEAFAD, CIT)
                cursor.execute(query, val)


                # Fetch all rows
                query = "SELECT * FROM data"
                cursor.execute(query)
                result = cursor.fetchall()

                # Update the table
                row_data = []
                for row in result:
                    date_str = row[0].strftime('%Y-%m-%d')
                    time_str = (datetime.min + row[1]).time().strftime('%H:%M:%S')
                    overall = row[2]
                    aces = row[3]
                    cics = row[4]
                    ceafad = row[5]
                    cit = row[6]

                    row_data.append(f"Date: {date_str}, Time: {time_str}, Overall: {overall}, ACES: {aces}, CICS: {cics}, CEAFAD: {ceafad}, CIT: {cit}")

                table.row_data = row_data

                db.commit()
                cursor.close()

        # Schedule the update function to run every 0.5 seconds
        Clock.schedule_interval(update_table, 0.5)

        return screen 
    
MainApp().run()