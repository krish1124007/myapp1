from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# engine1 = engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()





class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", spacing=10, padding=5)
        btn = Button(text="click me to see magic",
                     on_release=self.btn_click, )
        btn1 = Button(text="click me to see magic",
                      on_release=self.btn_click1, )
        btn2 = Button(text="click me to see magic",
                      on_release=self.btn_click2,)
        btn3 = Button(text="click me to see magic",
                      on_release=self.btn_click3, )
        layout.add_widget(btn)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout

    def btn_click(self, btn):
        speak("Hello sir I am jarvish How I Can Help You")

    def btn_click1(self, btn):
        speak("this button help toh visist wikideia")

    def btn_click2(self, btn):
        speak("this is a krish button")

    def btn_click3(self, btn):
        speak("jay shree ram")


if __name__ == "__main__":
    MyApp().run()