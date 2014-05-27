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
            next_scene_name = current_scene.enter()
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
