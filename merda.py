import pygame, sys
import time
from pygame.locals import *

largura= 1200
altura=700

v=8

class asteroide(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagem1 = pygame.image.load("imagem/asteroide1.png")
        self.imagem2 = pygame.image.load("imagem/asteroide2.png")

        self.posimagem = 0

        self.listaimagens = [self.imagem1, self.imagem2]
        self.posimagem = 0
        self.imagemasteroide = self.listaimagens[self.posimagem]

        
        
        self.rect = self.imagemasteroide.get_rect()
        
        self.listadisparo = []
        self.velocidade = 20
        self.velocidadebala = 5
        self.rect.top = posy
        self.rect.left = posx

        self.configtempo = 1

    def comportamento(self, tempo):
        if self.configtempo == tempo:
            self.posimagem+=1
            self.configtempo+=1
            if self.posimagem > len(self.listaimagens)-1:
                self.posimagem = 0

    def colocar(self, superficie):
        self.imagemasteroide=self.listaimagens[self.posimagem]
        superficie.blit(self.imagemasteroide, self.rect)

        
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

    inimigo = asteroide(100,100) 

    balaprojetil = bala(largura/ 2, altura - 60)

    relogio = pygame.time.Clock()
    
    while True:
        relogio.tick(250)
        tempo = int(pygame.time.get_ticks()/1000)
        balaprojetil.trajetoria()
        Somtiro = pygame.mixer.Sound("Sons/shoot.wav")#CARREGAR SOM TIRO
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
                    Somtiro.play()
            
                    
                    
                    
        tela.blit(imagemfundo, (0,0))
        balaprojetil.colocar(tela)
        jogador.colocar(tela)
        inimigo.colocar(tela)
        inimigo.comportamento(tempo)
        
        
        if len(jogador.listadisparo) > 0:
            for x in jogador.listadisparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.top < 0:
                    jogador.listadisparo.remove(x)
        pygame.display.update()
            

invasaoespaco()
