import socket

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.connect(('127.0.0.1',8888))
	print(s.recv(1024).decode())
	flag = False
	while True:
	    s.send(input().encode())
	    message = s.recv(1024).decode()
	    if("Game Lost" in message):
	    	flag = True
	    	break
	    if("Game won!!" in message):
	    	flag = True
	    	break
	    print(message)
	    if flag :
	    	print("Game Over !!!")
	print(message)

if __name__ == "__main__":
    main()
