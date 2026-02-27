import random
import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.08, 0.08, 0.12, 1)

PASSWORD = "1234"
signals_given = 0


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=30, spacing=20, **kwargs)

        self.add_widget(Label(text="SIGNAL APP", font_size=28))

        self.password_input = TextInput(
            hint_text="Enter Password",
            password=True,
            multiline=False,
            size_hint=(1, 0.2)
        )
        self.add_widget(self.password_input)

        login_btn = Button(text="LOGIN", size_hint=(1, 0.3))
        login_btn.bind(on_press=self.check_password)
        self.add_widget(login_btn)

        self.message = Label(text="")
        self.add_widget(self.message)

    def check_password(self, instance):
        if self.password_input.text == PASSWORD:
            self.clear_widgets()
            self.add_widget(MainScreen())
        else:
            self.message.text = "Wrong Password"


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)

        self.title = Label(text="Strong Signal Generator", font_size=22)
        self.add_widget(self.title)

        self.signal_label = Label(text="Press button to generate signal")
        self.add_widget(self.signal_label)

        self.button = Button(text="GET SIGNAL", size_hint=(1, 0.3))
        self.button.bind(on_press=self.generate_signal)
        self.add_widget(self.button)

    def generate_signal(self, instance):
        global signals_given

        if signals_given >= 15:
            self.signal_label.text = "Daily limit reached"
            return

        pair = random.choice(["EUR/USD", "GBP/USD", "USD/JPY"])
        direction = random.choice(["CALL", "PUT"])
        timeframe = random.randint(1, 5)
        accuracy = random.randint(88, 96)
        entry_time = (datetime.datetime.now() + datetime.timedelta(seconds=30)).strftime("%H:%M:%S")

        self.signal_label.text = f"""
Pair: {pair}
Direction: {direction}
Timeframe: {timeframe} Min
Enter At: {entry_time}
Accuracy: {accuracy}%
"""
        signals_given += 1


class SignalApp(App):
    def build(self):
        return LoginScreen()


SignalApp().run()
