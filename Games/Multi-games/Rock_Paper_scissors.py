import sys
import random
from enum import Enum
import argparse
Timi_parser = argparse.ArgumentParser(
     description = "Small argparse project"
       
    )
    
Timi_parser.add_argument(
    "-n","--name","--n", metavar = "name",
    required = True,  help = "display greetings with         name"
    )
args = Timi_parser.parse_args()
namez = args.name

def rps(name = "Player1"):
    global namez
    game_count = 0
    player_wins = 0
    python_wins = 0
    game_percentage = 100
    def play_rps():
        global namez
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        nonlocal game_percentage

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{name} Please,Enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"Please,{name},You must enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name},you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )

        def decide_winner(player, computer):
            global namez
            nonlocal player_wins
            nonlocal python_wins
            nonlocal game_percentage
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉{namez}, You win!"
                
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉{namez}, You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉{namez}, You win!"
            elif player == computer:
                return f"😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1
        nonlocal game_percentage
        

        print(f"\nGame count: {game_count}")
        print(f"\n{namez}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"\nPlay again,{namez}?")

        while True:
            playagain = input("\nY for Yes   or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
k
        if playagain.lower() == "y":
            return play_rps()
        else:   
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye! {namez}👋")
            from arcade import arcade

    return play_rps()
   
    
    
rock_paper_scissors = [rps(args.name),decide_winner(args.name),play_rps(args.name)]
       
rock_paper_scissors()
