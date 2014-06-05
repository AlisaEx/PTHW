from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        print "Engine __init__ has scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print "Play's first scene", current_scene

        while True:
            print "\n---------"
            next_scene_name = current_scene()
            print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "map returns new scene", current_scene

class Death(Scene):
    quips = [
        "You died. You suck at this.",
        "Your mom would be proud, if you were dead.",
        "Wow. Such Loser. So Fail. Much Death.",
        "Are you even trying?"
    ]
    def enter(self):
        print Death.quips[randint(0, lens(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print """The Gothons of Planet Percal #25 have invaded your ship and destroyed\nyour entire crew. You are the last surviving member and your last\nmission is to get the ceutron destruct bomb from the Weapons Armory,\nput it in the bridge, and blow up the ship after getting into an\nescape pod.\n\nYou're running down the central corridor to the Weapons armory when\na Gothon jumps out, red scaley skin, dark grimy teeth, and evil clown costume\nflowing around his hate filled body. He's blocking the door to the\nArmory and about to pull a weapon to blast you."""

        action = raw_input("> ")

        if action == "shoot!":
            print """Quick on the draw you yank out your blaster and fire it at the Gothon.\nHis clown costume is flowing and mocign his body around, which throws\noff your aim. Your laser hits his costume but misses him entirely. This\ncompletely ruins his brand new costume his mother bought him, which\nmakes him fly into an insane rage and blast you repeatedly in the face until\nyou are dead. Then he eats you."""
            return 'death'
        elif action == "dodge!":
            print """Like a world class boxer, you dodge, weave, slip and slide right\nas the Gothon's blaster cranks a laser past your head.\nIn the middle of your artful dodge your foot slips and you\nbang your head on the metal wall and pass out.\nYou wake up shortly after only to die as a Gothon stomps on\nyour head and eats you."""
            return 'death'
        elif action == "tell a joke":
            print """Lucky for you, they made you learn Gothon insults in the academy.\nYou tell the on Gothon joke you know:"\n\nLbhe zbgure vf fb sng, jura fur fcgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.\n\nThe Gothon stops, tries not to laugh, then bursts out laughing and can't movee.\nWhile he's laughing you run up and shoot him square in the head\nputting him down, then jump through the Weapon Armory door."""
            return 'laser_weapon_armory'
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print """You do a dive roll into the Weapon Armory, crouch and scan the room\nfor more Gothons that might be hiding. It's dead quiet, too quiet.\nYou stand up and run to the far side of the room and find the \nneutron bomb in its container. There's a keypad lock on the box\nand you need the code to get the bomb out. If you get the code wrong 10 times then the lock closes forever and you can't\nget the bomb. The code is 3 digits long."""
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
        if guess == code:
            print """The container clicks open and the seal breaks, letting gas out.\nYou grab the neutron bomb and run as fast as you can to the\nbridge where you must place it in the right spot."""
            return 'the_bridge'
        else:
            print """The lock buzzes one last time and then you hear a sickening\nmelting sound as the mechanism is fused together.\nYou decide to sit there, and finally the Gothons blow up the\nship from their ship and you die."""
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and suprise 5 Gothons who are trying to"
        print "take control of the ship. Each of them has a even unglier"
        print "clown costume than the last. They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print """In a panic you throw the bomb at a group of Gothons\nand make a leap for the door. Right as you drop it a\nGothon shoots you right in the back killing you.\nAs you die you see another Gothon frantically try to disarm\nthe bomb. You die knowing they will probably blow up when\nit goes off."""
            return 'death'

        elif action == "slowly place the bomb":
            print """You point your blaster at the bomb under your arm\nand the Gothons put their hands up and start to sweat.\nYou inch backward to the door, open it, and then carefully\nplace the bomb on the floor, pointing your blaster at it.\nYou then jump back through the door, punch the close button\nand blast the lock so the Gothons can't get out.\nNow that the bomb is placed you run to the escape pod to\nget off this tin can."""
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print """You rush through the ship desperately trying to make it to\nthe escape pod before the whole ship explodes. It seems like\nhardly any Gothons are on the ship, so your run is clear of\ninterference. You get to the chamber with the escape pods, and\nnow need to pick one to take. Some of them could be damaged\nbut you don't have time to look. There's 5 pods, which on\ndo you take?"""

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print """The pod escapes out into the void of space, then]nimplodes as the hull ruptures, crushing your body\ninto jam jelly"""
            return 'death'

        else:
            print "You jump into pdo %s and hit the eject button." % guess
            print """The pod easily slides out into space heading to\ntheplanet below. As it dlies to the planet, you look back and see your ship implode like a\nbright star, taking out the Gothon ship at the same\ntime. You win!"""

            return 'finished'


class Map(object):
    scenes = {
        'central corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "start_scene in __init__", self.start_scene

    def next_scene(self, scene_name):
        print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        print "next_scene returns", val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
