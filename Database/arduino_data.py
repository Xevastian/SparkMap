import serial
import mysql.connector
from datetime import date, datetime

# Connect to the arduino board via the serial port
ser = serial.Serial("COM9", 9600)

# Connect to the mysql database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="carlemedina",
    database="arduino_data"
)


# Loop to read data from serial port and insert into database
while True:
    # Read data from serial port
    data = ser.readline().decode('utf-8').rstrip()  # Read a line of data from the serial port
    
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
    for row in result:
        date_str = row[0].strftime('%Y-%m-%d')
        time_str = (datetime.min + row[1]).time().strftime('%H:%M:%S')
        overall = row[2]
        aces = row[3]
        cics = row[4]
        ceafad = row[5]
        cit = row[6]

        print(f"Date: {date_str}, Time: {time_str}, Overall: {overall}, ACES: {aces}, CICS: {cics}, CEAFAD: {ceafad}, CIT: {cit}")

    db.commit()
    cursor.close()