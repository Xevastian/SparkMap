from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from datetime import date, datetime

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
                ("Electricity Cconsumption", dp(30)),
                ("Status", dp(30))
            ],
            # INSERT INTO TABLE
            row_data = [
                (now.date(), now.time(), "Null", "Null"),
            ]
        )

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        # return Builder.laod_file("test.kv")

        # Add table to screen
        screen.add_widget(table)

        return screen 
    
MainApp().run()