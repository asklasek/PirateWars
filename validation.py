# validation module

ROWS=10
COLUMNS=10

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

def shipSunk(row, column, oceans):
    ship=oceans[row][column]
    for r in range(ROWS):
        for c in range(COLUMNS):
            if oceans[r][c]==ship.upper():
                return False
    if ship=='s':
        ship="Swashbuckler's vessel"
    elif ship=='c':
        ship='''Cabin boy's rowboat'''
    elif ship=='f':
        ship='Frigate'
    elif ship=='g':
        ship='Galley'
    elif ship=='b':
        ship='Black Medallion'
    elif ship=='v':
        ship="Varmin's Ride"
    elif ship=='q':
        ship="Quickboot's Barnacle"
    elif ship=='b':
        ship="Blackeye's Galley"
    elif ship=='b':
        ship='''Jack Jones' Warship'''
    else:
        ship='Redbeard'
    print()
    print(ship, 'has been sunk!')


