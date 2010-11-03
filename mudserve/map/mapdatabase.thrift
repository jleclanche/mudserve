namespace py mudserve.mudrpc.map.database
include "spell_types.thrift"

struct MapDatabase {
	1: required list<Map> maps;
}
