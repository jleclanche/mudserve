namespace py mudserve.mudrpc.spell.types
include "spelleffect.thrift"

// The type of a spell id
typedef i16 SpellID

struct Spell {
	1: required SpellID id,
	2: required string name,
	3: optional list<spelleffect.SpellEffect> effects
}
