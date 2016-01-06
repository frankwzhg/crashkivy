from kivy.app import App
import webbrowser
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from arithmetic import Arithmetic
from kivy.properties import ObjectProperty
import random

class KivyTutoRoot(BoxLayout):
    math_screen = ObjectProperty(None)

    def __init__(self,**kwargs):
        super(KivyTutoRoot, self).__init__(**kwargs)
        #List of previous screens
        self.screen_list = []
        self.is_mix = False

    def ChangeScreen(self, next_screen):
        operations = "addition subtraction multiplication division".split()
        question = None
        if self.ids.kivy_screen_manager.current not in self.screen_list:
            self.screen_list.append(self.ids.kivy_screen_manager.current)
        if next_screen == "about this app":
            self.ids.kivy_screen_manager.current = "about_screen"
        else:
            print next_screen
            if next_screen == "mix":
                self.is_mix = True
                index = random.randint(0, len(operations)-1)
                next_screen = operations[index]
                print next_screen
            else:
                self.is_mix = False
            for operation in operations:
                if next_screen == operation:
                    print "test1"
                    question = "self.math_screen.get_{}_question()".format(operation)
            self.math_screen.question_text.text = KivyTutoRoot.prepQuestion(
                eval(question) if question is not None else None
            )
            self.ids.kivy_screen_manager.current = "math_screen"
    @staticmethod
    def prepQuestion(question):
        if question is None:
            return "ERROR"
        text_list = question.split()
        text_list.insert(2, "[b]")
        text_list.insert(len(text_list), "[/b]")
        return " ".join(text_list)

    def onBackBtn(self):
        # check if there are any screen to go back
        if self.screen_list:
            # if there are screen we can go back to , the just do it
            self.ids.kivy_screen_manager.current = self.screen_list.pop()
            # saw we  don't want to close
            return True
        # no more screen to go back to
        return False

class MathScreen(Screen, Arithmetic):
    #widget that will act as a screen and hold funcs for maths questions
    def __init__(self, *args, **kwargs):
        super(MathScreen, self).__init__(*args, **kwargs)

class MyfirstApp(App):
    def __init__(self, **kwargs):
        super(MyfirstApp, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.onBackBtn)

    def onBackBtn(self, window, key, *args):
        # user press back button
        if key == 27:
            return self.root.onBackBtn()

    def build(self):
        return KivyTutoRoot()

    def getText(self):
        return ("Hey there!\nThis App was built using"
                "[b][ref=kivy]kivy[/ref][/b]\n"
                "Feel free to look at the source code"
                "[b][ref=source]here[/ref][/b].\n"
                "This app is underthe [b][ref=mit]MIT License[/ref][/b]\n"
                "My site: [b][ref=website]PyGopar.com[/ref][/b]")

    def on_ref_press(self, instance, ref):
        _dict = {
            "source": "https://github.com/gopar/kivy-Tutor",
            "website": "https://www.pygopar.com",
            "kivy": "http://kivy.org/#home",
            "mit": "https://github.com/gopar/kivy-Tutor/blod/master/LICENSE"
        }
        webbrowser.open(_dict[ref])



if __name__ == "__main__":
    MyfirstApp().run()