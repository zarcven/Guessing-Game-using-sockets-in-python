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
        leaderboard = file.read()
        return leaderboard.encode()

def play_again(conn):
    conn.sendall(b"Do you want to play again? (yes/no): ")
    choice = conn.recv(1024).decode().strip().lower()
    if choice == "yes":
        return True
    elif choice == "no":
        return False
    else:
        conn.sendall(b"Invalid choice. Please enter 'yes' or 'no'.")
        return play_again(conn)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)

print("Server is listening in port %s" % (port))

while True:
    conn, addr = s.accept()
    conn.sendall(banner)

    while True:
        client_input = conn.recv(1024).decode().strip()
        if client_input in ['a', 'b', 'c']:
            difficulty = client_input
            n = diff_chooser(difficulty)
            conn.sendall(b"Enter your guess: ")
            tries = 0  
        elif client_input.isdigit():
            guess = int(client_input)
            tries += 1  

            if guess == n:
                conn.sendall(f"You are correct! This is the number of guesses you made: {tries}\nEnter your name for the leaderboard: ".encode())
                client_input = conn.recv(1024).decode().strip()
                name = client_input
                update_leaderboard(name, tries)
                conn.sendall(display_ldrbrd())
                if not play_again(conn):
                    conn.close()
                    break
                else:
                    conn.sendall(banner)
                    continue
            elif guess > n:
                conn.sendall(b"Go lower: ")
                continue
            elif guess < n:
                conn.sendall(b"Go higher: ")
                continue
        else:
            conn.sendall(b"Invalid response. Please enter a valid guess.")
            continue

s.close()
