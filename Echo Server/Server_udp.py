import socket

class HTTPServer:
    def __init__(self, IP, port):
        super().__init__()
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as self.s:
        	self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        	self.s.bind((IP, port))
        	while True :
        		data,addr = self.s.recvfrom(1024)
        		self.s.sendto(((data.decode()).upper()).encode(), addr)

def main():
	HTTPServer('127.0.0.1', 2020)

if __name__ == "__main__":
    main()