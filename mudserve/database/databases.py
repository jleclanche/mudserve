from os.path import abspath, join
from mudserve.mudrpc.database.ttypes import SpellDB, MapDB
from mudserve.spell.spell import SpellHandler
from mudserve.map.map import MapHandler
from mudserve.settings import MUDSERVE_ROOT

class DatabaseBase(object):
	@classmethod
	def get_file_path(cls):
		"""
		Returns the path to the database file relative to MUDSERVE_ROOT.
		"""
		
		return "database/db/%s.db" % cls.DATABASE_NAME
	
	@classmethod
	def get_json_path(cls):
		"""
		Returns the path to the json file containing object definitions,
		relative to MUDSERVE_ROOT.
		"""
		
		return "database/src/%s.json" % cls.DATABASE_NAME
	
	@classmethod
	def get_object(cls, object_id):
		"""
		Retrieves the object from the database with the given object id.
		"""
		
		db = cache.get_memory_file(cls.DATABASE_STRUCT, cls.get_file_path())
		# We use 0-indexed lists but like our object id's to start at 1.
		obj = db.objects[object_id]
		return cls.OBJECT_HANDLER(obj)
		
	@classmethod
	def from_python(cls, objects):
		"""
		Converts an id => object dict into a database instance.
		"""
		
		object_dict = {}
		for obj in objects:
			object_dict[obj['id']] = cls.OBJECT_HANDLER.from_python(obj)
		# Create and return database
		db = cls.DATABASE_STRUCT(objects=object_dict)
		return db

class SpellDatabase(DatabaseBase):
	DATABASE_NAME = "spell"
	DATABASE_STRUCT = SpellDB
	OBJECT_HANDLER = SpellHandler
	
class MapDatabase(DatabaseBase):
	DATABASE_NAME = "map"
	DATABASE_STRUCT = MapDB
	OBJECT_HANDLER = MapHandler

# A map from db name to db.
DATABASE_MAP = dict((db.DATABASE_NAME, db) for db in
	(SpellDatabase, MapDatabase)
)
