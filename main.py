def number_guessing_game():
    import random
    game_on = True
    while game_on:
        print("""                                                              
  __ _ _   _  ___  ___ ___ 
 / _` | | | |/ _ \/ __/ __|
| (_| | |_| |  __/\__ \__ \\
 \__, |\__,_|\___||___/___/
  __/ |                    
 |___/     """)
        print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
        level = input("Choose a difficulty. Type 'easy' or 'hard':\n")
        if level.lower() == 'easy':
            no_of_attempts = 10
        else:
            no_of_attempts = 5
        chosen_num = random.randint(1, 100)

        for _ in reversed(range(no_of_attempts)):
            print(f"You have {_} attempts remaining to guess the number.")
            guessed_num = int(input("Make a guess:   "))
            if guessed_num == chosen_num:
                print(f"Correct! The number is {chosen_num}")
                break
            elif guessed_num > chosen_num:
                print("Too high.\nGuess again.")
            else:
                print("Too low.\nGuess again.")

            if _ == 0:
                print("Sorry! You have run out of attempts. You Lost.")

        play_on = input("Do you want to play again?\nIf yes type 'y' else type 'n':\n")
        if play_on.lower() == 'y':
            pass
        else:
            game_on = False


if __name__ == '__main__':
    number_guessing_game()
