from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()
print "Type the filename again:"
fileAgain = raw_input(">")

txtAgain = open(fileAgain)

print txtAgain.read()
txtAgain.close()
