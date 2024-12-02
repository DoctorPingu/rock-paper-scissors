import random
import time
import sys

def menu():
    while True:
        try:
            user_input = input("\nTo begin, type START\nTo exit, type EXIT\n")
            if user_input.upper() == "START":
                print("\nLoading...\n")
                time.sleep(2)
                print("\nGame loaded.\n")
                return "start"
            elif user_input.upper() == "EXIT":
                print("\nExiting...")
                time.sleep(1)
                return "exit"
            else:
                print("Invalid input.")
        except KeyboardInterrupt:
            print("\nExiting...")
            return "exit"

def explain_rules():
    print("\nThe rules are simple:\n",
          "Rock beats Scissors.\n",
          "Scissors beats Paper.\n",
          "Paper beats Rock.\n",
          "You and the computer will each choose one of these options.\n",
          "The winner of each round is determined by these rules.\n")

def intro():
    print("Welcome to the game: Rock, Paper, Scissors!")
    while True:
        try:
            user_input = input("Would you like to view the rules? Type 'yes' or 'no'\n")
            if user_input.lower() == "yes":
                explain_rules()
                break
            elif user_input.lower() == "no":
                break
            else:
                print("Invalid input.")
        except Exception as e:
            print("\nError occured: " + str(e))
            return "exit"
        
def determine_round_winner(player_move, computer_move, rules):
    if player_move not in rules:
        return "Invalid move. Please choose rock, paper, or scissors."

    if player_move == computer_move:
        return "Tie!"
    elif rules[player_move] == computer_move:
        return "Player wins the round!"
    else:
        return "Computer wins the round!"


def play_game():
    player_score = 0
    computer_score = 0
    rounds_played = 0

    game_choice = ["rock", "paper", "scissors"]

    rules = {"rock":"scissors",
            "paper":"rock",
            "scissors":"paper"} 

    while player_score < 3 and computer_score < 3:
        rounds_played = rounds_played + 1
        print((f"\nRound {rounds_played}:"))

        player_move = input("Pick your move (rock, paper, scissors): ").lower()
        computer_move = random.choice(game_choice)
        print(f"Computer's move: {computer_move}")

        if player_move in game_choice:
            round_winner = determine_round_winner(player_move, computer_move, rules)
            print(round_winner)
            if round_winner == "Player wins the round!":
                player_score = player_score + 1
            elif round_winner == "Computer wins the round!":
                computer_score = computer_score + 1
        else:
            print("Invalid move. Please choose rock, paper, or scissors.")

    print("\nGame Over!\n")

    if player_score > computer_score:
        print("Congratulations! You won!")
    elif computer_score > player_score:
        print("You lost! Better luck next time!")
    else:
        print("It's a tie! Try harder next time!")

    print(f"Final Score - Player: {player_score}, Computer: {computer_score}")
    sys.exit()