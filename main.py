from kivy.app import App
from kivy.uix.widget import Widget

class BitBossGame(Widget):
    print("hello world")

class BitBoss(App):
    def build(self):
        return BitBossGame()

if __name__ == '__main__':
    BitBoss().run()