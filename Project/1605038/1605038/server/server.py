import SocketServer
import time

port = 8000
data_length = 10000000
ip = '10.0.2.4'

data = "A" * data_length


class TCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print "Connection opened from %s:%d." % self.client_address
	time0 = time.time()
        self.request.sendall(data)
	time1 = time.time()
	print "Data sent in (seconds): ", time1-time0
        

server = SocketServer.TCPServer((ip, port), TCPRequestHandler)
try:
	print "Server started on ", port
	server.serve_forever()
except KeyboardInterrupt as e: server.shutdown()


