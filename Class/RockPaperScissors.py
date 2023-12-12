import random
user_score = 0
computer_score = 0
valid_moves = ["rock", "paper", "scissors"]
while user_score < 5 and computer_score < 5:
    computer_move = random.choice(valid_moves)
    user_move = input("Enter your move (rock, paper, or scissors): ").lower()
    if user_move in valid_moves:
        print(f"Computer chose {computer_move}")
        print(f"You chose {user_move}")   
        if user_move == computer_move:
            print("It's a tie!")
        elif (
            (user_move == "rock" and computer_move == "scissors") or
            (user_move == "paper" and computer_move == "rock") or
            (user_move == "scissors" and computer_move == "paper")
        ):
            print("You win this round!")
            user_score += 1 
        else:
            print("Computer wins this round!")
            computer_score += 1
        print(f"Your Score: {user_score}, Computer Score: {computer_score}")
    else:
        print("Invalid input. Please enter a valid move (rock, paper, or scissors).")
if user_score >= 5:
    print("Congratulations! You won the game!")

else:
    print("Computer wins the game. Better luck next time!")
