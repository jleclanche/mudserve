from mudserve.combat.handler import CombatHandler
from mudserve.mudrpc.combat import CombatService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

PORT = 9090

handler = CombatHandler()
processor = CombatService.Processor(handler)
transport = TSocket.TServerSocket(PORT)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TForkingServer(processor, transport, tfactory, pfactory)

print "Starting the server on port %i..." % (PORT)
server.serve()
print "done."
