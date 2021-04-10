from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder

list_build='''
MDScreen:
    ScrollView:
        MDList:
            OneLineRightIconListItem:
                text: "Milk"
                IconRightWidget:
                    icon: "plus-circle"
                    on_release: app.add_milk()

<Content>
    MDTextField:
        hint_text: 'Amount'

'''
class Content(MDBoxLayout):
    pass

class BabyRecorder(MDApp):
    def build(self):
        screen = Builder.load_string(list_build)
        return screen
    
    def add_milk(self):
        self.dialog = MDDialog(title='Feed of milk',type='custom',content_cls=Content())
        self.dialog.open()


BabyRecorder().run()