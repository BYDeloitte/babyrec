# import from kivy
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder

# import from google api
from gutils import GoogleConnector

# import miscellaneous
from datetime import datetime as dt

kv='''
MDScreen:
    MDTextField:
        id: amt
        hint_text: 'Amount'
        size_hint_x: 0.8
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    
    MDRaisedButton:
        text: 'Save'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: app.add_milk(consumed=amt.text)

'''

class BabyRecorder(MDApp):
    gc=GoogleConnector()

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.primary_hue = '200'
        screen = Builder.load_string(kv)
        return screen
    
    def add_milk(self,start=0,end=0,consumed=None):
        consumed="=INDIRECT(ADDRESS(ROW(), COLUMN()-2, 4))-INDIRECT(ADDRESS(ROW(), COLUMN()-1, 4))" if consumed is None else consumed
        now=dt.now()
        data={'values':[[now.strftime("%Y-%m-%d"),now.strftime("%I:%M %p"),start,end,consumed]]}
        try:
            self.gc.add_data('milk',data)
        except Exception as e:
            self.dialog = MDDialog(text=str(e),buttons=[MDFlatButton(text='OK',on_release=self.close_dialog)])
            self.dialog.open()
        
        
    def close_dialog(self,o):
        self.dialog.dismiss()


BabyRecorder().run()