# metagame

import ocean
import ships
import validation
import random
import time

ROWS=10
COLUMNS=10

def meta(pOcean, cOcean, dOcean, mode):
    turn=0
    win=False
    lose=False
    compShots=loadCannonBalls()
    print('\n    Enemy Waters')
    ocean.showOcean(dOcean)
    while win==False and lose==False:
        turn+=1
        print('\nWhere would you like to take a shot at?', end=' ')
        shot=input()
        validShot=validation.validateTile(shot)
        while validShot==False:
            print('That is not a valid location.\nWhere would you like to take a shot at?', end=' ')
            shot=input()
            validShot=validation.validateTile(shot)
        print('\n***BOOM***\n')
        time.sleep(1)
        cOcean, row, column=shots(shot, cOcean)
        if cOcean[row][column]=='M':
            dOcean=ocean.updateDisplayOcean(cOcean, dOcean, row, column) 
        else:
            dOcean[row][column]=cOcean[row][column]
        time.sleep(2)
        print('\n    Enemy Waters')
        ocean.showOcean(dOcean)
        win=checkWinCondition(cOcean)
        time.sleep(1)
        if win==False:
            time.sleep(2)
            print('\nYour enemies took a shot at you!!!\n')
            time.sleep(1)
            shot=compShots[0]
            compShots=compShots[1:]
            pOcean, row, column=shots(shot, pOcean)
            time.sleep(2)
            print("\n    Player's Armada")
            ocean.showOcean(pOcean)
            lose=checkWinCondition(pOcean)
    if win==True:
        print('\nCongratulations, you sunk all the enemy ships! The treasure is saved!!!!')
        print('You won the game on', mode, 'difficulty in', turn, 'turns.')
        time.sleep(4)
        user=input('Enter your name for the leaderboard: ')
        leaderBoard(mode, turn, user)
    else:
        print('\nYour enemies sunk all your ships! Shibber me timbers!')

def loadCannonBalls():
    arsenal=[]
    yaxis=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for letter in yaxis:
        for num in range(1,11):
            cannonball=letter+str(num)
            arsenal.append(cannonball)
    random.shuffle(arsenal)
    return arsenal

def shots(shot, oceans):
    row=shot[0]
    row=row.upper()
    column=int(shot[1:])-1
    row=ships.convert(row)
    if oceans[row][column]!='~':
        if oceans[row][column]=='M':
            oceans=mine(shot, oceans)      
        else:
            oceans[row][column]=oceans[row][column].lower()
            print('Direct Hit!')
            validation.shipSunk(row, column, oceans)
        
    else:
        oceans[row][column]='X'
        print('A miss!')
    return oceans, row, column

def mine(shot, oceans):
    print('You have shot a mine!\nMAXIMUM DAMAGE!!!!!')
    time.sleep(2)
    row=shot[0]
    row=row.upper()
    column=int(shot[1:])-2
    row=ships.convert(row)-1
    for x in range(3):
        for y in range(3):
            if oceans[row+x][column+y]!='~':
                if oceans[row+x][column+y]=='M' or oceans[row+x][column+y].lower==True:
                    print('A miss!')
                else:
                    oceans[row+x][column+y]=oceans[row+x][column+y].lower()
                    print('Direct Hit!')
                    validation.shipSunk(row, column, oceans)
            else:
                oceans[row+x][column+y]='X'
                print('A miss!')
    return oceans

def checkWinCondition(oceans):
    # check every index in the matrix for a capitol letter.
    for row in range(ROWS):
        for col in range(COLUMNS):
            if oceans[row][col].isupper()==True and oceans[row][col]!='X'\
               and oceans[row][col]!='M':
                # If a capitol letter is found, return False to keep playing
                return False
    # No capitols are found, return True
    return True

def leaderBoard(mode, turn, user):
    filename='Leaderboard'
    outFile=open(filename, 'a')
    outFile.write(user+', ')
    outFile.write(turn+', ')
    outFile.write(mode+'\n')
    outFile.close()
