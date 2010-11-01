from ..mudrpc.character import Character
from ..mudrpc.character.ttypes import *

class CharacterHandler(object):
    def __init__(self):
        self.characters = []
    def ping(self):
        print "ping()"
    def createCharacter(self, name):
        char = Character(id=1, name=name)
        self.characters.append(char)
        return char
    def getCharacters(self):
        return self.characters