import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    computer_choice = random.choice(choices)
    
    print(f"\nYour choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You won")
    elif  (computer_choice == 'rock' and user_choice == 'scissors') or \
         (computer_choice == 'paper' and user_choice == 'rock') or \
         (computer_choice == 'scissors' and user_choice == 'paper'):
        print("Computer won")
    else:
        print("Wrong choice")
        
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break
