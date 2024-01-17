from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

class Matriz(App):
    def build(self):
        return Button(text="Olá",
                      )

Matriz().run()