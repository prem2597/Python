'''
    Write a python client program that
        0. connects to localhost and port 10000
        1. send a "Hi <name>" message
        2. waits for the server to send the "READY" message
        3. guess a number and send to the server
        4. wait for the server to send the message
        5. Read the message and make a decision based on the following
            4.1 Close the client if the message is of the form "Correct! <name> took X attempts to guess the secret"
            4.2 Use the clue given by the server and repeat from step 3
'''

import socket
from random import seed
from random import randint

host = socket.gethostname()
port = 10000

client_socket = socket.socket()

client_socket.connect((host, port))

# seed(1)

message = randint(0, 10)

data = ''

while data.lower().strip() != 'correct':

    client_socket.send(str(message).encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')

    print('Received from server: ' + data)

    # message = input(" -> ")
    if data == 'low' :
    	# data = int(data)
    	message = randint(int(message) + 1, 10)
    	# client_socket.send(str(message).encode('utf-8'))

    if data == 'high' :
    	message = randint(0, int(message) - 1)




client_socket.close()


