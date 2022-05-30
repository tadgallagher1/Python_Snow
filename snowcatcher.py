
#import 
import pygame
import random

# Initialize Pygame
pygame.init()


# Define Some Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN =  (0,255,0)
RED = (255,0,0)

class Block():
    pass

class Player():
    pass

# Screen width/height variables
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

maxFlakes = 50

# This is a list of the 'sprites'.  Each block in the program
# is added to this list.  The list is managed by a class called 'Group'.
block_list = pygame.sprite.Group()

# This is a list of every sprite.  All bocks and the ployer block also.
all_sprites_list = pygame.sprite.Group()

# Create a loop - Snow Flakes
for i in range(maxFlakes):
    color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    width = 40
    height = 30 
    block = Block(color, width, height)
    
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    block_list.add(block)
    all_sprites_list(block)
    
# Create main player
player = Player(BLACK, 20, 15)    
all_sprites_list(player)

# Scoring variable
score = 0

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loop until the user closes the button in the upper right corner.
done = False
while not done:
    
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:
            done = True
            
            

# Quit the game - Exit Loop
pygame.quit()             