from mudserve import cache
from mudserve.spell.spell import SpellDatabaseHandler
from mudserve.mudrpc.combat.types.ttypes import CombatStatus
from mudserve.combat.combatant import CombatantHandler

class Fight(object):
	"""
	The abstraction of a specific fight instance. This class will be
	instantiated dynamically from memory any time we want to perform some
	logic during a fight.
	
	NOTE! Only one method may be called for any one instance of the fight class,
	as the methods may mutate the internal state of the class and required
	attributes for other methods may be unset to facilitate speedy transfer
	with other methods.
	"""
	
	def __init__(self, guid):
		# Get the CombatStatus from memory
		self.status = cache.get_struct(CombatStatus, guid)
		if self.status is None:
			# We need to grab the information from the database as this is
			# either an invalid fight or a fight no longer residing in memory
			# because it is not currently occurring.
			raise AssertionError("Fight GUID not found.")
		self.fight_guid = guid
		
	def get_status(self, known_turn=None):
		"""
		Returns a statusupdate of the fight. This may unset some fields if there
		has been no further updates since the last update. This is controlled
		by the known_turn parameter, described below.
		
		@param known_turn
		  Controls how much data to return. If an integer is passed in it is
		  used in order to judge how much data has already been sent to the
		  client. If the known_turn parameter equals the internal current turn,
		  several fields are unset in order to decrease total bandwidth and
		  speed up delivery.
		
		@return
		  Returns the current status of the fight.
		"""
		
		# TODO: Update turnTime according to current time
		
		status = self.status
		if not status.active or status.turnId != known_turn:
			return status
		# Unset fields that are already known
		for field in ("currentTurn", "combatants"):
			setattr(status, field, None)
		return status
	
	def cast_spell(self, spellId, casterGuid, targetGuid):
		"""
		Casts the given spell targetting the given target.
		This function naively assumes that the request is issued by the current
		turn holder; THIS MUST BE VERIFIED WHEN RECEIVING THE REQUEST.
		
		@param spellId
		  The id of the spell to cast.
		
		@param targetGuid
		  The guid of the target to cast the spell on.
		"""
		
		status = self.status
		# TODO: We have to verify that the player 1) has the spell and 2) can cast it
		spell = SpellDatabaseHandler.get_spell(spellId)
		
		# Retrieve the target and caster
		caster_combatant = status.combatants[casterGuid]
		target_combatant = status.combatants[targetGuid]
		caster = CombatantHandler(caster_combatant)
		target = CombatantHandler(target_combatant)
		spell.execute(caster, target)
		
		# Update the turn count and so on
		status.turnId += 1
		# TODO: This needs to correctly retrieve the next turn's player.
		# We'll just use the target of the spell for now.
		status.currentTurn = targetGuid
		self.update_status()
	
	def update_status(self):
		cache.set_struct(CombatStatus, self.fight_guid, self.status)
