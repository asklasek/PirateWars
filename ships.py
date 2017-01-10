# ships module

import ocean
import validation
import time

def shipBuilder(playerOcean):
    # Swashbuckler's vessel
    ship='S'
    print("\nWhere would you like to place the Swashbuckler's vessel? It is 2 spaces long.")
    for x in range(2):
        placement=input()
        validShot=validation.validateTile(placement)
        while validShot==False:
            print("That is not a valid location.\nWhere would you like to place the Swashbuckler's vessel?", end=' ')
            placement=input()
            validShot=validation.validateTile(placement)
        playerOcean=setSail(playerOcean, placement, ship)
    print('     __/\\__\n\
  ~~~\\____/~~~~~~\n\
    ~  ~~~   ~.         ')
    print("Swashbuckler's vessel successfully launched.")
    time.sleep(2)
    print("\n    Player's Armada")
    ocean.showOcean(playerOcean)
    # Rowboat
    ship='R'
    print("\nWhere would you like to place the Rowboat? It is 3 spaces long.")
    for x in range(3):
        placement=input()
        validShot=validation.validateTile(placement)
        while validShot==False:
            print("That is not a valid location.\nWhere would you like to place the Rowboat?", end=' ')
            placement=input()
            validShot=validation.validateTile(placement)
        playerOcean=setSail(playerOcean, placement, ship)
    print('     _\n\
    /|\\ \n\
   /_|_\\ \n\
 ____|____\n\
 \\_o_o_o_/\n\
~~ |     ~~~~~\n\
___t_________ ')
    print("Rowboat successfully launched.")
    time.sleep(2)
    print("\n    Player's Armada")
    ocean.showOcean(playerOcean)
    # Galley
    ship='G'
    print("\nWhere would you like to place the Galley? It is 4 spaces long.")
    for x in range(4):
        placement=input()
        validShot=validation.validateTile(placement)
        while validShot==False:
            print("That is not a valid location.\nWhere would you like to place the Galley?", end=' ')
            placement=input()
            validShot=validation.validateTile(placement)
        playerOcean=setSail(playerOcean, placement, ship)
    print('      _~  _~\n\
   __|=|_|=|__\n\
   \\ o.o.o.oY/\n\
    \\_______/\n\
  ~~~~~~~~~~~~~~')
    print("Galley successfully launched.")
    time.sleep(2)
    print("\n    Player's Armada")
    ocean.showOcean(playerOcean)
    # Frigate
    ship='F'
    print("\nWhere would you like to place the Frigate? It is 5 spaces long.")
    for x in range(5):
        placement=input()
        validShot=validation.validateTile(placement)
        while validShot==False:
            print("That is not a valid location.\nWhere would you like to place the Frigate?", end=' ')
            placement=input()
            validShot=validation.validateTile(placement)
        playerOcean=setSail(playerOcean, placement, ship)
    print('       _~\n\
    _~ )_)_~\n\
    )_))_))_)\n\
    _!__!__!_\n\
    \\______t/\n\
  ~~~~~~~~~~~~~')
    print("Frigate successfully launched.")
    time.sleep(2)
    print("\n    Player's Armada")
    ocean.showOcean(playerOcean)
    # Black Medallion
    ship='B'
    print('\nWhere would you like to place the "Black Medallion"? It is 6 spaces long!')
    for x in range(6):
        placement=input()
        validShot=validation.validateTile(placement)
        while validShot==False:
            print("That is not a valid location.\nWhere would you like to place the Black Medallion?", end=' ')
            placement=input()
            validShot=validation.validateTile(placement)
        playerOcean=setSail(playerOcean, placement, ship)
    print('\n\
              |    |    |\n\
             )_)  )_)  )_)\n\
            )___))___))___)\n\
           )____)____)_____)\n\
         _____|____|____|________\n\
---------\                   /---------\n\
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^\n\
    ^^^^      ^^^^     ^^^    ^^\n\
         ^^^^      ^^^')
    print("Black Medallion successfully launched.")
    time.sleep(2)
    print("\n    Player's Armada")
    ocean.showOcean(playerOcean)
    time.sleep(2)
    print('\nAll ships have launched from Tortuga Bay and the cannons are loaded.')
    print("Let's save that treasure!!! YARRR!!!!!!!")
    time.sleep(3)
    
def enemyBuilder(compOcean, mode):
    if mode.lower()=='easy':
        # Varmin's Ride
        compOcean[0][0]='V'
        compOcean[0][1]='V'
        # Quickboot's Barnacle
        compOcean[4][7]='Q'
        compOcean[4][5]='Q'
        compOcean[4][6]='Q'
        # Blackeye's Galley
        compOcean[9][4]='B'
        compOcean[9][6]='B'
        compOcean[9][5]='B'
        compOcean[9][7]='B'
        # Jack Jones' Warship
        compOcean[3][2]='J'
        compOcean[4][2]='J'
        compOcean[5][2]='J'
        compOcean[6][2]='J'
        compOcean[7][2]='J'
        # Redbeard
        compOcean[3][9]='R'
        compOcean[4][9]='R'
        compOcean[5][9]='R'
        compOcean[6][9]='R'
        compOcean[7][9]='R'
        compOcean[8][9]='R'
        # Add mines
        compOcean[4][8]='M'
        compOcean[6][1]='M'

    elif mode.lower()=='medium':
        # Varmin's Ride
        compOcean[0][0]='V'
        compOcean[1][1]='V'
        # Quickboot's Barnacle
        compOcean[6][7]='Q'
        compOcean[4][5]='Q'
        compOcean[5][6]='Q'
        # Blackeye's Galley
        compOcean[2][1]='B'
        compOcean[3][1]='B'
        compOcean[4][1]='B'
        compOcean[5][1]='B'
        # Jack Jones' Warship
        compOcean[8][2]='J'
        compOcean[8][2]='J'
        compOcean[8][3]='J'
        compOcean[8][4]='J'
        compOcean[8][5]='J'
        # Redbeard
        compOcean[2][4]='R'
        compOcean[3][4]='R'
        compOcean[4][4]='R'
        compOcean[5][4]='R'
        compOcean[6][4]='R'
        compOcean[7][4]='R'
        # Add mines
        compOcean[5][5]='M'
        
    elif mode.lower()=='hard':
        # Varmin's Ride
        compOcean[2][3]='V'
        compOcean[3][4]='V'
        # Quickboot's Barnacle
        compOcean[4][9]='Q'
        compOcean[4][8]='Q'
        compOcean[4][7]='Q'
        # Blackeye's Galley
        compOcean[1][8]='B'
        compOcean[2][7]='B'
        compOcean[3][6]='B'
        compOcean[4][5]='B'
        # Jack Jones' Warship
        compOcean[3][0]='J'
        compOcean[4][0]='J'
        compOcean[5][0]='J'
        compOcean[6][0]='J'
        compOcean[7][0]='J'
        # Redbeard
        compOcean[7][2]='R'
        compOcean[7][3]='R'
        compOcean[7][4]='R'
        compOcean[7][5]='R'
        compOcean[7][6]='R'
        compOcean[7][7]='R'
        # Add mines
        compOcean[3][3]='M'
        
    #ocean.showOcean(compOcean) # for debugging only
    return compOcean


def setSail(playerOcean, location, ship):
    row=location[0]
    row=row.upper()
    column=int(location[1:])-1
    row=convert(row)
    playerOcean[row][column]=ship
    return playerOcean


def convert(row):
    if row=='A':
        row=0
    elif row=='B':
        row=1
    elif row=='C':
        row=2
    elif row=='D':
        row=3
    elif row=='E':
        row=4
    elif row=='F':
        row=5
    elif row=='G':
        row=6
    elif row=='H':
        row=7
    elif row=='I':
        row=8
    elif row=='J':
        row=9
    return row
