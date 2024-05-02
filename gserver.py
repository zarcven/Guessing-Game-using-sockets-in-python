import socket
import random
host = ""
port = 7777

banner = b"""
==== Guessing Game ====
   Choose Difficulty
 [EASY] [MEDIUM] [HARD]
"""
eas = b"""
==== Guessing Game ====
 GUESS THE NUMBER 1-5
"""
medi = b"""
==== Guessing Game ====
 GUESS THE NUMBER 1-20
"""
har = b"""
==== Guessing Game ====
 GUESS THE NUMBER 1-100
"""

def easy():
    return random.randint(1, 5)
def med():
    return random.randint(1, 20)
def hard():
    return random.randint(1, 100)

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
        diff = str(client_input.decode().strip())
        if diff == 'easy':
            n = easy()
            print(n)
            while True:
                client_input1 = conn.recv(1024)
                guess = int(client_input1.decode().strip())
                if (guess > n):
                    conn.sendall(b"LOWER")
                    continue
                elif (guess < n):
                    conn.sendall(b"HIGHER")
                    continue
                else:
                    conn.sendall(b"CORRECT")
                    break
        elif diff == 'medium':
            n = med()
            print(n)
            while True:
                client_input1 = conn.recv(1024)
                guess = int(client_input1.decode().strip())
                if (guess > n):
                    conn.sendall(b"LOWER")
                    continue
                elif (guess < n):
                    conn.sendall(b"HIGHER")
                    continue
                else:
                    conn.sendall(b"CORRECT")
                break
        elif diff == 'hard':
            n = hard()
            print(n)
            while True:
                client_input1 = conn.recv(1024)
                guess = int(client_input1.decode().strip())
                if (guess > n):
                    conn.sendall(b"LOWER")
                    continue
                elif (guess < n):
                    conn.sendall(b"HIGHER")
                    continue
                else:
                    conn.sendall(b"CORRECT")
                break
s.close
