from sys import argv
script, fromFile, toFile = argv
inData = open(fromFile).read()
outFile = open(toFile, "w").write(inData)
