import pygame
import numpy as np
import random


class Grid:
    def __init__(self, genislik, yukseklik, sabit, son):
        self.sabit = sabit

        self.sutun = int(yukseklik / sabit)
        self.satir = int(genislik / sabit)

        self.size = (self.satir, self.sutun)
        self.liste = np.ndarray(shape=(self.size))
        self.son = son

    def random2d_array(self):
        for x in range(self.satir):
            for y in range(self.sutun):
                self.liste[x][y] = random.randint(0, 1)

    def Conway(self, olu, canli, surface, pause):
        for x in range(self.satir):
            for y in range(self.sutun):
                y_pos = y * self.sabit
                x_pos = x * self.sabit
                # random_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                if self.liste[x][y] == 1:
                    siyah = pygame.Rect(x * self.sabit, y * self.sabit, self.sabit - self.son,
                                        self.sabit - self.son)
                    pygame.draw.rect(surface, canli, siyah)
                else:
                    beyaz = pygame.Rect(x * self.sabit, y * self.sabit, self.sabit - self.son,
                                        self.sabit - self.son)
                    pygame.draw.rect(surface, olu, beyaz)

        yeni = np.ndarray(shape=(self.size))
        if pause == False:
            for x in range(self.satir):
                for y in range(self.sutun):
                    eleman = self.liste[x][y]
                    sonuc = self.hesapla(x, y)
                    if eleman == 0 and sonuc == 3:
                        yeni[x][y] = 1
                    elif eleman == 1 and (sonuc < 2 or sonuc > 3):
                        yeni[x][y] = 0
                    else:
                        yeni[x][y] = eleman
            self.liste = yeni

    def mouse_kontrol(self, x, y):
        _x = x // self.sabit
        _y = y // self.sabit

        if self.liste[_x][_y] != None:
            self.liste[_x][_y] = 1

    def hesapla(self, x, y):
        count = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x1 = (x + n + self.satir) % self.satir
                y1 = (y + m + self.sutun) % self.sutun
                count += self.liste[x1][y1]

        count -= self.liste[x][y]
        return count