import time # Time component is only used for aesthetic
import random # Imports random component for the computer to choose randomly between "Rock", "Paper", or "Scissors

player_input = {
    "rock" : "1",
    "paper" : "2",
    "scissors" : "3"
    }

comp_input = {
    "1" : "rock",
    "2" : "paper",
    "3" : "scissors"
    }

win_list = {
    "11" : "Tie ! Nobody won !",
    "22" : "Tie ! Nobody won !",
    "33" : "Tie ! Nobody won !",
    "12" : "Computer won ! D:",
    "13" : "You won ! :D",
    "21" : "You won ! :D",
    "23" : "Computer won ! D:",
    "31" : "Computer won ! D:",
    "32" : "You won ! :D"
    }

endgame = 0
print(endgame)

def gamestart(): # Game in a function for easier restart
    player_turn = input("Rock, Paper, or Scissors ?") 
    if player_turn.lower() in ["rock", "paper", "scissors"]:# Check if player input is one of the choices, if not, sends an error message
        play_num = player_input[player_turn]
        print("Received input, waiting for Computer to play...")
        comp_num = str(random.randint(1,3))
        comp_turn = comp_input[comp_num]
        print("Computer plays ", comp_turn)
        combine = play_num + comp_num
        winner = win_list[combine]
        print(winner)
        endgame = 1
        print(endgame)
        menu()
    else:
        print("Expected answer not detected, quitting to main menu...") # If player inputs anything else other than "Rock", "Paper" or "Scissors", prints an error message and stops function
        time.sleep(3)
        endgame = 2
        print(endgame)
        menu()
def menu():
    if endgame == 0:
        print("Start game ?")
        choice = input("Y/N")
    elif endgame == 1:
        print("Restart ?")
        choice = input("Y/N")
    else:
        print("Game ended due to an error, want to restart ?")
        choice = input("Y/N")
    
    if choice.lower() in ["y"]:
        gamestart()
    elif choice.lower() in ["n"]:
        exit()
    else:
        print("Expected answer not detected, quitting...")
        time.sleep(3)
        exit()

menu()


