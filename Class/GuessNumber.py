#Kavan Abeyratne
#ICS3U1
#Mr.Sahota
#Guess the number assignment
import random

def play_guess_the_number():
    min_num = 1
    max_num = 30
    max_guesses = 6

    while True:
        target_number = random.randint(min_num, max_num)
        num_guesses = 0

        print(f"Welcome to the Guess the Number game! I'm thinking of a number between {min_num} and {max_num}.")

        while num_guesses < max_guesses:
            guess = input(f"Guess the number ({min_num}-{max_num}): ")
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if guess < min_num or guess > max_num:
                print(f"You picked a number that is outside the range of {min_num} - {max_num}. Please pick a number within this range!")
            else:
                num_guesses += 1
                if guess < target_number:
                    print("You guessed too low!")
                elif guess > target_number:
                    print("You guessed too high!")
                else:
                    print(f"Congratulations! You guessed the number {target_number} in {num_guesses} {'guess' if num_guesses == 1 else 'guesses'}.")
                    break

            guesses_left = max_guesses - num_guesses
            if guesses_left > 1:
                print(f"You have {guesses_left} guesses left.")
            elif guesses_left == 1:
                print("You have 1 guess left.")
            else:
                print("Out of guesses! The number was", target_number)
                break

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing. Goodbye!")
            break

play_guess_the_number()