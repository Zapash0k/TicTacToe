import time
import random

# Cell name logic
# line 1 = 1 2 3
# line 2 = 4 5 6
# line 3 = 7 8 9
# Var value:
# 0 = empty, 1 = ai, -1 = player
# Declaration of variables 
line1 = [0, 0, 0]
line2 = [0, 0, 0]
line3 = [0, 0, 0]
game_status = 'game' # game, win (ai win), lose (ai lose)

def ai_decision(line1, line2, line3):    #ai move
    pass
    #not ready

def ai_line_check(c1, c2, c3): #good move check
    line = [c1, c2, c3]  #c1 = cell 1, c2 = cell 2...
    check = c1 + c2 + c3
    if check == 2:
        for i in range(3):
            if line[i] != 1:
                return line[i]
    #not ready

def win_check():
    pass

def game_status_check(): 
    for i in range(8):
        if game_status == 'game':
            win_check()
        else:
            return game_status
    #not ready


#main game module 

#start of the game

while game_status == 'game':
    #ai or player are making their move
    game_status_check()
    

#ending the game
