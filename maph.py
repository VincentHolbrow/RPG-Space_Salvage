from mapdata import *

roomchange = True

class Map():
    def __init__(self, pos):
        self.pos = (pos)
        self.currentroom = roomlayout[self.pos[1]][self.pos[0]][0]

    def move(self, movedir):
        movedir = movedir[0]
        if movedir in roomdata[self.currentroom[0]]['dirs']:
            global roomchange
            roomchange = True
            if movedir == 'n':
                self.pos = self.pos[0], self.pos[1] - 1
            elif movedir == 's':
                self.pos = self.pos[0], self.pos[1] + 1
            elif movedir == 'e':
                self.pos = self.pos[0] + 1, self.pos[1]
            elif movedir == 'w':
                self.pos = self.pos[0] - 1, self.pos[1]
        else:
            print("You cannot move that way.")
    
    def update(self):
        global roomchange
        self.currentroom = roomlayout[self.pos[1]][self.pos[0]][0]
        if roomchange == True:
            print('-----------------------------------------------')
            roomchange = False
            text = roomdata[self.currentroom[0]]['text']
            for char in roomlayout[self.pos[1]][self.pos[0]]:
                for obj in objects:
                    if char == objects[obj]['id']:
                        text = text + str('\nThere is a ' + obj + '.')
            print(text)