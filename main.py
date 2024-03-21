import input
import maph

map1 = maph.Map((0,0))

while True:
    map1.update()
    input.player_action(map1)
