#argparse practical 
import argparse

Timi_parser = argparse.ArgumentParser(
       description = "Small argparse project"
       
)

Timi_parser.add_argument(
    "-n","--name","--n", metavar = "name",
    required = True,  help = "dispkay greetings with name"
    )
args = Timi_parser.parse_args()
print (f"{args.name}")