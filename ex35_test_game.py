from sys import exit

def start(score):
    print "You awake in a white room with no doors or windows."
    print "To your left you see a chair."
    print "Next to the chair, a cat is purring contently."
    print "1. Pet the Cat."
    print "2. Sit in the Chair."
    next = raw_input("> ")

    if next == "1":
	score += 1
        pet_cat(score)
    elif next == "2":
        sit_chair(score)
    else:
        dead("You stand there staring at the cat and chair.", score)


def pet_cat(score):
    while True:
        print "You reach down to pet the cat on it's..."
    
        next = raw_input("> ")
    
        if next.lower() == "head" or next.lower() == "neck":
            score += 1
            print "*purr purr purr*"
        elif next.lower() == "belly":
            dead("The cat scratches your face off.", score)
        else:
            print "I don't know if that is legal o.O"


def sit_chair(score):
    dead("The chair is incredibly comfortable.\nThe longer you sit in it,\nthe more your desire to get up is diminsihed.", score)


def dead(why, score):
    print why, "You're dead.\nGame Over."
    print "You scored %d out of 300 points!" % score
    exit(0)

start(0)
