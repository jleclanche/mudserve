import sys
sys.path.append('../server')

from mudrpc.character import CharacterService
from mudrpc.character.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:

  # Make socket
  transport = TSocket.TSocket('localhost', 9090)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder
  client = CharacterService.Client(protocol)

  # Connect!
  transport.open()

  client.ping()
  print 'ping()'
  
  # Create a character
  client.createCharacter("Cide")
  print client.getCharacters()
  client.createCharacter("Adys")
  print client.getCharacters()

  # Close!
  transport.close()

except Thrift.TException, tx:
  print '%s' % (tx.message)