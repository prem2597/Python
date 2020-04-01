import socket

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('localhost', 2020))
	data = input("enter the roll number:")
	s.sendto(str(data).encode('utf-8'),('127.0.0.1',2020))
	data,conn = s.recvfrom(1024)
	print(data.decode())
	data,conn = s.recvfrom(1024)
	print(data.decode())
	s.close()

if __name__ == "__main__":
    main()
