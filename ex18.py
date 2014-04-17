def printTwo(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
def printTwoAgain(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def printOne(arg1):
	print "arg1: %r" % arg1
def printNone():
	print "I got nothin;."

printTwo("Alisa", "Palson")
printTwoAgain("Alisa", "Palson")
printOne("First!")
printNone()
