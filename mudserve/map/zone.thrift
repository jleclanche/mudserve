namespace py mudserve.mudrpc.map.zone
enum ZONE_TYPE {
	FOREST = 1,
	DENSE_FOREST,
	DESERT
}

struct Zone {
	1: ZONE_TYPE type,
	2: byte      footprint_x,
	3: byte      footprint_y,
	4: i16       pos_x,
	5: i16       pos_y
}
