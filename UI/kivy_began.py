import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class BeganApp(App):


    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    BeganApp().run()