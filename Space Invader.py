import pygame
import time
import sys
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,215,0)
LAVA = (255,69,0)


v = 8
#variaveis
pontos = 0
naves=[]


def nave(screen, x, y):
    # Legs
    pygame.draw.line(screen, WHITE, [10 + x, -15 + y], [50 + x, 8 + y], 7)
    pygame.draw.line(screen, WHITE, [10 + x, -15 + y], [-30 + x, 8 + y], 7)


def shoot1(screen, x, y):
    global bullets
    # Head
    




# Setup
pygame.init()

# Set the width and height of the screen [width,height]
size = [1200, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("keyboard game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# POSICAO NAVE
x_coord = 560
y_coord = 650

#Audio
pygame.mixer.music.load("Sons/37.mp3")
pygame.mixer.music.play(3)

#Imagem de Fundo
# Set positions of graphics
import pygame
image_position = [0, 0]

 
# Load and set up graphics.
my_image = pygame.image.load("imagem/galaxy2.png").convert()
my_image = pygame.transform.scale(my_image, (1200,700))


shoot = 0

bullets = []

click_sound = pygame.mixer.Sound("sons/tiro.ogg")

# -------- Main Program Loop -----------
while not done:
    screen.fill(WHITE)
    # --- Event Processing
    for event in pygame.event.get():

    
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
    
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -v
                
            elif event.key == pygame.K_RIGHT:
                x_speed = v
                
            if event.key == pygame.K_SPACE:
                shoot = True
                x_shoot = x_coord + 4
                y_shoot = y_coord - 48   

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_LEFT:
                x_speed = 0

            
                

    # --- Game Logic




    # Move the object according to the speed vector.
    #---Tiro da nave---#
    



    #---Barramento da nave---#
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    if x_coord > 1140:
        x_coord=1145
    if x_coord <40:
        x_coord=35

    # --- Drawing Code
    screen.blit(my_image, image_position)
    
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.

    nave(screen, x_coord, y_coord)
    if shoot == True:
        shoot1(screen, x_shoot, y_shoot)
        screen.blit(tiro, postiro)
        pygame.display.flip()
        y_shoot -= 5

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit frames per second

    clock.tick(80)

# Close the window and quit.
pygame.quit()
