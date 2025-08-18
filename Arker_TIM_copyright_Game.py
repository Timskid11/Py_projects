import math
import random
import sys
from enum import Enum 
print()
# First display
print("WELCOME❗❗❗❗❗❗❗❗❗❗❗❗❗")
print(" ")
firstDisplay1 = ("Hello SURVIVOR..🤭\n... I am May🎀")
print(firstDisplay1)
print("")
print("💨 💨 💨 💨...proceeding")
firstDisplay2 = ("I would be your personal guide🤗🤗🙂🙂")
print(firstDisplay2)
print("")
# Rules Information
mayAddressing = input("     The rule of the game is to form words from given letters..There would also be Bonuses along the way⁉\n In or Out❓❔❕\n")
if(mayAddressing.lower().strip() == "in" or mayAddressing.lower().strip() == "i"):
   print("AGREED>>>>>>proceeding...😋😊")
else:
   SystemExit("Cancelled❌")
# Player Info 
playerName = input("Player Name: ")
print("WELCOME " + playerName)
Years = input("Optionals😪🤐🤐\nEnter Age😉 : ")
print("")
yearsContinued = input("\nEnter Gender : ")
if(yearsContinued == "boy" or yearsContinued == "male" or yearsContinued == "m" or yearsContinued == "M"):
   print("Hey "+playerName+",Welcome Boyo😎🤝🏿🤙🏿")
elif(yearsContinued == "gay"):
   print("WHY ARE YOU GAY🙄🧐❓❗❗")
elif(yearsContinued == "girl" or yearsContinued.lower().strip() == "girl"):
   print("Hello Lady 😊😚,Glad you are here "+playerName+"😻😊😇")
else:
   print("Hello😊😚,Glad you are here "+playerName+"😻😊😇")
#Proceeding...
proceed = input("Click any key to Start")
print()
print()
print("BAM❗❗❗❗,Press Enter to start your journey "+playerName)
print()
# level 1
print()
print("LEVEL 1-  EASY")
firstWord = input("The word letters: \n S , C , T ,A \nWORD:  ")
if(firstWord.lower().upper().strip() == "ACTS" or firstWord.lower().upper().strip() == "CATS" or firstWord.lower().upper().strip() == "CAST" or firstWord.lower().upper().strip() == "STAC"):
   print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
elif(firstWord.lower().upper().strip() == "STAC"):
   print("Exceptional🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   print("Olodo😂😁🤣")
# LEVEL 2
print()
print("LEVEL 2-  MEDIUM")
firstWord = input("The word letters are: \n D , U , O , L , C \n")
if(firstWord.lower().upper().strip() == "COULD" ):
   print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
elif(firstWord.lower().upper().strip() == "CLOUD"):
   print("Exceptional🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   print("Olodo😂😁🤣")
# LEVEL 3
print()
print("LEVEL 3-  MEDIUM-HARD")
firstWord = input("The word letters are: \n L , L , A , B , E \n")
if(firstWord.lower().upper().strip() == "ABEL" ):
   print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
elif(firstWord.lower().upper().strip() == "LABEL"):
   print("Exceptional🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   sys.exit("Olodo😂😁🤣")
# LEVEL 4
print()
print("LEVEL 4-  HARD")
firstWord = input("The word letters are: \n E , S , A , L , F , K\n")
if(firstWord.lower().upper().strip() == "FLAKES" ):
   print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
elif(firstWord.lower().upper().strip() == "LAKE" or firstWord.lower().upper().strip() == "FLAKE"):
   print("Exceptional🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   print("Olodo😂😁🤣")
# LEVEL 5.5

print()
print("LEVEL 5.5😂- VERY HARD")
firstWord = input("The word letters are: \n D , A , I , R , B \n")
if(firstWord.lower().upper().strip() == "BRAID" ):
   print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
elif(firstWord.lower().upper().strip() == "BARD" ):
   print("Exceptional🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   sys.exit("Olodo😂😁🤣")
# LEVEL 6
print()
print("LEVEL 6- VERY HARD")
firstWord = input("The word letters are: \n P , S , A , T , M \n")
if(firstWord.lower().upper().strip() == "STAMP" ):
   print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   print("Olodo😂😁🤣")
# LEVEL 7
print()
print("LEVEL 7- VERY HARD")
firstWord = input("The word letters are: \n D , A , E , R , B \n")
if(firstWord.lower().upper().strip() == "BREAD" ):
   print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
elif(firstWord.lower().upper().strip() == "DARBE" ):
   print("Exceptional🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   sys.exit("Olodo😂😁🤣")
# LEVEL 8
print()
print("LEVEL 8- VERY HARD")
firstWord = input("The word letters are: \n C , A , N , E , C , L \n")
if(firstWord.lower().upper().strip() =="CANCEL" ):
   print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
elif(firstWord.lower().upper().strip() == "" ):
   print("Exceptional🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   print("Olodo😂😁🤣")
# LEVEL 9
print()
print("LEVEL 9- VERY HARD")
firstWord = input("The word letters are: \n R , R , D , O ,I , A , H , E , A \n")
if(firstWord.lower().upper().strip() == "DIARRHOEA" ):
   print("Exceptional🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   sys.exit("Olodo😂😁🤣")
# LEVEL 10
print()
print("LEVEL 10- VERY HARD")
firstWord = input("The word letters are: \n D , A , E , E , R , L \n")
if(firstWord.lower().upper().strip() == "DEALER" ):
   print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
elif(firstWord.lower().upper().strip() == "READER" ):
   print("Exceptional🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   print("Olodo😂😁🤣")
# LEVEL 11
print()
print("LEVEL 11- DIFFICULT")
firstWord = input("The word letters are: \n I , L , E ,  A , S  \n")
if(firstWord.lower().upper().strip() == "AISLE" ):
   print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
elif(firstWord.lower().upper().strip() == "LAISE" ):
   print("Exceptional🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   sys.exit("Olodo😂😁🤣")
print("TO PROCEED TO THE MOST DIFFICULT RIDDLES: \n")
# Picking a subject
subjectPick = input("Choose what subject to ask the question from?\n choose 1 for MATHS \n choose 2 for ENGLISH\n\n")
print("REMEMBER!!-Failing this question cancels your progress and exits you❗❗❗❗ ")
if(subjectPick == "1"):
   maths = input("what is the product of 2 and 4 ?  ")
   print(maths)
   if(maths == "8" or maths == "eight"):
      print("Very Correct😉😉")
      print("PROCEED>>>")
   else:
      sys.exit("Oops😣😯")
elif(subjectPick == "2"):
   English = input("What is the past participle of took ?  ")
   print(English)
   if(English.lower().strip() == "taken"):
      print("Correct...PROCEED😁")
   else:
      sys.exit("SORRY😑😶")
else:
   sys.exit("SORRY...😶😑")
print()
print()
print("RIDDLE TIME>>>YAYYYY😊👏🏿👏🏿")
#LEVEL 12
riddle1 = input("What has an eye but cannot see? ")
if(riddle1.lower().upper().strip() == "needle"):
     print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   print("You are Wrong but proceed")
#LEVEL 13
riddle2 = input("What comes down but never goes up?  ")
if(riddle2.lower().upper().strip() == "rain"):
     print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   print("You are Wrong but proceed")
#LEVEL 14
riddle3 = input("I am a Bank that has no branches,what am I ")
if(riddle3.lower().upper().strip() == "riverbank"):
     print("Correct🎉🎉🥂!!!\n Press any click to proceed to the next level")
else:
   print("You are Wrong but proceed")
print()
print()
print("LAST LEVEL🤗🙂🙂")

#LAST LEVEL
copyrightByTimilehinOyinlolaApril2025 = input("What is your name ? ") 
print(copyrightByTimilehinOyinlolaApril2025 + ",Thanks for playing to the end")
copyrightByTimilehinOyinlolaApril2025SecondProof = input("What are your reviews of the game")
print(copyrightByTimilehinOyinlolaApril2025SecondProof)
print()
print("Congratulations "+ copyrightByTimilehinOyinlolaApril2025+",You are truly a WINNER😁😁😄")
sys.exit("Thanks for playing")

