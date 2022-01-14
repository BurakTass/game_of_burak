import pygame
import time
import random
import numpy as np
import os
import grids

"""
os.environ["SDL_VIDEO_CENTERED"]='1'
"""
# resolution
genislik, yukseklik = 1980, 1080
size = (genislik, yukseklik)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
zaman = 60

kirmizi = (238, 130, 238)
blue = (0, 121, 150)
black = (0, 14, 71)
white = (255, 255, 255)

satir_sutun = 30
son = 1

Grid = grids.Grid(genislik, yukseklik, satir_sutun, son)
Grid.random2d_array()

a = True
b = False
while a:
    clock.tick(zaman)
    screen.fill(kirmizi)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                a = False
            if event.key == pygame.K_SPACE:
                b = not b

    Grid.Conway(olu=white, canli=black, surface=screen, pause=b)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.mouse_kontrol(mouseX, mouseY)

    pygame.display.update()

pygame.quit()