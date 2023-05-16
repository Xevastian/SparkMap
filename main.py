from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import escape_markup
import webbrowser
import serial
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')

# Arduino communication
arduino = serial.Serial('com3', 9600)  # Replace with your Arduino port


class ImageButton(ButtonBehavior, Image):
    pass


class MainScreen(Screen):

    
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.button_data = [0, 0, 0, 0]  # Initialize with default data for each button

    def on_enter(self):
        self.update_button_images()  # Update button images when entering the screen
        self.start_timer()  # Start the timer to periodically update the button images

    def on_leave(self):
        self.stop_timer()  # Stop the timer when leaving the screen

    def update_button_images(self):
        # Update button images based on button data
        aces = self.button_data[0]
        cics = self.button_data[1]
        ceafad = self.button_data[2]
        cit = self.button_data[3]

        # Update ACES button image
        button_aces = self.ids['button_aces']
        if aces == 1:
            button_aces.source = 'images/BLUE_ACES.png'
        elif aces == 2:
            button_aces.source = 'images/GREEN_ACES.png'
        elif aces == 3:
            button_aces.source = 'images/RED_ACES.png'
        else:
            button_aces.source = 'images/DEF_ACES.png'

        # Update CICS button image
        button_cics = self.ids['button_cics']
        if cics == 1:
            button_cics.source = 'images/BLUE_CICS.png'
        elif cics == 2:
            button_cics.source = 'images/GREEN_CICS.png'
        elif cics == 3:
            button_cics.source = 'images/RED_CICS.png'
        else:
            button_cics.source = 'images/DEF_CICS.png'

        # Update CEAFA button image
        button_ceafa = self.ids['button_ceafa']
        if ceafad == 1:
            button_ceafa.source = 'images/BLUE_CEAFA.png'
        elif ceafad == 2:
            button_ceafa.source = 'images/GREEN_CEAFA.png'
        elif ceafad == 3:
            button_ceafa.source = 'images/RED_CEAFA.png'
        else:
            button_ceafa.source = 'images/DEF_CEAFA.png'

        # Update CIT button image
        button_cit = self.ids['button_cit']
        if cit == 1:
            button_cit.source = 'images/BLUE_CIT.png'
        elif cit == 2:
            button_cit.source = 'images/GREEN_CIT.png'
        elif cit == 3:
            button_cit.source = 'images/RED_CIT.png'
        else:
            button_cit.source = 'images/DEF_CIT.png'

    def start_timer(self):
        self.timer = Clock.schedule_interval(self.update_arduino_data, 0.001)  # Update every second

    def stop_timer(self):
        self.timer.cancel()  # Stop the timer

    def update_arduino_data(self, dt):
        if arduino.in_waiting:
            arduino_data = arduino.readline().decode().strip().split(',')
            button_data = [int(value) for value in arduino_data[1:5]]  # Extract values for buttons

         # Update button images based on the new Arduino data
            if button_data[0] == 1:
                self.ids.button_aces.source = 'images/BLUE_ACES.png'
            elif button_data[0] == 2:
                self.ids.button_aces.source = 'images/GREEN_AcES.png'
            elif button_data[0] == 3:
                self.ids.button_aces.source = 'images/RED_ACES.png'
            else:
                self.ids.button_aces.source = 'images/DEF_ACES.png'

            if button_data[1] == 1:
                self.ids.button_cics.source = 'images/BLUE_CICS.png'
            elif button_data[1] == 2:
                self.ids.button_cics.source = 'images/GREEN_CICS.png'
            elif button_data[1] == 3:
                self.ids.button_cics.source = 'images/RED_CICS.png'
            else:
                self.ids.button_cics.source = 'images/DEF_CICS.png'

            if button_data[2] == 1:
                self.ids.button_ceafa.source = 'images/BLUE_CEAFA.png'
            elif button_data[2] == 2:
                self.ids.button_ceafa.source = 'images/GREEN_CEAFA.png'
            elif button_data[2] == 3:
                self.ids.button_ceafa.source = 'images/testceafa.png'
            else:
                self.ids.button_ceafa.source = 'images/DEF_CEAFA.png'

            if button_data[3] == 1:
                self.ids.button_cit.source = 'images/BLUE_CIT.png'
            elif button_data[3] == 2:
                self.ids.button_cit.source = 'images/GREEN_CIT.png'
            elif button_data[3] == 3:
                self.ids.button_cit.source = 'images/RED_CIT.png'
            else:
                self.ids.button_cit.source = 'images/DEF_CIT.png'

    def bceafa_pressed(self):
        print('CEAFA BUILDING button is pressed')

class OtherScreen1(Screen):

    def voltsS_pressed(self):
        print('Volts button is pressed')

    def watts_pressed(self):
        print('Watts button is pressed')

    def ohms_pressed(self):
        print('OHMS button is pressed')
    
    def amperes_pressed(self):
        print('Frequency  button is pressed')

    def ceafa_pressed(self):
        print('Amperes button is pressed')

    def aces_pressed(self):
        print('Miliamperes button is pressed')

    def cics_pressed(self):
        print('Kiloamperes  button is pressed')

    def cit_pressed(self):
        print('Megaamperes button is pressed')

class SDG(Screen):

    def open_link(self):
        webbrowser.open('https://www.un.org/sustainabledevelopment/sustainable-development-goals/')

class LOGIN(Screen):
    pass

class CREDITS(Screen):
    pass

class LEARNMORE(Screen):
    pass

class CU(Screen):
    pass

class HSD(Screen):
    pass

class LIVEDATA(Screen):
    pass

Builder.load_file('my.kv')

class ScreenManagement(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='mainscreen'))
        sm.add_widget(OtherScreen1(name='otherscreen1'))
        sm.add_widget(SDG(name='sdg'))
        sm.add_widget(LOGIN(name='login'))
        sm.add_widget(CREDITS(name='credits'))
        sm.add_widget(LEARNMORE(name='learnmore'))
        sm.add_widget(CU(name='contactus'))
        sm.add_widget(HSD(name='HS'))
        sm.add_widget(LIVEDATA(name='LD'))
        return sm
 
if __name__ == '__main__':
    MyApp().run()