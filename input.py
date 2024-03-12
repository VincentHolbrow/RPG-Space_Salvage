directions = ['north','n','south','s','east','e','west','w']

def player_action():
    response = input("What would you like to do? \n")
    if response == 'help':
        print ("north/n - Move to the North\nsouth/s - Move to the South\n" \
               "east/e - Move to the East\nwest/w: Move to the West \n" \
               "quit - Exit the program\ninspect/i - Get details on an object\n" \
                "or environment\n")
#    elif response in directions:
#        maph.move(response)