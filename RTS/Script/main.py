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

    elif var.scene == 'editor':
        editor.loop()

def set_font():
    var.Font.title = pygame.font.SysFont(None, 60)
    var.Font.main_1 = pygame.font.SysFont(None, 28)

def image_load():
    pass

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
        
        elif event.type == pygame.KEYDOWN:
            if var.scene == 'editor':
                key = event.key
                editor.key_down(key)

init()

while True:
    loop()
