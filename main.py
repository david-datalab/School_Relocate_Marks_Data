from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        def on_text(instance, value):
            print('The widget', instance, 'have:', value)

        textinput = TextInput(multiline=False)
        textinput.bind(text=on_text)

        l1 = Label(text="Enter your marks.")
        # b1 = Button(text="Marks")
        l2 = Label(text="Choose a city or leave blank to show all results.")
        b2 = Button(text="City")
        l3 = Label(text="Choose a district or leave blank to show all results.")
        b3 = Button(text="District")
        b4 = Button(text="Search")
        self.add_widget(l1)
        self.add_widget(textinput)
        # self.add_widget(b1)
        self.add_widget(l2)
        self.add_widget(b2)
        self.add_widget(l3)
        self.add_widget(b3)
        self.add_widget(b4)


class TheLabApp(App):
    pass


TheLabApp().run()
