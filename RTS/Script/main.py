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

    img.Level.cleared = pygame.image.load('../Image/Level/LevelCleared.png')
    img.Level.unlock = pygame.image.load('../Image/Level/LevelUnlock.png')
    img.Level.lock = pygame.image.load('../Image/Level/LevelLock.png')

    img.Terrain.tile[101] = pygame.image.load('../Image/Terrain/Grass01.png')

    img.Unit.unit[1001] = pygame.image.load('../Image/Unit/Unit1001.png')
    img.Unit.unit[1002] = pygame.image.load('../Image/Unit/Unit1002.png')
    img.Unit.unit[2001] = pygame.image.load('../Image/Unit/Unit2001.png')

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save.save_to_file()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
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
        
        elif event.type == pygame.KEYDOWN:
            if var.scene == 'editor':
                key = event.key
                editor.key_down(key)

            elif var.scene == 'custom':
                key = event.key
                custom.key_down(key)

        elif event.type == pygame.KEYUP:
            if var.scene == 'editor':
                key = event.key
                editor.key_up(key)

init()

while True:
    loop()
