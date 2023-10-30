# Importing the random module
import random

# Declaring possible choices
choices = ['rock', 'paper', 'scissors']


# Defining the game function
def play_game():
    won = False
    while not won:
        userchoice = input("Rock, Paper or Scissors? ").lower()
        computerchoice = choices[random.randint(0, 2)]
        if userchoice in choices:
            if userchoice == computerchoice:
                print(f"Oh no, you tied. You both chose {userchoice}")
                won = True
            elif userchoice == 'rock':
                if computerchoice == 'scissors':
                    print(f"You won, computer chose {computerchoice}")
                    won = True
                else:
                    print(f"You lost, computer chose {computerchoice}")
                    won = True
            elif userchoice == 'paper':
                if computerchoice == 'scissors':
                    print(f"You lost, computer chose {computerchoice}")
                    won = True
                else:
                    print(f"You won, computer chose {computerchoice}")
                    won = True
            else:
                if computerchoice == 'paper':
                    print(f"You won, computer chose {computerchoice}")
                    won = True
                else:
                    print(f"You lost, computer chose {computerchoice}")
                    won = True
        else:
            print("Please make a valid selection")
    playAgain = input("Would you like to play again? Y or N: ").upper()
    if playAgain == 'Y':
        play_game()
    else:
        print("Thanks for playing!")


play = input("Would you like to play? Y or N: ").upper()

if play == 'Y':
    play_game()
