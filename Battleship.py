'''
Created on Nov 14, 2022
@author: KHarashima25

This code allows the user to play a game of rock paper scissors against a computer playing pseudorandomly
No currently known bugs
Bonuses - Repeat Game option
'''
import random # random

def main():
    usership, compship, tryp, pcoords, ccoords, pmiss, phit, cmiss, chit = startGame()  # Set Game
    missilecount= 5                                                                     # Reset Player Missile Number
    cmissilecount = 5                                                                   # Reset Computer Missile Number
    reload(usership,tryp,missilecount,cmissilecount)                                    # Print Boards and Interface
    hitcount = 0                                                                        # Reset Player Hit Number
    chitcount = 0                                                                       # Reset Computer Hit Number
    while missilecount != 0:                                                            # Loop for Player and Computer Moves
        compship, tryp, ccoords, pmiss, phit, hitcount = userFire(compship, tryp, ccoords, pmiss, phit, hitcount)           # user move
        missilecount = missilecount-1                                                                   # update player missile counter
        pcoords, cmiss, chit, usership, chitcount = compFire(pcoords, cmiss, chit, usership, chitcount) # computer move
        cmissilecount = cmissilecount-1                                                                 # update computer missile counter
        reload(usership,tryp,missilecount,cmissilecount)                                                # reset interface
    clearBoard()
    print("\nYour Ships -")      # interface - show player's missiles
    printBoard(usership)                                                    # print updated board (player's ships)
    print("\nThe Enemy's Ships -")
    printBoard2(compship)                                                   # print updated board (computer's ships hidden)
    print("\n")
    print("Your Opponent Hit", chitcount,"Ships\nYou Hit", hitcount,"Ships")          # Detect Who Wins
    if chitcount > hitcount: print("Your Opponent Won!") 
    elif chitcount < hitcount: print("You Won!")
    elif chitcount == hitcount: print("You Tied!")

def startGame():
    ccoords = []
    pcoords = []
    pmiss = []
    phit = []
    cmiss = []
    chit = []
    compship = [['01','02','03','04','05'], ['06','07','08','09','10'], ['11','12','13','14','15'], ['16','17','18','19','20'], ['21','22','23','24','25']]           # set board to default
    usership = [['01','02','03','04','05'], ['06','07','08','09','10'], ['11','12','13','14','15'], ['16','17','18','19','20'], ['21','22','23','24','25']]           # set board to default
    tryp = [['01','02','03','04','05'], ['06','07','08','09','10'], ['11','12','13','14','15'], ['16','17','18','19','20'], ['21','22','23','24','25']]           # set board to default
    
    placecount = 4                                                          # counter for placing boats loop
    while placecount >= 0:                                                  # loop for placing boats
        printBoard(usership)                                                # print clean board
        boatnumber = placecount+1                                           # set boat counter (purely for interface)
        print("\nBoats Left -", boatnumber)                                 # interface data (boats left to place)
        usership, pcoords = userPlace(usership,pcoords)                     # player place
        placecount = placecount - 1                                         # update counter for placing boats loop
    placecount = 4                                                          # reset counter for placing boats loop (for computer)
    while placecount >= 0:                                                  # loop for placing boats (computer)
        compship, ccoords = compPlace(compship,ccoords)                     # computer place
        placecount = placecount -1                                          # update counter for placing boats loop

    return usership, compship, tryp, pcoords, ccoords, pmiss, phit, cmiss, chit # return and end setup

def reload(usership,tryp,missilecount,cmissilecount):
    clearBoard()                                                            # clear past interface from screen
    print("Computer's Remaining Missiles:", cmissilecount)                  # interface - show computer's missiles
    print("Your Remaining Missiles:", missilecount,"\n\nYour Ships -")      # interface - show player's missiles
    printBoard(usership)                                                    # print updated board (player's ships)
    print("\nThe Enemy Waters -")
    printBoard1(tryp)                                                       # print updated board (computer's ships hidden)
    print("\n")
    
def clearBoard():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")   # clear past interface using new lines

def printBoard(usership):                                                   # print board containing player's ships
    for row in range(0,5):                                                  
        column = 0
        for column in range(0,5): print(usership[row][column],end = ' ')
        print('')
    
def printBoard1(tryp):                                                      # print board containing computer's ships (hidden)
    for row in range(0,5):                                        
        column = 0
        for column in range(0,5): print(tryp[row][column],end = ' ')
        print('')

def printBoard2(compship):                                                      # print board containing computer's ships (hidden)
    for row in range(0,5):                                        
        column = 0
        for column in range(0,5): print(compship[row][column],end = ' ')
        print('')

def userPlace(usership,pcoords): # takes the board, asks the user for an input, inputs their answer into the board, returns the new board       
    while True:
        num = input('What number would you like to place a ship in?\n') # query
        if num == '1': num = '01'   # formatting for 0's before digit
        elif num == '2': num = '02'
        elif num == '3': num = '03'
        elif num == '4': num = '04'
        elif num == '5': num = '05'
        elif num == '6': num = '06'
        elif num == '7': num = '07'
        elif num == '8': num = '08'
        elif num == '9': num = '09'
        if num == '01' or num == '02' or num == '03' or num == '04' or num == '05' or num == '06' or num == '07' or num == '08' or num == '09' or num == '10' or num == '11' or num == '12' or num == '13' or num == '14' or num == '15' or num == '16' or num == '17' or num == '18' or num == '19' or num == '20' or num == '21' or num == '22' or num == '23' or num == '24' or num == '25':
            for row in range(0,5):          # loop through, then place ship in coordinate
                column = 0
                for column in range(0,5):
                    if usership[row][column] == num:    # when coordinates from query = coordinate on board
                        if usership[row][column] != '[]':
                            usership[row][column] = '[]'    # place ship
                            pcoords.append(num)             # add ship's location to list 
                            return usership,pcoords
            print("That spot is already occupied")
        else: print("Your answer was invalid")

def compPlace(compship,ccoords): 
    choices = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']    # create list for pseudo-random choice
    while True:
        num = random.choice(choices)                # choose 'random number' from list
        for row in range(0,5):                      # loop through, then place ship in coordinate
            column = 0
            for column in range(0,5):
                if compship[row][column] == num:    # when coordinates from query = coordinate on board
                    compship[row][column] = '[]'    # place ship (can't see)
                    ccoords.append(num)             # add ship's location to list
                    return compship,ccoords

def userFire(compship,tryp,ccoords, pmiss, phit, hitcount): # takes the board, asks the user for an input, inputs their answer into the board, returns the new board       
    while True:
        num = input('What number would you like to fire at?\n') # query
        if num == '1': num = '01'   # formatting for 0's before digit
        elif num == '2': num = '02'
        elif num == '3': num = '03'
        elif num == '4': num = '04'
        elif num == '5': num = '05'
        elif num == '6': num = '06'
        elif num == '7': num = '07'
        elif num == '8': num = '08'
        elif num == '9': num = '09'
        if num == '01' or num == '02' or num == '03' or num == '04' or num == '05' or num == '06' or num == '07' or num == '08' or num == '09' or num == '10' or num == '11' or num == '12' or num == '13' or num == '14' or num == '15' or num == '16' or num == '17' or num == '18' or num == '19' or num == '20' or num == '21' or num == '22' or num == '23' or num == '24' or num == '25':
            for counter in phit:        # test for repeated target (when past coordinate was a hit)
                if num == counter: print("You've already tried that spot!")
            for counter in ccoords:     # test for successful hit
                if num == counter:
                    phit.append(num)    # add coord of hit into list
                    for row in range(0,5):  # update visual chart
                        column = 0
                        for column in range(0,5):
                            if tryp[row][column] == num:
                                tryp[row][column] = 'XX'
                                compship[row][column] = 'XX'
                                hitcount = hitcount + 1
                                return compship, tryp, ccoords, pmiss, phit, hitcount
            for counter in pmiss:       # test for repeated target (when past coordinate was a miss)
                if num == counter:
                    print("You've already tried that spot!")
            break
        else: print("Invalid Response - Try Again") # catch invalid
    pmiss.append(num)
    for row in range(0,5):
        column = 0
        for column in range(0,5):
            if tryp[row][column] == num:
                tryp[row][column] = '--'
                compship[row][column] = '--'
    return compship, tryp, ccoords, pmiss, phit, hitcount

def compFire(pcoords, cmiss, chit, usership, chitcount): 
    choices = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']    # create list for pseudo-random choice
    while True:
        loop = 0                        # set loop counter
        num = random.choice(choices)    # choose 'random number' from list
        if num == '01' and usership[0][0] == '[]': usership[0][0] = 'XX' # hardcoding for testing if the computer hits a player's ship
        elif num == '02' and usership[0][1] == '[]': usership[0][1] = 'XX'
        elif num == '03' and usership[0][2] == '[]': usership[0][2] = 'XX'
        elif num == '04' and usership[0][3] == '[]': usership[0][3] = 'XX'
        elif num == '05' and usership[0][4] == '[]': usership[0][4] = 'XX'
        elif num == '06' and usership[1][0] == '[]': usership[1][0] = 'XX'
        elif num == '07' and usership[1][1] == '[]': usership[1][1] = 'XX'
        elif num == '08' and usership[1][2] == '[]': usership[1][2] = 'XX'
        elif num == '09' and usership[1][3] == '[]': usership[1][3] = 'XX'
        elif num == '10' and usership[1][4] == '[]': usership[1][4] = 'XX'
        elif num == '11' and usership[2][0] == '[]': usership[2][0] = 'XX'
        elif num == '12' and usership[2][1] == '[]': usership[2][1] = 'XX'
        elif num == '13' and usership[2][2] == '[]': usership[2][2] = 'XX'
        elif num == '14' and usership[2][3] == '[]': usership[2][3] = 'XX'
        elif num == '15' and usership[2][4] == '[]': usership[2][4] = 'XX'
        elif num == '16' and usership[3][0] == '[]': usership[3][0] = 'XX'
        elif num == '17' and usership[3][1] == '[]': usership[3][1] = 'XX'
        elif num == '18' and usership[3][2] == '[]': usership[3][2] = 'XX'
        elif num == '19' and usership[3][3] == '[]': usership[3][3] = 'XX'
        elif num == '20' and usership[3][4] == '[]': usership[3][4] = 'XX'
        elif num == '21' and usership[4][0] == '[]': usership[4][0] = 'XX'
        elif num == '22' and usership[4][1] == '[]': usership[4][1] = 'XX'
        elif num == '23' and usership[4][2] == '[]': usership[4][2] = 'XX'
        elif num == '24' and usership[4][3] == '[]': usership[4][3] = 'XX'
        elif num == '25' and usership[4][4] == '[]': usership[4][4] = 'XX'
        #
        elif num == '01' and usership[0][0] == '01': usership[0][0] = '--'  # hardcoding for testing if the computer misses
        elif num == '02' and usership[0][1] == '02': usership[0][1] = '--'
        elif num == '03' and usership[0][2] == '03': usership[0][2] = '--'
        elif num == '04' and usership[0][3] == '04': usership[0][3] = '--'
        elif num == '05' and usership[0][4] == '05': usership[0][4] = '--'
        elif num == '06' and usership[1][0] == '06': usership[1][0] = '--'
        elif num == '07' and usership[1][1] == '07': usership[1][1] = '--'
        elif num == '08' and usership[1][2] == '08': usership[1][2] = '--'
        elif num == '09' and usership[1][3] == '09': usership[1][3] = '--'
        elif num == '10' and usership[1][4] == '10': usership[1][4] = '--'
        elif num == '11' and usership[2][0] == '11': usership[2][0] = '--'
        elif num == '12' and usership[2][1] == '12': usership[2][1] = '--'
        elif num == '13' and usership[2][2] == '13': usership[2][2] = '--'
        elif num == '14' and usership[2][3] == '14': usership[2][3] = '--'
        elif num == '15' and usership[2][4] == '15': usership[2][4] = '--'
        elif num == '16' and usership[3][0] == '16': usership[3][0] = '--'
        elif num == '17' and usership[3][1] == '17': usership[3][1] = '--'
        elif num == '18' and usership[3][2] == '18': usership[3][2] = '--'
        elif num == '19' and usership[3][3] == '19': usership[3][3] = '--'
        elif num == '20' and usership[3][4] == '20': usership[3][4] = '--'
        elif num == '21' and usership[4][0] == '21': usership[4][0] = '--'
        elif num == '22' and usership[4][1] == '22': usership[4][1] = '--'
        elif num == '23' and usership[4][2] == '23': usership[4][2] = '--'
        elif num == '24' and usership[4][3] == '24': usership[4][3] = '--'
        elif num == '25' and usership[4][4] == '25': usership[4][4] = '--'
        else: loop = 1          # if invalid then loop -> 1
        for counter in pcoords: # detects computer hit
            if num == counter:
                chit.append(num)    # add coord of hit into list
                chitcount = chitcount + 1   # update computer's score counter
                return pcoords, cmiss, chit, usership, chitcount     
        if loop == 0:
            break
    cmiss.append(num)     # add coord of miss into list
    return pcoords, cmiss, chit, usership, chitcount

if __name__ == '__main__': main()