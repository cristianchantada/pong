import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption('Pong')

game_over = False

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((0, 255, 0))        

    pg.display.flip()

pg.quit()