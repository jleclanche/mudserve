from .spelleffect import SpellEffectHandler

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
