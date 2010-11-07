class DatabaseObjectHandler(object):
	"""
	Defines the minimum interface for database object handlers.
	These methods are required in order to properly serialize to
	and from disk and for generating Thrift structures from json.
	
	The exposed interface may implement whatever methods deemed
	necessary as long as the minimum interface defined below is implemented.
	"""
	
	@classmethod
	def from_python(cls, data):
		"""
		Returns a Thrift structure instance from python's dict representation
		of the object. This is used for serializing the json files into
		Thrift structures and later to disk.
		"""
		
		raise NotImplementedError
	
	def __init__(self, thrift_object):
		"""
		Takes a Thrift structure and initializes the object handler for
		use in python code.
		"""
		
		raise NotImplementedError
