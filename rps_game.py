import random

def start_rps():
    print("\n=== Rock-Paper-Scissors Game ===")

    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("Enter rock/paper/scissors or 'exit': ").lower()

        if user == "exit":
            print("Exiting Rock-Paper-Scissors...")
            break

        if user not in choices:
            print("Invalid choice! Try again.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            print("🎉 You win!")
        else:
            print("😢 You lose!")
