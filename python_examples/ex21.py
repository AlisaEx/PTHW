def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with those functions!"

age = add(20, 2)
height = subtract(75, 14)
weight = multiply(15, 10)
iq = divide(300, 2)

print "Age: %d, Height: %d, Weight: %d, IQ %d" % (age, height, weight, iq)

print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "\nCan you do it by hand?"
