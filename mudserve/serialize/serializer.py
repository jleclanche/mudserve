from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.transport.TTransport import TMemoryBuffer

class Serializer(object):
	"""
	Takes care of serializing Thrift structures to and from disk.
	"""
	
	def __init__(self, Transport=TMemoryBuffer, Protocol=TBinaryProtocol):
		"""
		Initializes a serializer object for serializing to and from objects
		of the structure Struct.
		"""
		
		self._transport = Transport
		self._protocol = Protocol
	
	def from_string(self, Struct, str):
		"""
		Deserializes the object from a string to a fully constructed object.
		"""
		
		# Set up our transport and protocol
		transport = self._transport(str)
		protocol = self._protocol(transport)
		# Create a new empty instance
		inst = Struct()
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
	
	def from_file(self, Struct, filepath):
		"""
		Deserializes an object given a file path. This is a pure utility method.
		"""
		
		f = open(filepath, "rb")
		inst = self.from_string(Struct, f.read())
		f.close()
		return inst
	
	def to_file(self, inst, filepath):
		"""
		Serializes an object given an instance and a file path.
		This is a pure utility method.
		"""
		
		str = self.to_string(inst)
		f = open(filepath, "wb")
		f.write(str)
		f.close()
