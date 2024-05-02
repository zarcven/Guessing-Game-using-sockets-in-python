import socket
import random
host = ""
port = 7777

banner = b"""
==== Number Guessing Game ====
      Choose Difficulty
    [EASY] [MEDIUM] [HARD]
Choose between the difficulties
A = EASY
B = MEDIUM
C = HARD
"""

def diff_chooser(diff):
    if diff == 'a':
        return random.randint(1, 50)
    elif diff == 'b':
        return random.randint(1, 100)
    elif diff == 'c':
        return random.randint(1, 500)

def update_leaderboard(name, tries):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {tries}\n")

def display_ldrbrd():
    with open("leaderboard.txt", "r") as file:
        print("======LEADERBOARD======")
        for line in file:
            print(line.strip())
        print("=======================")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)

print("Server is listening in port %s" % (port))
conn = None
n = 0
while True:
    if conn is None:
        print("waiting for connection...")
        conn, addr = s.accept()
        conn.sendall(banner)
    else:
        client_input = conn.recv(1024)
        if client_input in ['a', 'b', 'c']:
            difficulty = client_input
            n = diff_chooser(difficulty)
            conn.sendall(b"Enter your guess:")
            tries = 0  
        elif client_input.isdigit():
            guess = int(client_input)
            print(f"User guess attempt: {guess}")
            tries += 1  
            if guess > n:
                conn.sendall("Go lower")
                continue
            elif guess < n:
                conn.sendall("Go higher")
                continue
            else:
                conn.sendall(f"You are correct! This is the number of guesses you made: {tries}")
                conn.sendall("Enter your name for the leaderboard: ")
                client_input = conn.recv(1024)
                name = client_input
                update_leaderboard(name, tries)
                conn.sendall(display_ldrbrd())
                conn = None
                continue

