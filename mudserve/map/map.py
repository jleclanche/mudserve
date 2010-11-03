from mudserve import cache
from mudserve.mudrpc.map.database.ttypes import MapDatabase

class MapHandler(object):
	def __init__(self, map):
		self.map = map

class MapDatabaseHandler(object):
	@classmethod
	def get_map(cls, mapId):
		db = cache.get_memory_file(MapDatabase, "map/map.db")
		# We use 0-indexed maps in memory but like our mapId's to start at 1.
		obj = db.maps[mapId-1]
		return MapHandler(obj)
