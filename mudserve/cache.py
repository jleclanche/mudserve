import memcache
from mudserve.serialize import Serializer
from mudserve.settings import MUDSERVE_ROOT
from os.path import join, normpath
from hashlib import sha1

MEMCACHED_HOST = "127.0.0.1:11211"

client = memcache.Client([MEMCACHED_HOST], debug=0)

def get(key, namespace=None):
	if namespace is not None:
		key = str(namespace)+"-"+key
	return client.get(key)
	
def set(key, value, namespace=None):
	if namespace is not None:
		key = str(namespace)+"-"+key
	return client.set(key, value)

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
	
	key = _get_path_key(filepath)
	
	# Check if it exists in memory
	obj = get_struct(Struct, key)
	if obj is not None:
		return obj
	
	# Read from disk
	path = join(MUDSERVE_ROOT, filepath)
	f = open(path, "rb")
	data = f.read()
	f.close()
	# Send raw data to memcached
	client.set(key, data)
	return _serializer.from_string(Struct, data)
	
def expire_memory_file(filepath):
	"""
	This method expires the cache related to a specific file in memory.
	"""
	
	client.delete(_get_path_key(filepath))
	
# Help variables below
_serializer = Serializer()

def _get_path_key(filepath):
	# Compute key as the sha1-hash of the file path
	# (should be a path relative to MUDSERVE_ROOT)
	path = normpath(filepath)
	key = sha1(path).hexdigest()
	return key
