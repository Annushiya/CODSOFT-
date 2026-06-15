import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    print("\n===== ROCK PAPER SCISSORS GAME =====")
    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()

    if user_choice not in choices:
        print("Invalid Choice! Try Again.")
        continue

    computer_choice = random.choice(choices)

    print("Your Choice:", user_choice)
    print("Computer Choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScore Board")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("\nPlay Again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        print("Thank You for Playing!")
        break