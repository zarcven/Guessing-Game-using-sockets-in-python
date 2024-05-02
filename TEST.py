import random

def diff_chooser(diff):
    if diff == 'A':
        return random.randint(1, 50)
    elif diff == 'B':
        return random.randint(1, 100)
    elif diff == 'C':
        return random.randint(1, 500)

def update_leaderboard(name, tries):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {tries}\n")

print("""
==== Number Guessing Game ====
      Choose Difficulty
    [EASY] [MEDIUM] [HARD]
Choose between the difficulties
A = EASY
B = MEDIUM
C = HARD
""")

while True:
    diff = input("Please Choose between the difficulties: ").upper()
    guessme = diff_chooser(diff)
    tries = 0

    while True:
        number = int(input("Please guess the number: "))
        tries += 1

        if number > guessme:
            print("Go lower")
        elif number < guessme:
            print("Go higher")
        else:
            print(f"You are correct! This is the number of guesses you made: {tries}")
            name = input("Enter your name for the leaderboard: ")
            update_leaderboard(name, tries)
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break