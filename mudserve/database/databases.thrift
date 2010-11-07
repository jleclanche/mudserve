namespace py mudserve.mudrpc.database

include "../spell/spell_types.thrift"
include "../map/map.thrift"

/**
 * Includes all database definitions we use. We use a common interface for
 * all of them for simplicity; this is a bit ugly because of Thrift's lack
 * of subclassing however.
 */
 
struct SpellDB {
	1: required map<i16, spell_types.Spell> objects;
}

struct MapDB {
	1: required map<i16, map.Map> objects;
}
