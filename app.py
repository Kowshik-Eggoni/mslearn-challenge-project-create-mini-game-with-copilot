import random

def get_computer_choice():
    """Randomly select between rock, paper, or scissors."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the game."""
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    else:
        return 'lose'
    
def main():
    player_score = 0
    while True:
        player_choice = input("Choose 'rock', 'paper', or 'scissors': ").lower()
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        if result == 'win':
            player_score += 1
            print("YOu won this round!")
        elif result == 'lose':
            print("You lost this round.")
        else:
            print("It's a tie.")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"Final Score: {player_score}")
            break

if __name__ == '__main__':
    main()