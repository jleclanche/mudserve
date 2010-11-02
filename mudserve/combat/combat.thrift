include "combat_types.thrift"
include "../auth/auth_types.thrift"
include "../data/spell/spell_types.thrift"
include "../main.thrift"

/**
 * The Combat service which keeps track of all things related to
 * the actual in-game combat.
 */
service CombatService {
	/**
	 * Cast a spell at a given target.
	 * @param spellId
	 *   The id of the spell, as described in the Spell structure.
	 *
	 * @param targetGuid
	 *   The id of the target, as passed in the Combatant structure.
	 */
	void castSpell(1: auth_types.AuthToken authToken,
	               2: main.guid combatGuid,
				   3: spell_types.SpellID spellId,
				   4: main.guid targetGuid)
	  throws (1: combat_types.CombatException combatException,
	          2: auth_types.MUDAUserException userException,
			  3: auth_types.MUDASystemException systemException),
	
	/**
	 * Retrieves the combat status of a specific fight.
	 * The information set depends on the status of the fight.
	 * @param combatGuid
	 *   The combat's guid. This will allow you to query the
	 *   status of fights you are no longer participating in, but may
	 *   want to receive history about later on.
	 */
	combat_types.CombatStatus getStatus(1: auth_types.AuthToken authToken,
	                       2: main.guid combatGuid)
	  throws (1: combat_types.CombatException combatException,
	          2: auth_types.MUDAUserException userException,
			  3: auth_types.MUDASystemException systemException)
}
