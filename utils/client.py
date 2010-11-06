#!/usr/bin/env python
import sys
import time
sys.path.append("../")

from mudserve.mudrpc.combat.CombatService import Client

from thrift import Thrift
from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol.TBinaryProtocol import TBinaryProtocol

try:
	# Make socket
	transport = TSocket("213.100.51.33", 9090)
	
	# Buffering is critical. Raw sockets are very slow
	transport = TBufferedTransport(transport)
	
	# Wrap in a protocol
	protocol = TBinaryProtocol(transport)
	
	# Create a client to use the protocol encoder
	client = Client(protocol)
	
	# Connect!
	transport.open()
	
	while True:
		status = client.getStatus("auth1", "fight1")
		print "Status update:\n%r" % (status)
		
		if status.currentTurn == "player1":
			print "It's your turn, casting spell!\n"
			client.castSpell("auth1", "fight1", 1, "player2")
		print "---------------------"
		time.sleep(1)
	
	# Close!
	transport.close()
except Thrift.TException, e:
	print e.message
