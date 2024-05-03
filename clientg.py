import socket

host = "localhost" 
port = 7777

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    user_input = input("").strip()
    client.sendall(user_input.encode())
    reply = client.recv(1024).decode().strip()
    if "Correct" in reply:
        print(reply)
        name = input("Enter your name: ") 
        client.sendall(name.encode())  
        break
    print(reply)
    continue

    client.close()

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break