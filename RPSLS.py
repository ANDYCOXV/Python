#Author:        Andy Cox V
#Date:          9/30/2017
#Language:      Python
#File:          RPSLS.py
#Description:
#       RPSLS stands for Rock Paper Sissors Lizard Spock, which was a game
#       like rock paper sissors played on the television show Big Bang Theory.
#       In Rice's Coursera a program must be constructed to play this game
#       against the computer. The game is assessed with the following
#       attributes (each choice is associated with a number):
#               NAME    - VALUE - BEATS
#               Rock    - 0     - Sissors and Lizard
#               Spock   - 1     - Rock and Sissors
#               Paper   - 2     - Spock and Rock
#               Lizard  - 3     - Paper and Spock
#               Sissors - 4     - Lizard and Paper
#       The player is allowed to select a unit to go against the computer and
#       the computer will randomly select a unit to play against the player.
#       A "wheel" will be used to determine the winner and loser of a match.

import random
        
# This function is used to evalaute the comparison to determine the winner.
# This is a table of evaluations of what beats what.
#               Rock    - 0     - Sissors and Lizard
#               Spock   - 1     - Rock and Sissors
#               Paper   - 2     - Spock and Rock
#               Lizard  - 3     - Paper and Spock
#               Sissors - 4     - Lizard and Paper
# To evalute a player victory a "wheel" is used.
# Python does modulus different than a language like C.
# Python uses Knuth's definition:
# Knuth argued for floored division on the basis that it was "mathematically correct".
# Python's modulus will either add or subtract to a value between 0 and modulus - 1.
# So the modulo will always have the sign of the left argument.
# 13 % 5 in Python is (13-5) turns into (13-10) = 3.
# -2 % 5 in Python is (-2 + 5) = 3.

def evaluator(usr, com):

        win = 0;                        # Initilized variable and tie evaluation.
        
        if((usr - com) == 0):
                win = 0
        elif(((usr - com) % 5) > 2):    # Computer victory.
                win = -1
        else:                           # Player victory.
                win = 1

        return win;
        
# The game begins initilize the vairables.

user = -1
player = 0
computer = 0
ties = 0
winner = ""
name = ["ROCK", "SPOCK", "PAPER", "LIZARD", "SISSORS"] # This array is used to convert numbers to strings.

print("""


RPSLS.py - ANDY COX V - 10/10/2017
RPSLS stands for Rock Paper Sissors Lizard Spock, which was a game
like rock paper sissors played on the television program Big Bang Theory.
In Rice's Coursera a program must be constructed to play this game
against the computer. The game is assessed with the following
attributes (each choice is associated with a number):
       NAME    - BEATS
       Rock    - Sissors and Lizard
       Spock   - Rock and Sissors
       Paper   - Spock and Rock
       Lizard  - Paper and Spock
       Sissors - Lizard and Paper
The player is allowed to select a unit to go against the computer and
the computer will randomly select a unit to play against the player.


Press <ENTER> to continue...
""")

input()

# Loop for the game exit on 5.
while(user != 5):

        print(
        """
          --== MAIN SELECTION ==--
     PLAYER:""", player, """ COMPUTER:""", computer, """ TIES:""", ties, """
========================================
\t0) ROCK
\t1) SPOCK
\t2) PAPER
\t3) LIZARD
\t4) SISSORS
\t5) QUIT
        """)
        user = int(input("Please choose an object (0-4) or quit '5' then press <ENTER> when done: "))
        
        if((user < 0) or (user > 5)):
                print("\tINVALID INPUT!")
        elif(user != 5): # Cannot equal 5 since 5 is for exits.
                # Aquire the computer's choice.
                                
                com = random.randint(0,4) # Generate random integers from 0 to 4.
                print("\tThe Computer chooses: ", name[com], "\n\tThe Player chose: ", name[user])
                
                if(evaluator(user, com) == 0):
                        winner = "tie."
                        ties += 1
                elif(evaluator(user, com) == 1):
                        winner = "win for the player."
                        player += 1
                else:
                        winner = "win for the computer."
                        computer += 1
                        
                print("\tResulted in a", winner)
                
print("Exiting...")