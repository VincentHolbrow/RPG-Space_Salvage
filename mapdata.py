roomdata = {
    'a': {
        'text':"You are in a long hallway with steel walls.\n"
              "The hall continues to the South, and there is a doorway to the North.",
        'dirs':["n","s"]
    },
    'b': {
        'text':"You are in a small room with steel walls.\n"
        "There is a doorway to the South.",
        'dirs':["s"]
    },
    'c': {
        'text': "You are at a turn in a hallway.\n"
        "The hallway continues to the North and East.",
        'dirs':["n","e"]
    },
    'd': {
        'text': "You are in a long, steel hallway.\n"
        "The hallway continues to the East and West.",
        'dirs':["w","e"]
    },
    'e': {
        'text': "You are at the end of a steel hallway.\n"
        "You can exit to the West.",
        'dirs':["w"]
    }
}
objects = {
    'lasergun':{
        'id': '1',
        'desc': 'gun that shoots lasers'
    }
}
roomlayout = [
    ['b',None,None],
    ['a1',None,None],
    ['c','d','e']
]