from mudserve.auth.authhandler import AuthHandler
from mudserve.combat.fight import Fight

class CombatHandler(AuthHandler):
	def castSpell(self, authToken, combatGuid, spellId, targetGuid):
		self.validate_token(authToken)
		fight = Fight(combatGuid)
		# TODO: Grab this from authToken
		casterGuid = "player1"
		fight.cast_spell(spellId, casterGuid, targetGuid)
		pass
		# spell = getSpellByID(spell)
		# caster = getCaster()
		# if caster.canCast(spell):
		#  return target.apply(spell)
		# raise CANNOT_CAST_SPELL
		
	def getStatus(self, authToken, combatGuid):
		fight = Fight(combatGuid)
		return fight.get_status()
