namespace py mudrpc.spell.database
include "spell_types.thrift"

struct SpellDatabase {
	1: required list<spell_types.Spell> spells;
}
