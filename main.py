from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import *
from kivy.properties import ObjectProperty

class BitBossWelcome(Screen):
    pass

class BitBossGame(Screen):
	# initialize variables for whether tutorials are completed or not
	# tutorials_completed = False
	# and_completed = BitBossAndTutorial.and_tutorial_completed()
	# or_completed = False
	# comp_completed = False

	# initialize variables to reference buttons for enabling/disabling the tutorials
	# and_tutorial = ObjectProperty()
	# or_tutorial = ObjectProperty(Button)
	# not_tutorial = ObjectProperty()

	def and_tutorial_completed(self, instance):
		and_completed = True
		self.ids.or_tutorial.disabled = False

	def or_tutorial_completed(self, instance):
		or_completed = True
		self.ids.comp_tutorial.disabled = False

	def tutorials(self):
		tutorials_completed = and_completed and or_completed and comp_completed
		return tutorials_completed

	def update(self):
		tutorials_completed = self.tutorials()

class BitBossAndTutorial(Screen):
	pass

class BitBossOrTutorial(Screen):
	pass

class BitBossCompTutorial(Screen):
	pass

class BitBossScreenManager(ScreenManager):
	pass

class BitBoss(App):
    def build(self):
    	self.load_kv("bitboss.kv")
    	return BitBossScreenManager(transition = WipeTransition())

if __name__ == '__main__':
    BitBoss().run()