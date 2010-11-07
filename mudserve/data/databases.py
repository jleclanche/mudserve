from mudserve.map.map import MapHandler
from mudserve.spell.spell import SpellHandler

class DatabaseBase(object):
	@classmethod
	def get_object(cls, spellId):
		db = cache.get_memory_file(cls, "data/db/%s.db" % cls.DATABASE_NAME)
		# We use 0-indexed lists but like our object id's to start at 1.
		obj = db.objects[spellId-1]
		return cls.OBJECT_HANDLER(obj)

class SpellDatabase(DatabaseBase):
	DATABASE_NAME = "spell"
	OBJECT_HANDLER = SpellHandler
	
class MapDatabase(DatabaseBase):
	DATABASE_NAME = "map"
	OBJECT_HANDLER = MapHandler
