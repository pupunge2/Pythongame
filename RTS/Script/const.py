class Color():
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    magenta = (255, 0, 255)
    white = (255, 255, 255)

class Level():
    level = [None,
             [1, 80, 80, 'Start1', 2],
             [2, 80, 240, 'Start2', 3],
             [3, 240, 240, 'Start3', 2]]

class Editor():
    floor_list = []
    unit_list = [1001, 1002, 2001]

class Unit():
    size = {1001 : [40, 40], 1002 : [40, 40], 2001 : [40, 40]}
