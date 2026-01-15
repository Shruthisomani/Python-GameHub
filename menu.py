import rps_game
import snake_game

def main_menu():
    while True:
        print("\n==== Python Game Hub ====")
        print("1. Snake Game")
        print("2. Rock-Paper-Scissors")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            snake_game.start_snake()
        elif choice == "2":
            rps_game.start_rps()
        elif choice == "3":
            print("Thank you for playing! Bye!")
            break
        else:
            print("Invalid choice! Try again.")

main_menu()
