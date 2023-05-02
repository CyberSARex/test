from kivy.app import App
from kivy.uix.button import Button # button
from kivy.uix.label import Label # label
from kivy.uix.boxlayout import BoxLayout # layout (it's a widget too!)
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # the name of the screen must be passed to the constructor of the Screen class
        btn = Button(text="Switch to another screen")
        btn.on_press = self.next
        self.add_widget(btn) # screen is a widget on which all others (descendants) can be created

    def next(self):
        self.manager.transition.direction = 'left' # the Screen object has a "manager" property
                                                   # - is a link to the parent
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text="Come back, come back!")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyApp(App):
 
   def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        return sm

app = MyApp()
app.run()
