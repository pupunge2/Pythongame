scene = None
FPS = 40
scene = 'title'
state = ''

unit_list = {}

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
    terrain = []
    floor = []
    unit = []
    num_of_summoned_units = 0
    camera = [0, 0]

class Player_Ready():
    level_cleared = []
    level_unlock = []
    level_lock = []
    card = []
    upgrade = []

class Player():
    selected_unit = []
    mouse_left_down = [0, 0]
    mouse_move_position = [0, 0]
    mouse_left_up = [0, 0]
    mouse_right_up = [0, 0]
    mouse_press = False

class Editor():
    map_name_edit = False
    map_name = 'New Map'
    map_theme = 'grass'
    map_size = 64

    camera = [0, 0]
    key_pressed = [False, False, False, False]
    team_mode = 1
    selected_unit = -1
    unit_delete_mode = False

    terrain = []
    floor = []
    unit = []

class Custom():
    load_map_name = ''
    load_map_name_edit = False