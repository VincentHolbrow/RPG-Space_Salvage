class map():
    def __init__(self, pos):
        self.pos = (pos)
    def move(self, dir)
        if dir == 'north' or dir == 'n' and 'n' in get_room(pos)['dirs']:
            self.pos = self.pos[0], self.pos[1] + 1
        elif dir == 'south' or dir == 's' and 's' in get_room(pos)['dirs']:
            self.pos = self.pos[0], self.pos[1] - 1
        elif dir == 'east' or dir == 'e' and 'e' in get_room(pos)['dirs']:
            self.pos = self.pos[0] - 1, self.pos[1]