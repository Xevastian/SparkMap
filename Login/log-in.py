import re
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import mysql.connector
Window.size = (310, 580)


class Slope(MDApp):
    # for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    db = mysql.connector.Connect(
        host = "localhost",
        user = "root",
        password = "carlemedina",
        database = "login"
    )

    cursor = db.cursor()

    def build (self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager
    
    # LOGIN
    def send_data(self, email, password):
        # Function to send data from python to mysql
        if re.fullmatch(self.regex, email.text):
            self.cursor.execute(f"INSERT INTO user values ('{email.text}', '{password.text}')")
            self.db.commit() # insert query into database 
            email.text = ""
            password.text = ""

    def receive_data(self, email, password):
        # Function to receive data from mysql to python and validate it with textfield text
        self.cursor.execute("SELECT * FROM user")
        email_list = []
        for i in self.cursor.fetchall():
            email_list.append(i[0])
        if email.text in email_list and email.text != "":
            self.cursor.execute(f"SELECT password from user WHERE email='{email.text}'")
            for j in self.cursor:
                if password.text == j[0]:
                    print("You have Successfully Logged In")
                else:
                    print("Incorrect Password")
        else:
            print("Incorrect Email")



if __name__ == "__main__":
    Slope().run()