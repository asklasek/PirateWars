# ocean module

# Set the global variables that can be changed for a bigger or smaller game.
ROWS=10
COLUMNS=10

# The ocean will be a 2 dimensional matrix. 
def createOcean():
    ocean=[]
    for row in range(ROWS):
        ocean.append([])
        for column in range(COLUMNS):
            ocean[row].append('~')
    return ocean
    

# The ocean will be displayed with grid lines.
def showOcean(ocean):
    print()
    yaxis=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for x in range(11):
        print(x, end=' ')
    print()
    for row in range(ROWS):
        print(yaxis[row], end=' ')
        for column in range(COLUMNS):
            print(ocean[row][column], end=' ')
        print()
        
# Ensures the user inputs a valid location on the ocean to avoid crashing the program.
def validateTile(location):
    if len(location)<2 or len(location)>3:
        return False
    if location[0].isalpha()==False:
        return False
    count=0
    yaxis=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if location[0].upper() in yaxis:
        count+=1
    for num in range(1, 11):
        if location[1:]==str(num):
            count+=1
    if count==2:
        return True
    else:
        return False


def updateDisplayOcean(ocean1, ocean2, row, column):
    column-=1
    row-=1
    for x in range(3):
        for y in range(3):
            ocean2[row+x][column+y]=ocean1[row+x][column+y]
    return ocean2
