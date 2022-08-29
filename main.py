import pygame as pg
from entidades import Bola, Raqueta

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption('Pong')

bola = Bola(400, 300)
raqueta1 = Raqueta(10, 300, 20, 120)

game_over = False
while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((0, 255, 0))

    bola.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)




    pg.display.flip()

pg.quit()