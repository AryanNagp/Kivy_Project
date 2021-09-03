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
from kivy_garden.mapview import MapView, MapSource, MapMarker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRoundFlatButton



#Widgets
#Popup
class P(MDFloatLayout):
    pass
def show_popup():
    show = P()

    popupWindow = Popup(title="Popup window", content=show, size_hint=(None,None), size=(400,400))
    popupWindow.open()

#Tab
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

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Laddu2007",
            database = "first_db"
        )
        c = mydb.cursor()

        sql_command = "INSERT INTO login (username,password) VALUES (%s,%s)"
        values = (self.ids.username.text,self.ids.password.text)

        c.execute(sql_command, values)

        mydb.commit()
        mydb.close()
    def show_records(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Laddu2007",
            database = "first_db"
        )
        c = mydb.cursor()
        c.execute("SELECT * FROM customers")
        records = c.fetchall()
        word = ''
        for record in records:
            word = f'{word}\n{record[0]}'
            self.ids.username.text = f'{word}'

        mydb.commit()
        mydb.close()

class Login(Screen):
    dialog = None
    username_login = ObjectProperty(None)
    password_login = ObjectProperty(None)
    def build(self):
        return Login()
    def clear(self):
        self.ids.username.text = ""
        self.ids.password.text = ""

    def validate(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Laddu2007",
            database="first_db"
        )
        c = mydb.cursor()


class SecondPage(Screen):
    age = ObjectProperty(None)
    def build(self):
        return SecondPage()
    def image_changer(self):
        pass
class ThirdPage(Screen):
    def build(self):
        return ThirdPage()

#ERRORS








class WindowManager(ScreenManager):
    pass


#App
class MainApp(MDApp):
    username = ObjectProperty(None)
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Laddu2007",
            database = "first_db"
        )
        c = mydb.cursor()


        return Builder.load_file("login.kv")





sm = WindowManager()
sm.add_widget(SignUp(name='signup'))
sm.add_widget(Login(name='login'))
if __name__ == "__main__":
    MainApp().run()