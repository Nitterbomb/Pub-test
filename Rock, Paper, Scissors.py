import random
def main():
    player_score = 0
    computer_score = 0
    tie_games = 0
    play_again = "y"
    while play_again == "y":
        result = play()
        print(result)
        if result == "You Win":
            player_score += 1
        elif result == "You Lose":
            computer_score += 1
        else:
            tie_games += 1
        print(f"Player Score: {player_score} , Computer Score: {computer_score}, Tie Games: {tie_games}")
        play_again = input(f"Play Again, 'y' or 'n'?").lower()
    
def play():
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Rock, Paper, Scissors: ").lower()
    computer_choice = random.choice(choices)
    print(f"Player Choice: {player_choice}\nComputer Choice: {computer_choice}")
    if player_choice == computer_choice:
        return "Tie Game"
    elif is_win(player_choice, computer_choice):
        return "You Win"
    return "You Lose"

def is_win(player, opponent):
    if (player == "rock" and opponent == "scissors") or (player == "paper" and opponent == "rock") or (player == "scissors" and opponent == "paper"):
        return True

if __name__ == "__main__":
    main()



