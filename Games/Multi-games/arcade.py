#Program to either play the RockPaperScisscors game or the guess my number game
import argparse

Timi_parser = argparse.ArgumentParser(
       description = "Small argparse project"
       
)

Timi_parser.add_argument(
    "-n","--name","--n", metavar = "name",
    required = True,  help = "dispkay greetings with name"
    )
args = Timi_parser.parse_args()
print (f"Player {args.name} Saved")
namez = args.name

print(f"{namez} , welcome to the Arcade!\n\n")
def game_select(name = "Player"):
            global namez
            select_game = input("Please choose a game: \n 1 = Rock Paper Scisscors \n 2 = Guess my Number\n\n")
            if select_game == "1":
                        import Rock_Paper_scissors
            
            elif select_game == "2":
                        import guess_my_number
            
            else:
            	print(f"Please,{namez},You must enter 1, 2, or 3.")
            	return game_select()
            	
game_select_name=game_select(args.name)
game_select_name()
