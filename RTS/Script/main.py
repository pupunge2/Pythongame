import sys
import pygame

import var
import const
import img
import save
import physics

import title
import saveselect
import levelselect
import field
import editor
import custom

clock = pygame.time.Clock()

def init():
    var.screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Desserterria Strawberry')
    pygame.font.init()
    set_font()
    image_load()
    save.save_init()
    save.load()
    unit_load()

def loop():
    clock.tick(var.FPS)
    input_handle()

    if var.scene == 'title':
        title.loop() 

    elif var.scene == 'save_select':
        saveselect.loop()

    elif var.scene == 'level_select':
        levelselect.loop()

    elif var.scene == 'field':
        field.loop()

    elif var.scene == 'editor':
        editor.loop()

    elif var.scene == 'custom':
        custom.loop()

def set_font():
    var.Font.title = pygame.font.SysFont(None, 60)
    var.Font.main_1 = pygame.font.SysFont(None, 28)

def image_load():
    img.Button.new_map = pygame.image.load('../Image/Button/NewMap.png')
    img.Button.save = pygame.image.load('../Image/Button/Save.png')
    img.Button.load = pygame.image.load('../Image/Button/Load.png')
    img.Button.exit = pygame.image.load('../Image/Button/Exit.png')
    img.Button.done = pygame.image.load('../Image/Button/Done.png')
    img.Button.delete = pygame.image.load('../Image/Button/Delete.png')

    img.Level.cleared = pygame.image.load('../Image/Level/LevelCleared.png')
    img.Level.unlock = pygame.image.load('../Image/Level/LevelUnlock.png')
    img.Level.lock = pygame.image.load('../Image/Level/LevelLock.png')

    img.Terrain.tile[101] = pygame.image.load('../Image/Terrain/Grass01.png')

    img.Unit.unit[1001] = pygame.image.load('../Image/Unit/Unit1001.png')
    img.Unit.unit[1002] = pygame.image.load('../Image/Unit/Unit1002.png')
    img.Unit.unit[2001] = pygame.image.load('../Image/Unit/Unit2001.png')

def unit_load():
    var.unit_list = {}
    f = open('../Data/Unit.txt', 'r')

    f.readline()
    f.readline()

    unit_list = []

    while True:
        line = f.readline()

        if not line:
            break

        temp_list = line.split('|')
        temp_ID = int(temp_list[0])
        temp_name = temp_list[1]
        temp_element = temp_list[2]
        temp_type = temp_list[3]
        temp_weapon_ID = int(temp_list[4])
        temp_attack = int(temp_list[5])
        temp_health = int(temp_list[6])
        temp_speed = int(temp_list[7])
        temp_ability = temp_list[8]

        temp_dict = {'name' : temp_name, 'element' : temp_element, 'type' : temp_type, 'weapon' : temp_weapon_ID, 'attack' : temp_attack, 'health' : temp_health, 'speed' : temp_speed, 'ability' : temp_ability}
        var.unit_list[temp_ID] = temp_dict

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save.save_to_file()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if var.scene == 'field':
                if event.button == 1:
                    field.mouse_left_down()

        elif event.type == pygame.MOUSEMOTION:
            if var.scene == 'field':
                field.mouse_move()

        elif event.type == pygame.MOUSEBUTTONUP:
            if var.scene == 'title':
                if event.button == 1:
                    title.mouse_left_up()

            elif var.scene == 'save_select':
                if event.button == 1:
                    saveselect.mouse_left_up()

            elif var.scene == 'level_select':
                if event.button == 1:
                    levelselect.mouse_left_up()

            elif var.scene == 'editor':
                if event.button == 1:
                    editor.mouse_left_up()

            elif var.scene == 'custom':
                if event.button == 1:
                    custom.mouse_left_up()

            elif var.scene == 'field':
                if event.button == 1:
                    field.mouse_left_up()
                elif event.button == 3:
                    field.mouse_right_up()
        
        elif event.type == pygame.KEYDOWN:
            if var.scene == 'editor':
                key = event.key
                editor.key_down(key)

            elif var.scene == 'custom':
                key = event.key
                custom.key_down(key)

            elif var.scene == 'field':
                key = event.key
                field.key_down(key)

        elif event.type == pygame.KEYUP:
            if var.scene == 'editor':
                key = event.key
                editor.key_up(key)

            elif var.scene == 'field':
                key = event.key
                field.key_up(key)

init()

while True:
    loop()
