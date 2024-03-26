from mapdata import *

directions = ['north','n','south','s','east','e','west','w']

def player_action(maph):
    response = input("\nWhat would you like to do? \n")
    if response == 'h' or response == 'help':
        print ("north/n - Move to the North\nsouth/s - Move to the South\n"\
               "east/e - Move to the East\nwest/w: Move to the West \n"\
               "quit - Exit the program\ninspect/i - Get details on an object\n"\
                "or environment\n")
    elif response in directions:
        maph.move(response)
    elif response == 'q' or response == 'quit':
        quit()

    elif response == 'i' or response == 'inspect':
        inspectobj = input('Inspect what?\n')
        try:
            if objects[inspectobj]['id'] in roomlayout[maph.pos[1]][maph.pos[0]]:
                print (objects[inspectobj]['desc'])
            else:
                print('That object does not exist in this room.')
        except:
            print('That object does not exist.')
    
    else:
        print("That's not an available action.")