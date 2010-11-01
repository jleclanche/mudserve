from ..mudrpc.character import CharacterService
from ..mudrpc.character.ttypes import *

class CharacterHandler(object):
	def __init__(self):
		self.characters = []
	
	def ping(self):
		print "ping()"
	
	def createCharacter(self, name):
		char = Character(id=(1 + len(self.characters)), name=name)
		self.characters.append(char)
		return char
	
	def getCharacters(self):
		return self.characters
