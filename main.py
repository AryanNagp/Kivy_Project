import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
#Import layouts
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.gridlayout import GridLayout
#TI
from kivy.uix.textinput import TextInput
#Kivy to Python
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
#Tabs
from kivymd.uix.tab import MDTabsBase
from kivy.uix.tabbedpanel import TabbedPanel
#Icons
from kivymd.icon_definitions import md_icons
from kivy.config import Config
#Accessories
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import mysql.connector
from kivy_garden.mapview import MapView, MapSource, MapMarker, MapMarkerPopup
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRoundFlatButton
from kivy_garden.mapview import MapSource
from kivy.uix.widget import Widget
#Database
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://Aryan_Nagpal:Laddu2007@kivymongodatabase.ofb48.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["KivyMongoDatabase"]
collection = db["Login"]



class P(MDFloatLayout):
    pass

def show_popup():
    show = P()

    popupWindow = Popup(title="Popup window", content=show, size_hint=(None, None), size=(400, 400))
    popupWindow.open()

# Tab
class Tab(MDFloatLayout, MDTabsBase):
    content_text = StringProperty("")



#ScreenManager
class SignUp(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    def build(self):
        return SignUp()
    def clear(self):
        self.ids.username.text = ""
        self.ids.password.text = ""
    def submit(self):
        post = {"Name": self.ids.username.text, "Password": self.ids.password.textA}
        collection.insert_one(post)


class Login(Screen):
    dialog = None
    username_login = ObjectProperty(None)
    password_login = ObjectProperty(None)
    def clear(self):
        self.ids.username_login.text = ""
        self.ids.password_login.text = ""

class SecondPage(Screen):
    age = ObjectProperty(None)
class ThirdPage(Screen):
    pass
class WindowManager(ScreenManager):
    pass


#App
class MainApp(MDApp):
    username = ObjectProperty(None)
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"


        return Builder.load_file("login.kv")





sm = WindowManager()
sm.add_widget(SignUp(name='signup'))
sm.add_widget(Login(name='login'))
if __name__ == "__main__":
    MainApp().run()