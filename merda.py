import pygame, sys
from pygame.locals import *

largura= 1200
altura=700

v=8

class bala(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagembala = pygame.image.load("imagem/bala5.png")

        self.rect = self.imagembala.get_rect()
        self.velocidadebala = 5
        self.rect.top = posy
        self.rect.left = posx

    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadebala

    def colocar(self, superficie):
        superficie.blit(self.imagembala, self.rect)

        

class naveespacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagemnave = pygame.image.load("imagem/nave.png")
        pygame.mixer.music.load("Sons/37.mp3")
        pygame.mixer.music.play(3)

        self.rect = self.imagemnave.get_rect()
        self.rect.centerx = largura / 2 
        self.rect.centery = altura - 60

        self.listadisparo = []
        self.vida = True
        self.velocidade = 20

    def movimentoDireita(self):
        self.rect.right += self.velocidade 
        self.__movimento()
        
    def movimentoEsquerda(self):
        self.rect.left -= self.velocidade 
        self.__movimento()
        
    def __movimento(self):
        if self.vida==True:
            if self.rect.left <= 0:
                self.rect.left=0
                
            elif self.rect.right > 1200:
                self.rect.right = 1200


    def disparar(self, x, y):
        minhabala = bala(x-10,y-50)
        self.listadisparo.append(minhabala)
        print("disparou")

    def colocar(self, superficie):
        superficie.blit(self.imagemnave, self.rect)


def invasaoespaco():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Invasão do Espaço")
    jogador = naveespacial()
    imagemfundo = pygame.image.load("imagem/galaxy2.png")
    jogando = True

    balaprojetil = bala(largura/ 2, altura - 60)

    relogio = pygame.time.Clock()
    
    while True:
        relogio.tick(60)
        balaprojetil.trajetoria()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    jogador.movimentoEsquerda()

                elif evento.key ==K_RIGHT:
                    jogador.movimentoDireita()

                elif evento.key == K_SPACE:
                    x,y = jogador.rect.center
                    jogador.disparar(x,y)
                    
                    
        tela.blit(imagemfundo, (0,0))
        balaprojetil.colocar(tela)
        jogador.colocar(tela)
        if len(jogador.listadisparo) > 0:
            for x in jogador.listadisparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.top < 0:
                    jogador.listadisparo.remove(x)
        pygame.display.update()

invasaoespaco()

        
        



        



    
                    
        
