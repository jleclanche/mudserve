from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.transport.TTransport import TMemoryBuffer

class Serializer(object):
	"""
	Takes care of serializing Thrift structures to and from disk.
	"""
	
	def __init__(self, Struct, transport=TMemoryBuffer, protocol=TBinaryProtocol):
		"""
		Initializes a serializer object for serializing to and from objects
		of the structure Struct.
		"""
		
		self._struct = Struct
		self._transport = transport
		self._protocol = protocol
	
	def from_string(self, str):
		"""
		Deserializes the object from a string to a fully constructed object.
		"""
		
		# Set up our transport and protocol
		transport = self._transport(str)
		protocol = self._protocol(transport)
		# Create a new empty instance
		inst = self._struct()
		# Construct the instance by reading the byte string
		inst.read(protocol)
		
		# Return the fully constructed instance
		return inst
	
	def to_string(self, inst):
		"""
		Serializes the object to a string from a fully constructed object.
		"""
		
		# Set up our transport and protocol
		transport = self._transport()
		protocol = self._protocol(transport)
		# Write the instance serialization to the protocol
		inst.write(protocol)
		
		# Return the serialization as a byte string
		return transport.getvalue()
	
	def from_file(self, filepath):
		"""
		Deserializes an object given a file path. This is a pure utility method.
		"""
		
		f = open(filepath, "rb")
		inst = self.from_string(f.read())
		f.close()
		return inst
	
	def to_file(self, inst, filepath):
		"""
		Serializes an object given an instance and a file path.
		This is a pure utility method.
		"""
		
		str = self.to_string(inst)
		f = open(filepath, "rb")
		f.write(str)
		f.close()
