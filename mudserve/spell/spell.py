from mudserve import cache
from mudserve.serialize import Serializer
from mudserve.database.objects import DatabaseObjectHandler
from mudserve.spell.spelleffect import SpellEffectHandler
from mudserve.mudrpc.spell.types.ttypes import Spell

class SpellHandler(DatabaseObjectHandler):
	def __init__(self, spell):
		self.spell = spell
	
	def can_use(self, player, target):
		# TODO: Fix this 
		return True
	
	def execute(self, player, target):
		for effect in self.spell.effects:
			handler = SpellEffectHandler(effect)
			handler.execute(player, target)
			
	@classmethod
	def from_python(cls, data):
		obj = Spell()
		obj.id = data['id']
		obj.name = data['name']
		obj.effects = []
		for effect in data['effects']:
			obj.effects.append(SpellEffectHandler.from_python(effect))
		return obj
