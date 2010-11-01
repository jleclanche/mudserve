import sys
sys.path.append("../server")

from mudrpc.character.CharacterService import Client
from mudrpc.character.ttypes import *

from thrift import Thrift
from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol.TBinaryProtocol import TBinaryProtocol

try:
	# Make socket
	transport = TSocket("localhost", 9090)
	
	# Buffering is critical. Raw sockets are very slow
	transport = TBufferedTransport(transport)
	
	# Wrap in a protocol
	protocol = TBinaryProtocol(transport)
	
	# Create a client to use the protocol encoder
	client = Client(protocol)
	
	# Connect!
	transport.open()
	
	client.ping()
	print "ping()"
	
	# Create a character
	client.createCharacter("Cide")
	print client.getCharacters()
	client.createCharacter("Adys")
	print client.getCharacters()
	
	# Close!
	transport.close()
except Thrift.TException, e:
	print e.message
