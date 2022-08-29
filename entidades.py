import pygame as pg

class Bola:
    def __init__(self, x, y, radio=10, color=(222, 255, 0)):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color

        self.vx = 0
        self.vy = 0

    def dibujar(self, pantalla):
        pg.draw.circle(pantalla, self.color, (self.x, self.y), self.radio)


class Raqueta:

    def __init__(self, x, y, w=120, h=20, color=(255, 255, 0)):
        self.x = x
        self.y = y
        self.color = color
        self.w = w
        self.h = h


        self.vx = 0
        self.vy = 0

    def dibujar(self, pantalla):
        pg.draw.rect(pantalla, self.color, (self.x, self.y, self.w, self.y))

        