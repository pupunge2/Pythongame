scene = None
FPS = 40
scene = 'title'
state = ''

class Font():
    title = None
    main_1 = None

class Save():
    data = [
        {'new' : True, 'level' : [], 'card' : [], 'upgrade' : []},
        {'new' : True, 'level' : [], 'card' : [], 'upgrade' : []},
        {'new' : True, 'level' : [], 'card' : [], 'upgrade' : []},
        {'new' : True, 'level' : [], 'card' : [], 'upgrade' : []}
    ]

class Field():
    pass

class Player_Ready():
    level_cleared = []
    level_unlock = []
    level_lock = []
    card = []
    upgrade = []

class Player():
    pass

class Editor():
    map_name_edit = False
    map_name = 'New Map'
    map_theme = 'grass'
    map_size = 64

    temp_data = []

    terrain = []
    floor = []
    unit = []