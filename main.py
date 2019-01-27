from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import *
from kivy.properties import ObjectProperty, StringProperty
from puzzles import *
from BinaryClass import *

class BitBrainWelcome(Screen):
    pass

class BitBrainGame(Screen):
	# initialize variables for whether tutorials are completed or not
	tutorials_completed = False
	and_completed = False
	or_completed = False
	comp_completed = False

	and_puzzle_1_completed = False
	and_puzzle_2_completed = False
	and_puzzle_3_completed = False
	and_puzzle_4_completed = False

	# AND STUFF
	def and_tutorial_completed(self):
		self.ids.and_button_1.disabled = False
		self.ids.and_button_2.disabled = False
		self.ids.and_button_3.disabled = False
		self.ids.and_button_4.disabled = False

	# OR TUTORIAL STUFF
	def or_tutorial_completed(self):
		self.ids.or_button_1.disabled = False
		self.ids.or_button_2.disabled = False
		self.ids.or_button_3.disabled = False
		self.ids.or_button_4.disabled = False

	# NOT TUTORIAL STUFF
	def comp_tutorial_completed(self):
		self.ids.comp_button_1.disabled = False
		self.ids.comp_button_2.disabled = False
		self.ids.comp_button_3.disabled = False
		self.ids.comp_button_4.disabled = False

	# STUFF
	def tutorials(self):
		tutorials_completed = and_completed and or_completed and comp_completed
		return tutorials_completed

	def update(self):
		tutorials_completed = self.tutorials()

class BitBrainAndTutorial(Screen):
	pass

class BitBrainOrTutorial(Screen):
	pass

class BitBrainCompTutorial(Screen):
	pass

class BitBrainScreenManager(ScreenManager):
	pass

class BitBrainPuzzleFunctions(Screen):
	def displayPuzzleAndOr(puzzleNum):
		# AND / OR
		if puzzleNum == 1:
			input1 = input1a
			input2 = input1b
		elif puzzleNum == 2:
			input1 = input2a
			input2 = input2b
		elif puzzleNum == 3:
			input1 = input3a
			input2 = input3b
		elif puzzleNum == 4:
			input1 = input4a
			input2 = input4b
		return [input1, input2]

	def displayPuzzleComp(puzzleNum):
		# AND / OR
		if puzzleNum == 1:
			input1 = input1a
		elif puzzleNum == 2:
			input1 = input2a
		elif puzzleNum == 3:
			input1 = input3a
		elif puzzleNum == 4:
			input1 = input4a
		return input1

	def check2Input(self, first, second, result, functionNum):
	#determine if correct using and functions for 0, or functions for 1
		if functionNum == 0 and (result.binString == (first.And(second)).binString):
			return True # finishes
		elif functionNum == 1 and (result.binString==(first.Or(second)).binString):
			return True # finishes
		else:
			return False # need to refresh

	# PUZZLE STUFF
		#read user input to var userInput or something
		# CHECKS BINARY VALIDITY
	def checkPuzzle(self, firstInput, secondInput, userInput, functionNum):
		first = Binary(firstInput)
		second = Binary(secondInput)
		result = Binary(userInput)
		if functionNum == 0:
			return self.check2Input(first, second, result, 0)
		else:
			return self.check2Input(first, second, result, 1)

	#checks if ~first == result
	def checkPuzzleNot(self, first, result):

		if (result.binString ==((first.Not()).binString)):
			return True
		else:
			return False

# AND PUZZLES
class BitBrainAndPuzzle1(Screen):
	textinput_text = ""
	inputs = None
	check = None
	text = None

	def display(self):
		self.inputs = BitBrainPuzzleFunctions.displayPuzzleAndOr(1)
		return self.inputs
	
	def check(self):
		self.textinput_text = self.ids.textinput_and1.text
		x = BitBrainPuzzleFunctions()
		check = x.checkPuzzle(self.inputs[0], self.inputs[1], self.textinput_text, 0)
		if check:
			return 0
		else:
			self.ids.textinput_and1.text = ""
			return 1

class BitBrainAndPuzzle2(Screen):
	textinput_text = ""
	inputs = None
	check = None
	text = None

	def display(self):
		self.inputs = BitBrainPuzzleFunctions.displayPuzzleAndOr(2)
		return self.inputs
	
	def check(self):
		self.textinput_text = self.ids.textinput_and2.text
		x = BitBrainPuzzleFunctions()
		check = x.checkPuzzle(self.inputs[0], self.inputs[1], self.textinput_text, 0)
		if check:
			return 0
		else:
			self.ids.textinput_and2.text = ""
			return 1

class BitBrainAndPuzzle3(Screen):
	textinput_text = ""
	inputs = None
	check = None
	text = None

	def display(self):
		self.inputs = BitBrainPuzzleFunctions.displayPuzzleAndOr(3)
		return self.inputs
	
	def check(self):
		self.textinput_text = self.ids.textinput_and3.text
		x = BitBrainPuzzleFunctions()
		check = x.checkPuzzle(self.inputs[0], self.inputs[1], self.textinput_text, 0)
		if check:
			return 0
		else:
			self.ids.textinput_and3.text = ""
			return 1

class BitBrainAndPuzzle4(Screen):
	textinput_text = ""
	inputs = None
	check = None
	text = None

	def display(self):
		self.inputs = BitBrainPuzzleFunctions.displayPuzzleAndOr(4)
		return self.inputs
	
	def check(self):
		self.textinput_text = self.ids.textinput_and4.text
		x = BitBrainPuzzleFunctions()
		check = x.checkPuzzle(self.inputs[0], self.inputs[1], self.textinput_text, 0)
		if check:
			return 0
		else:
			self.ids.textinput_and4.text = ""
			return 1

# OR PUZZLES
class BitBrainOrPuzzle1(Screen):
	textinput_text = ""
	inputs = None
	check = None
	text = None

	def display(self):
		self.inputs = BitBrainPuzzleFunctions.displayPuzzleAndOr(1)
		return self.inputs
	
	def check(self):
		self.textinput_text = self.ids.textinput_or1.text
		x = BitBrainPuzzleFunctions()
		check = x.checkPuzzle(self.inputs[0], self.inputs[1], self.textinput_text, 1)
		if check:
			return 0
		else:
			self.ids.textinput_or1.text = ""
			return 1

class BitBrainOrPuzzle2(Screen):
	textinput_text = ""
	inputs = None
	check = None
	text = None

	def display(self):
		self.inputs = BitBrainPuzzleFunctions.displayPuzzleAndOr(2)
		return self.inputs
	
	def check(self):
		self.textinput_text = self.ids.textinput_or2.text
		x = BitBrainPuzzleFunctions()
		check = x.checkPuzzle(self.inputs[0], self.inputs[1], self.textinput_text, 1)
		if check:
			return 0
		else:
			self.ids.textinput_or2.text = ""
			return 1

class BitBrainOrPuzzle3(Screen):
	textinput_text = ""
	inputs = None
	check = None
	text = None

	def display(self):
		self.inputs = BitBrainPuzzleFunctions.displayPuzzleAndOr(3)
		return self.inputs
	
	def check(self):
		self.textinput_text = self.ids.textinput_or3.text
		x = BitBrainPuzzleFunctions()
		check = x.checkPuzzle(self.inputs[0], self.inputs[1], self.textinput_text, 1)
		if check:
			return 0
		else:
			self.ids.textinput_or3.text = ""
			return 1

class BitBrainOrPuzzle4(Screen):
	textinput_text = ""
	inputs = None
	check = None
	text = None

	def display(self):
		self.inputs = BitBrainPuzzleFunctions.displayPuzzleAndOr(4)
		return self.inputs
	
	def check(self):
		self.textinput_text = self.ids.textinput_or4.text
		x = BitBrainPuzzleFunctions()
		check = x.checkPuzzle(self.inputs[0], self.inputs[1], self.textinput_text, 1)
		if check:
			return 0
		else:
			self.ids.textinput_or4.text = ""
			return 1

class BitBrainCompPuzzle1(Screen):
	textinput_text = ""
	inputs = None
	check = None
	text = None

	def display(self):
		self.inputs = BitBrainPuzzleFunctions.displayPuzzleComp(1) # only one int
		return self.inputs
	
	def check(self):
		self.textinput_text = self.ids.textinput_comp1.text
		x = BitBrainPuzzleFunctions()
		print(self.inputs, self.textinput_text)
		check = x.checkPuzzleNot(Binary(self.inputs), Binary(self.textinput_text))
		if check:
			return 0
		else:
			self.ids.textinput_comp1.text = ""
			return 1

class BitBrainCompPuzzle2(Screen):
	textinput_text = ""
	inputs = None
	check = None
	text = None

	def display(self):
		self.inputs = BitBrainPuzzleFunctions.displayPuzzleComp(2) # only one int
		return self.inputs
	
	def check(self):
		self.textinput_text = self.ids.textinput_comp2.text
		x = BitBrainPuzzleFunctions()
		check = x.checkPuzzleNot(Binary(self.inputs), Binary(self.textinput_text))
		if check:
			return 0
		else:
			self.ids.textinput_comp2.text = ""
			return 1

class BitBrainCompPuzzle3(Screen):
	textinput_text = ""
	inputs = None
	check = None
	text = None

	def display(self):
		self.inputs = BitBrainPuzzleFunctions.displayPuzzleComp(3) # only one int
		return self.inputs
	
	def check(self):
		self.textinput_text = self.ids.textinput_comp3.text
		x = BitBrainPuzzleFunctions()
		check = x.checkPuzzleNot(Binary(self.inputs), Binary(self.textinput_text))
		if check:
			return 0
		else:
			self.ids.textinput_comp3.text = ""
			return 1

class BitBrainCompPuzzle4(Screen):
	textinput_text = ""
	inputs = None
	check = None
	text = None

	def display(self):
		self.inputs = BitBrainPuzzleFunctions.displayPuzzleComp(4) # only one int
		return self.inputs
	
	def check(self):
		self.textinput_text = self.ids.textinput_comp4.text
		x = BitBrainPuzzleFunctions()
		check = x.checkPuzzleNot(Binary(self.inputs), Binary(self.textinput_text))
		if check:
			return 0
		else:
			self.ids.textinput_comp4.text = ""
			return 1

class BitBrain(App):
    def build(self):
    	self.load_kv("bitbrain.kv")
    	return BitBrainScreenManager(transition = WipeTransition())

if __name__ == '__main__':
    BitBrain().run()