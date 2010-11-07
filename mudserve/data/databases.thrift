namespace py mudserve.mudrpc.database

/**
 * Includes all database definitions we use. We use a common interface for
 * all of them for simplicity; this is a bit ugly because of Thrift's lack
 * of subclassing however.
 */
 
struct SpellDB {
	list<Spell> objects;
}

struct MapDB {
	list<Map> maps;
}
