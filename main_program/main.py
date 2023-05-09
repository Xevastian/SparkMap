from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import escape_markup
import webbrowser
from kivy.uix.label import Label
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')

class MainScreen(Screen):
    def login_pressed(self):
        print('Login button is pressed')

    def hsb_pressed(self):
        print('Historical Data button is pressed')

    def credits_pressed(self):
        print('Credits button is pressed')

    def learnmore_pressed(self):
        print('LearnMore button is pressed')

    def contactus_pressed(self):
        print('LearnMore button is pressed')

    def sdg_pressed(self):
        print('SDG button is pressed')

    def login_pressed(self):
        print('Login button is pressed')

    def credits_pressed(self):
        print('Credits button is pressed')

    def learnmore_pressed(self):
        print('LearnMore button is pressed')

    def contactus_pressed(self):
        print('Contact Us button is pressed')

    def volts_pressed(self):
        print('Volts button is pressed')

    def watts_pressed(self):
        print('Watts button is pressed')

    def kilowatts_pressed(self):
        print('Kilowatts button is pressed')

    def amperes_pressed(self):
        print('Amperes button is pressed')

    def milliamperes_pressed(self):
        print('Miliamperes button is pressed')

    def kiloamperes_pressed(self):
        print('Kiloamperes  button is pressed')

    def megaamperes_pressed(self):
        print('Megaamperes button is pressed')

    def frequency_pressed(self):
        print('Frequency  button is pressed')


class OtherScreen1(Screen):
    def hsb_pressed(self):
        print('Historical Data button is pressed')

    def login_pressed(self):
        print('Login button is pressed')

    def credits_pressed(self):
        print('Credits button is pressed')

    def learnmore_pressed(self):
        print('LearnMore button is pressed')

    def contactus_pressed(self):
        print('LearnMore button is pressed')

    def sdg_pressed(self):
        print('SDG button is pressed')

    def login_pressed(self):
        print('Login button is pressed')

    def credits_pressed(self):
        print('Credits button is pressed')

    def learnmore_pressed(self):
        print('LearnMore button is pressed')

    def contactus_pressed(self):
        print('Contact Us button is pressed')

    def volts_pressed(self):
        print('Volts button is pressed')

    def watts_pressed(self):
        print('Watts button is pressed')

    def ohms_pressed(self):
        print('OHMS button is pressed')

    def amperes_pressed(self):
        print('Amperes button is pressed')

    def ceafa_pressed(self):
        print('CEAFA button is pressed')

    def aces_pressed(self):
        print('Aces  button is pressed')

    def cics_pressed(self):
        print('CICS button is pressed')

    def cit_pressed(self):
        print('CIT  button is pressed')

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
        return sm
 
if __name__ == '__main__':
    MyApp().run()