import socket

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('localhost', 2020))
	data = "this is UDp client"
	s.sendall(bytes("hi this is client", "ASCII"))
	response = s.recv(1024)
	print(response.decode())


if __name__ == "__main__":
    main()