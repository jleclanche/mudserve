"""
Handles executing spell effects on targets.
This is accomplished by some black magic, mostly to make the registration
of new handlers easier. We create a metaclass that keeps track of all
sub classes and their registered effect codes.
"""

from mudserve.mudrpc.spell.effect.ttypes import SpellEffect, SpellEffectCode

class _SpellEffectMeta(type):
	def __init__(cls, *args):
		super(_SpellEffectMeta, cls).__init__(*args)
		# If the cls._handler attribute does not exist,
		# we're currently handling the SpellEffectHandler
		# base class, so we'll just initialize it without
		# adding the EFFECT_CODE to the dict (since there is none).
		if not hasattr(cls, '_handlers'):
			cls._handlers = {}
		else:
			cls._handlers[cls.EFFECT_CODE] = cls
			
class SpellEffectHandler(object):
	__metaclass__ = _SpellEffectMeta
	
	def __new__(cls, effect):
		"""
		Retrieves a handler given an effect code.
		
		@param effect_code
		  The effect code to retrieve the handler for.
		
		@return
		  An initialized spell effect handler for the given effect code.
		
		@throws KeyError
		  If the handler is not found.
		"""
		
		# Make sure this is the call to SpellEffectHandler and not
		# a subclass, since initialization of the subclass also
		# calls this __new__ method.
		if cls is SpellEffectHandler:
			handler = cls._handlers[effect.effectCode](effect)
			return handler
		else:
			return super(SpellEffectHandler, cls).__new__(cls)
			
	def __init__(self, effect):
		self.effect = effect
	
	def execute(self, caster, target, *args):
		raise NotImplementedError
	
class DamageEffectHandler(SpellEffectHandler):
	EFFECT_CODE = SpellEffectCode.DAMAGE
	
	def execute(self, caster, target):
		target.damage(self.effect.arg1)
