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



