include "zone.thrift"

struct Map {
	1: list<zone.Zone> zones,
}
