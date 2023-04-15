from operator import index
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label



#Defining each screens that will be used
class HomeLayout(Screen):
    pass


class ConversionTab(Screen):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f'You selected {value}'

        layout = GridLayout(cols=2)
        # Add widgets
        self.add_widget(Label(text="Input Number"))
        # Add input box
        layout.num = TextInput(multiline=False)
        layout.add_widget(layout.num)


class CalculatorTab(Screen):
    pass


class GraphTab(Screen):
    pass


class HistoryTab(Screen):
    pass


class ErrorTab(Screen):
    pass


class EducationTab(Screen):
    pass


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("home.kv")

class Home(App):
    def build(self):
        return kv


if __name__ == "__main__":
     Home().run()