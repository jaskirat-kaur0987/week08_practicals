from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class simple_app(App):
    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super(simple_app, self).__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        self.phonebook = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Phonebook Demo - Popup & Buttons"
        self.root = Builder.load_file('popup_demo.kv')
        return self.root
