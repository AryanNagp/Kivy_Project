import kivy
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
from kivymd.uix.dialog import MDDialog

class P(MDFloatLayout):
    pass
def show_popup():
    show = P()

    popupWindow = Popup(title="Popup window", content=show, size_hint=(None,None), size=(400,400))
    popupWindow.open()

#Tab
class Tab(MDFloatLayout, MDTabsBase):
    content_text = StringProperty("")