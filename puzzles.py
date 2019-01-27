from BinaryClass import *
#puzzles consist of input1, which is given to the user, 
#and either the result or the second input, the other the user must figure out
#easy puzzles give user both inputs
#medium puzzles make user figure out input2

#easy and/or/not puzzles (input1 and input2 are given)
input1a = "1010"
input1b = "1100"
input2a = "1110"
input2b = "0111"
input3a = "1111"
input3b = "1001"
input4a = "0000"
input4b = "1010"

#medium and/not puzzles (input1 and result are given)
input5 = "1010"
result5 = "0010"
input6 = "1100"
result6 = "0100"
input7 = "1111"
result7 = "0100"
input8 = "0010"
result8 = "0010"

#medium or puzzles (input1 and result are given)
#these must be different from and because only some results are possible with given inputs
input5o = "1010"
result5o = "1010"
input6o = "1100"
result6o = "1100"
input7o = "1111"
result7o = "1111"
input8o = "0010"
result8o = "0110"


#for simplicity, AND and ORs have the same given info
easyAndOrPuzzles = [(input1a, input1b), (input2a, input2b), (input3a, input3b), (input4a, input4b)]
mediumAndPuzzles = [(input5, result5), (input6, result6), (input7, result7), (input8, result8)] 
mediumOrPuzzles = [(input5o, result5o), (input6o, result6o), (input7o, result7o), (input8o, result8o)]
easyNotPuzzles = [input1a, input2a, input3a, input4a]
mediumNotPuzzles = [input5, input6, input7, input8]


#takes in inputs as Binary objects
def check2Input(first, second, result, functionNum):
	#determine if correct using and functions for 0, or functions for 1
		if functionNum ==0 && (result.binString==(first.AND(second)).binString):
			unlock next level
		elif functionNum ==1 && (result.binString==(first.OR(second)).binString):
			unlock next level
		else:
			refresh screen??

#checks if ~first == result
def check1Input(first, result):
		if (result.binString==((first.NOT()).binString)):
			unlock next level
		else:
			refresh screen??

#won't work for not because not only ever has 1 input
#functionNum = 0 for and, 1 for or
#difficulty = 0 for easy, 1 for medium
def showPuzzle((firstInput, secondInput), functionNum, difficulty):
	#do some GUI stuff to diplay the puzzle
		#need to display firstInput of type string on one line (display text)
		#need to display secondInput of type string on one line (display text)
		#need to display empty text box for user's input
	#read user input to var userInput or something
	first = Binary(firstInput)
    if difficulty==0: 	
		second = Binary(secondInput)
		result = Binary(userInput)
	else
	    second = Binary(userInput)
		result = Binary(secondInput)

	check2Input(first, second, result, functionNum)
	
#difficulty 0 = easy, 1 = medium
def showNot(firstInput):
	#do some GUI stuff to diplay the puzzle
	#read user input
	userInput = read user input
     #here it doesnt really matter the order of these because ~first = result
	first = Binary(firstInput)
	result = Binary(userInput)

	check2Input(first, result)


#function num = 0 for And, 1 for Or so we know which verification function to use
def play():
	#show AND ex1
	for x in easyAndOrPuzzles:
		showPuzzle(x, 0, 0)
		print("Yay, you're one step closer to winning!")
    #show AND ex2
	for x in mediumAndPuzzles:
		showPuzzle(x, 0, 1)
	#show OR ex1
	for x in easyAndOrPuzzles:
		showPuzzle(x, 1, 0)
	#show OR ex2
	for x in mediumOrPuzzles:
		showPuzzle(x, 1, 1)	
	#show NOT ex1
	for x in easyNotPuzzles:
		showNot(x)
	#show NOT ex2
	for x in mediumNotPuzzles:
		showNot(x)
    
	print("You win!")



print("hi")