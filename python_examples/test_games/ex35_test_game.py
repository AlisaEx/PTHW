from sys import exit

def start(score):
    print "You awake in a white room with no doors."
    print "On your left you see a chair, with a cat purring contently on it."
    print "To your right you see a window with curtains obscuing the view."
    print "Do you go left or right?"
    next = raw_input("> ")

    if next == "left":
        check_chair(score)
    elif next == "right":
        open_window(score)
    else:
        dead("You stand there staring at nothing.", score)

def check_chair(score):
    print "That cat looks really cute sleeping on the chair."
    print "Will you move the cat or pet it?"
    next = raw_input("> ")

    if next == "move cat":
        print "The cat begruginly moves from it's spot on the chair."
        score -= 100
        sit_chair(score)
    elif next == "pet cat":
        score += 10
        pet_cat(score)
    else:
        dead("Bro, what are you even doing?", score)



def pet_cat(score):
    while True:
        print "You reach down to pet the cat on it's..."
    
        next = raw_input("> ")
    
        if next.lower() == "head" or next.lower() == "neck":
            score *= 2
            print "*purr purr purr*"
        elif next.lower() == "belly":
            dead("The cat scratches your face off.", score-5)
        else:
            print "I don't know if that is legal o.O"


def sit_chair(score):
    print "The chair is callling you in with it's comfort."
    
    next = raw_input ("> ")
    if next == "sit in the chair":
        dead("The chair is incredibly comfortable.\nThe longer you sit in it,\nthe more your desire to get up is diminsihed.", score)
    else:
        dead("You stand there staring at the chair until you suddenly explode", score)

def open_window(score):
    print "Outside, there is a wonderful breeze\nAnd the sun shining brightly overhead\nCasting a warm glow on the room."
    next = raw_input("> ")
    if next == "open window":
        


def dead(why, score):
    print why, "You're dead.\nGame Over."
    print "You scored %d out of 9001 points!" % score
    exit(0)

start(0)
