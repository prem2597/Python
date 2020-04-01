import socket

class HTTPServer:
    def __init__(self, IP, port):
        super().__init__()
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as self.s:
        	self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        	bytesAddressPair = []
        	self.s.bind((IP, port))
        	roll = {'2019501109' : False, '2019501027' : False, '2019501051' : False, '2019501004' : False, '2019501001' : False, '2019501029' : False, '2019501012' : False, '2019501032' : False, '2019501043' : False}
        	ip = {'10.10.10.149' : False, '10.10.8.63' : False, '10.10.10.160' : False, '10.10.10.168' : False, '10.10.10.134' : False, '10.10.8.136' : False, '10.10.9.175' : False, '192.168.43.237' : False, '127.0.0.1' : False}
        	while True :
        		try :
        			self.s.settimeout(20)
        			bytesAddressPair = self.s.recvfrom(1024)
        			print('Connected by', bytesAddressPair[1][0])
	        		addr = bytesAddressPair[1][0]
	        		conn = bytesAddressPair[0].decode('utf-8')
	        		m = False
	        		n = False
	        		for x in ip :
	        			if addr == x :
	        				if ip[addr] == False :
	        					ip[addr] = True
	        					m = True
	        		for y in roll :
	        			if conn == y :
	        				if roll[conn] == False :
	        					roll[conn] = True
	        					n = True
	        		if m == True and n == True :
	        			message = "Accepted and Marked...!!!"
	        			m
	        		elif m == True and n == False :
	        			message = "You attendance is already marked with some other IP address"
	        		elif m == False and n == True :
	        			message = "You Ip address is already used to mark some other person attendance"
	        		else :
	        			message = "Invalid Credentials"
	        		self.s.sendto(bytes(message, "utf-8"), bytesAddressPair[1])
	        	except socket.timeout:
	        		List = []
	        		for key, value in roll.items():
	        			if value == False :
	        				List.append(key)
	        		data = "Absenties :"
	        		data = data + "\n"
	        		for i in List :
	        			data += i
	        			data = data + "\n"
	        		if len(bytesAddressPair) != 0:
	        			self.s.sendto(bytes(data, "utf-8"), bytesAddressPair[1])
        				return
        			return

def main():
	HTTPServer('127.0.0.1', 2020)

if __name__ == "__main__":
    main()
