import kivy
from kivy.app import App
from kivy.uix.label import Label

class BonjourApp(App):
    def build(self):
        # Créez un widget Label avec le texte "Bonjour"
        label = Label(text="Bonjour Henri", font_size=40)
        return label

if __name__ == "__main__":
    BonjourApp().run()
