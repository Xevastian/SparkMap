import mysql.connector
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Connecting to MySql database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="carlemedina",
    database="arduino_data"
)

mycursor = mydb.cursor()

# Define a kivy to display the data
class ArduinoDataApp(App):
    def build(self):
        # Box layout for the GUI 
        layout = BoxLayout(orientation="vertical")

        # Label for the data
        label = Label(text="Arduino Data")
        layout.add_widget(label)

        # Query the database and display the data in the label
        mycursor.execute("SELECT * FROM data")
        for row in mycursor:
            time, value = row
            label.text += "\nTime: {}, Value: {}".format(time,value)

        return layout
    
# run the kivy app
if __name__ == "__main__":
    ArduinoDataApp().run()