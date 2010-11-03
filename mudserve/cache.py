import memcache
from mudserve.serialize import Serializer
from mudserve.settings import DATA_ROOT
from os.path import join, normpath
from hashlib import sha1

MEMCACHED_HOST = "127.0.0.1:11211"

client = memcache.Client([MEMCACHED_HOST], debug=0)
# Default set/get methods pass-throughs
set = client.set
get = client.get

# Utility methods
def get_struct(Struct, key):
	"""
	Retrieves a Thrift structure from memcached memory.
	"""
	
	data = client.get(key)
	if data is None:
		return None
	return _serializer.from_string(Struct, data)
	
def set_struct(Struct, key, inst):
	"""
	Sets a Thrift structure in memcached memory.
	"""
	
	return client.set(key, _serializer.to_string(inst))

def get_memory_file(Struct, filepath):
	"""
	Retrieves a Thrift struct from memory, or if it does not exist,
	retrieves it from disk and caches it in memory.
	
	@param Struct
	  The type of Thrift struct to retrieve.
	
	@param filepath
	  The file path to the file on disk, relative to DATA_ROOT.
	"""
	
	# Compute key as the sha1-hash of the absolute path to the file
	path = normpath(join(DATA_ROOT, filepath))
	key = sha1(path).hexdigest()
	
	# Check if it exists in memory
	obj = get_struct(Struct, key)
	if obj is not None:
		return obj
	
	# Read from disk
	f = open(path, "rb")
	data = f.read()
	f.close()
	# Send raw data to memcached
	client.set(key, data)
	return _serializer.from_string(Struct, data)
	
# Utility variables below
_serializer = Serializer()
