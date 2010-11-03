from mudserve import cache
from mudserve.serialize import Serializer
from mudserve.spell.spelleffect import SpellEffectHandler
from mudserve.mudrpc.spell.database.ttypes import SpellDatabase

class SpellHandler(object):
	def __init__(self, spell):
		self.spell = spell
	
	def can_use(self, player, target):
		# TODO: Fix this 
		return True
	
	def execute(self, player, target):
		for effect in self.spell.effects:
			handler = SpellEffectHandler(effect)
			handler.execute(player, target)

class SpellDatabaseHandler(object):
	@classmethod
	def get_spell(cls, spellId):
		db = cache.get_memory_file(SpellDatabase, "spell/spell.db")
		# We use 0-indexed spells in memory but like our spellId's to start at 1.
		obj = db.spells[spellId-1]
		return SpellHandler(obj)
