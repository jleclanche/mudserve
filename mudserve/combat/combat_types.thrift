include "../main.thrift"

/**
 * The status of a specific fight. The optional fields set will depend on
 * whether or not the fight is active, i.e. whether or not it is currently
 * happening or has happened in the past.
 *
 * For active fights:
 * - currentTurn
 *     The player guid of the current turn holder.
 * - turnTime
 *     The time remaining on the current turn.
 * - turnId
 *     The id of the current turn (effectively a turn counter).
 *
 * For inactive fights:
 * - winningTeam
 *     The id of the winning team.
 */
struct CombatStatus {
	1: required bool active,
	
	// Fields below are set for active fights
	2: optional main.guid currentTurn,
	3: optional byte turnTime,
	4: optional i16 turnId,
	
	// Fields below are set for inactive fights
	5: optional byte winningTeam
}

/**
 * Various combat error codes.
 * - NOT_YOUR_TURN
 *     You cannot do that because it is not your turn.
 * - INVALID_COMBAT
 *     The combat guid you specified is invalid in the current context.
 * - INVALID_SPELL
 *     Input was a spell you do not have.
 * - UNUSABLE_SPELL
 *     The spell is unusable. The optional parameter may
 *     contain the following reasons:
 *       "cooldown" - The spell is on cooldown
 *       "disabled" - The spell is disabled for some reason
 *       "inactive" - The spell is reactionary and not currently active.
 *       "target"   - The spell may not be used on that target.
 */
enum CombatErrorCode {
	NOT_YOUR_TURN = 1,
	NOT_IN_COMBAT = 2,
	INVALID_SPELL = 3,
	UNUSABLE_SPELL = 4,
}

exception CombatException {
	1: required CombatErrorCode errorCode,
	2: optional string parameter
}
