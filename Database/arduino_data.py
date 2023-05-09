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
    line = ser.readline().decode().strip()  # Read a line of data from the serial port
    Electric_consumption = line
    now = datetime.now()
    cursor = db.cursor()
    query = "INSERT into data (date, time, Electric_consumption) VALUES (%s, %s, %s)"
    values = (now.date(), now.time(), Electric_consumption)
    cursor.execute(query, values)

    # Fetch all rows
    query = "SELECT * FROM data"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        date_str = row[0].strftime('%Y-%m-%d')
        time_str = (datetime.min + row[1]).time().strftime('%H:%M:%S')
        electric_consumption = row[2]
        status = row[3]

        print(f"Date: {date_str}, Time: {time_str}, Electric Consumption: {electric_consumption}, Status: {status}")

    db.commit()
    cursor.close()