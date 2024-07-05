import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        user_input = input("Enter your choice (1/2/3/4): ")
        if user_input == '4':
            print("Thanks for playing!")
            print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
            break

        choices_dict = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        if user_input not in choices_dict:
            print("Invalid choice. Please try again.")
            continue

        user_choice = choices_dict[user_input]
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Scores - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()
