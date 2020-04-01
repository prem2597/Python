'''
    Write a python server program that
        0. initialized a socket connection on localhost and port 10000
        1. accepts a connection from a  client
        2. receives a "Hi <name>" message from the client
        3. generates a random numbers and keeps it a secret
        4. sends a message "READY" to the client
        5. waits for the client to send a guess
        6. checks if the number is
            6.1 equal to the secret then it should send a message "Correct! <name> took X attempts to guess the secret"
            6.2 send a message "HIGH" if the guess is greater than the secret
            6.3 send a message "LOW" if the guess is lower than the secrent
        7. closes the client connection and waits for the next one
'''

import socket
from random import seed
from random import randint

host = '127.0.0.1'
port = 10002

server_socket = socket.socket()

server_socket.bind((host, port))

server_socket.listen(2)

conn, address = server_socket.accept()

print("Connection from: " + str(address))

# seed(1)

# value = str(randint(0, 10))

text = conn.recv(1024).decode('utf-8')
print(text)

value = str(randint(0, 10))

conn.send(str(f"READY").encode('utf-8'))

# value = 5

count = 0

while True:

    count = count + 1

    data = conn.recv(1024).decode('utf-8')

    # if not data :
    #     break

    # print(type(data))
    # print("from connected user: " + str(data))
    # print(type(int(data)))

    if int(data) == int(value) :
        # print("Correct ... Congratulations !!!! Total number of attempts " + str(count) + ".")
        conn.send(str(f"Correct! <name> took X attempts to guess the secret").encode('utf-8'))
        break

    # data = input(' -> ')

    elif int(value) > int(data) :
        conn.send(str(f"LOW").encode('utf-8'))

    else :
        conn.send(str(f"HIGH").encode('utf-8'))

    # conn.send(data.encode('utf-8'))

conn.close()
print("Connection closed")
