from _thread import *
import threading 
import socket
import random
import sys
import os
import functools

class HTTPServer:
	users = {}
	def __init__(self, IP, port):
		super().__init__()
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as self.s:
			self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.s.bind((IP, port))
			self.s.listen()
			print("Server in Progress..!")
			while True:
				conn, addr = self.s.accept()
				print('Connected by', addr[0])
				thread = threading.Thread(target = self.hangman_game, args = (conn, addr))
				thread.start()

	def word_guessed(self) :
		global text, guess_attempt, result
		if data in secretwordguessed :
			text += 'good guess' + "\n"
			for i in range(l) :
				if secretwordguessed[i] == data :
					result[i] = data
		else :
			guess_attempt = guess_attempt - 1
			text += 'Oops!that letter is not in my word ' + "\n"

	def report(self,conn) :
		global text
		t = result.count('_')
		if t == 0 :
			text += "congratulations Game won!! \n🎉 🎉 🎉 🎉 🎉 🎉 " + "\n" + "secret Word is: " + secretwordguessed + "\n"
			score = self.score_data()
			current_user.score += score
			text += "Your score is: " + str(score) + "\n" + self.getLeaderBoard() + "\n"
			return 1
		if guess_attempt == 0 :
			score = self.score_data()
			current_user.score += score
			text += "Sorry you have run out of lives. \n😔😔😔😔😔😔 \nThe word is " + secretwordguessed + "\nYour score is "  + str(score) + "\nGame Lost " + "\n" + self.getLeaderBoard() + "\n"
			return 1
		return 0

	def compare(self,this,that):
		if(self.users[this].score > self.users[that].score):
			return -1
		elif(self.users[this].score == self.users[that].score):
			if(this > that):
				return -1
		return 1

	def getLeaderBoard(self):
		leaderBoard = sorted(self.users, key=functools.cmp_to_key(self.compare))
		temp = "\n********** Leader Board ********** \n"
		for i in leaderBoard:
			temp +=  i + "\t" + str(self.users[i].score) + "\n"
		return temp

	def score_data(self):
		return (10 * len(secretwordguessed)) - ((6 - guess_attempt) * (len(secretwordguessed)))


	def hangman_game(self, conn, addr) :
		global current_user
		current_user = ""
		global secretwordguessed
		secretwordguessed = ""
		global data
		data = ""
		global text
		text = ""
		global guess_attempt
		global l
		global result
		message = "Welcome to the game, Hangman! \nStay Tuned until the Game start \n--------------------------------- \nPress the number based on the given data below as per your choice: \n1. New user \n2. Registered User \nEnter  your choice below :-"
		conn.sendall(message.encode('utf-8'))
		flag = True
		while flag :
			data = conn.recv(1024).decode('utf-8')
			if data == "2" :
				message = "Enter your username below :-"
				conn.sendall(message.encode('utf-8'))
				while True :
					data = conn.recv(1024).decode('utf-8')
					if data == "1" :
						break
					if data in self.users :
						current_user = self.users[data]
						while True :
							secretwordguessed = random.choice(open('words.txt').read().split()).strip()
							if secretwordguessed not in current_user.word_played :
								current_user.word_played.append(secretwordguessed)
								break
						flag = False
						break
					else :
						message = "You are not a registered player. \nRegister Yourself into the Game. \nEnter 1 to register as a new player :-"
						conn.sendall(message.encode('utf-8'))
					if flag == False :
						break
			if data == "1" :
				message = "Enter the User name below :- "
				conn.sendall(message.encode('utf-8'))
				while True :
					data = conn.recv(1024).decode('utf-8')
					if data in self.users :
						message += "\nAlready registered"
						conn.sendall(message.encode('utf-8'))
					else :
						secretwordguessed = random.choice(open('words.txt').read().split()).strip()
						self.users[data] = User_data(secretwordguessed)
						current_user = self.users[data]
						flag = False
						break
			if flag == True :
				message = "Enter only valid data either 0 or 1"
				conn.sendall(message.encode('utf-8'))
		flag = True
		text = "Data Base is successfully updated \n--------------------------------- \n \nLet start the game now...! \n"
		guess_attempt = 6
		letters = []
		for i in range(26) :
			letters.append(chr(i+97))
		l = len(secretwordguessed)
		print(secretwordguessed)
		result = list("_" * len(secretwordguessed))
		while flag :
			text += "--------------------------------- \nI am thinking of a word that is " + str(l) + " letters long. \n" + "Guessed Word :-  " + (' '.join(result)) + "\n" + "Available letters: " + (','.join(letters))+ "\n" + "You have " + str(guess_attempt) + " guesses left."  + "\n"
			conn.sendall(text.encode('utf-8'))
			data = conn.recv(1024).decode('utf-8')
			data = data.lower()
			text = "------------------------------------" + "\n"
			if data in letters :
				letters.remove(data)
				self.word_guessed()
			else :
				text +=  "Oops! You've already guessed that letter " + (' '.join(result)) + "\n"
			statuscode = self.report(conn)
			if statuscode :
				conn.sendall(text.encode())
				flag = False
				conn.close()

class User_data:
	score = 0
	word_played = []

	def __init__(self,Secretword):
		super().__init__()
		self.word_played.append(Secretword)

def main():
    HTTPServer('127.0.0.1', 8888)

if __name__ == "__main__":
    main()
