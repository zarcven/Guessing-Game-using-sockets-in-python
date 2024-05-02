import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    print(client.recv(1024).decode())  # Welcome message

    difficulty = input().strip().upper()
    client.send(difficulty.encode())

    response = client.recv(1024).decode()
    if "Invalid difficulty" in response:
        print(response)
        client.close()
        return

    game_over = False
    while not game_over:
        guess = input(response + " ")
        if guess.isdigit():
            client.send(guess.encode())
            response = client.recv(1024).decode()
            print(response)
            if "You are correct" in response:
                name = input("Enter your name: ")
                client.send(name.encode())
                leaderboard = client.recv(4096).decode()
                print(leaderboard)
                game_over = True
        else:
            print("Invalid input. Please enter a number.")

    client.close()

if __name__ == "__main__":
    main()
