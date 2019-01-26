#Test file written by Cambrea Earley
#Tests the Binary class functionality

from BinaryClass import *

b1 = Binary("0000")
b2 = Binary("1111")
b3 = Binary("1100")
b4 = Binary("1010")
b5 = Binary("1001")
print(b4.stringInput)
print(b5.binString)

print("Testing And...")
assert((b1.And(b2)).binString == b1.binString)
assert((b2.And(b3)).binString == b3.binString)
assert((b3.And(b4)).binString == ((Binary("1000")).binString))
print("And testing Passed")

print("Testing Or...")
assert((b1.Or(b2)).binString == b2.binString)
assert((b3.Or(b4)).binString == (Binary("1110").binString))
print("Or testing Passed")

print("Testing Not...")
assert(b1.Not().binString == b2.binString)
assert(b4.Not().binString == Binary("0101").binString)
print("Not testing Passed")

print("Testing Xor...")
assert(b1.Xor(b2).binString == b2.binString)
assert(b4.Xor(b5).binString == Binary("0011").binString)
print("Xor Testing Passed")
