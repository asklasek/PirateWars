# main "Pirate Wars" program.

import intro
import ocean
import ships
import metagame

def main():
    print('Please enter the difficulty you would like to play.')
    mode=input('You can choose "easy", "medium", or "hard": ')
    while mode.lower()!='easy' and mode.lower()!='medium' and mode.lower()!='hard':
        mode=input('You can choose "easy", "medium", or "hard": ')
    intro.rules()
    # Create the player ocean.
    playerOcean=ocean.createOcean()
    # Display the player ocean.
    ocean.showOcean(playerOcean)
    # Let player choose where to place the ships.
    ships.shipBuilder(playerOcean)
    # Generate the computers oceans.
    compOcean=ocean.createOcean()
    compOcean=ships.enemyBuilder(compOcean, mode)
    displayOcean=ocean.createOcean()
    # Play through the game.
    metagame.meta(playerOcean, compOcean, displayOcean, mode)
main()
