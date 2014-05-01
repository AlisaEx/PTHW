myName = 'Alisa J. Palson'
myAge = 22 
myHeight = 61 #inches
myWeight = 150 #pounds
myEyes = 'Green'
myTeeth = 'White'
myHair = 'Brown'

heightInFeet = myHeight / 12

print "Let's talk about %s." % myName
print "She's %d feet and %d inches tall." % (heightInFeet,myHeight%12)
print "She's %d pounds heavy." % myWeight
print "She's loosing weight..."
print "She's got %s eyes and %s hair." % (myEyes, myHair)
print "Her teeth are usually %s depending on the coffee." % myTeeth

print "If I add %d, %d, and %d I get %d." % (myAge, myHeight, myWeight, myAge+myHeight+myWeight)