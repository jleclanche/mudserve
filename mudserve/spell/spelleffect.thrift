/**
 * The spell effect codes, identifying a specific spell effect type.
 * - DAMAGE
 *     Does damage to a target.
 *     - arg1: Damage amount
 *
 * - More to come
 */
 
enum SpellEffectCode {
	DAMAGE = 1,
	
}
struct SpellEffect {
	1: required SpellEffectCode effectCode,
	2: optional i16 arg1,
	3: optional i16 arg2,
	4: optional i16 arg3
}
