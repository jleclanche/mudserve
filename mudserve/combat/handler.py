from mudserve.auth.authhandler import AuthHandler
class CombatHandler(AuthHandler):
	def __init__(self):
		self.teams = []
	
	def castSpell(self, authToken, combatGuid, spellId, targetGuid):
		self.validate_token(authToken)
		pass
		# spell = getSpellByID(spell)
		# caster = getCaster()
		# if caster.canCast(spell):
		#  return target.apply(spell)
		# raise CANNOT_CAST_SPELL
