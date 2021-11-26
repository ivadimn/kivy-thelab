from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text = "A")
        b2 = Button(text = "B")
        self.add_widget(b1)
        self.add_widget(b2)


class MainWidget(Widget):
    pass


class TheLabApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    TheLabApp().run()


