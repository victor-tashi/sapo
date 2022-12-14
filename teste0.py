import pygame as pg
from pygame.locals import *
from sys import exit as sair

pg.init()

larg = 640
alt = 250
preto = (0, 0, 0)

tela = pg.display.set_mode((larg, alt))
pg.display.set_caption('hacker')


class Sapo(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprits = []
        self.sprits.append(pg.image.load('sprits/attack_1.png'))
        self.sprits.append(pg.image.load('sprits/attack_2.png'))
        self.sprits.append(pg.image.load('sprits/attack_3.png'))
        self.sprits.append(pg.image.load('sprits/attack_4.png'))
        self.sprits.append(pg.image.load('sprits/attack_5.png'))
        self.sprits.append(pg.image.load('sprits/attack_6.png'))
        self.sprits.append(pg.image.load('sprits/attack_7.png'))
        self.sprits.append(pg.image.load('sprits/attack_8.png'))
        self.sprits.append(pg.image.load('sprits/attack_9.png'))
        self.sprits.append(pg.image.load('sprits/attack_10.png'))
        self.atual = 0
        self.image = self.sprits[self.atual]
        self.image = pg.transform.scale(self.image, (128 * 4, 64 * 4))

        self.rect = self.image.get_rect()
        self.rect.topleft = 200, 0

        self.anima = False

    def Atacar(self):
        self.anima = True

    def update(self):
        if self.anima == True:
            self.atual = self.atual + 0.25
            if self.atual >= len(self.sprits):
                self.atual = 0
                self.animar = False
            self.image = self.sprits[int(self.atual)]
            self.image = pg.transform.scale(self.image, (128 * 4, 64 * 4))


ts = pg.sprite.Group()
S = Sapo()
ts.add(S)

time = pg.time.Clock()

while True:
    tela.fill(preto)
    time.tick(60)
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sair()
        if event.type == K_a:
            Sapo.Atacar()
    ts.draw(tela)
    ts.update()
    pg.display.flip()
