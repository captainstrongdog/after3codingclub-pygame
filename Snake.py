import pygame, sys, math, random, time

# Initialize Pygame
pygame.init()

# Constants
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FPS = 60
last_key = 0

# Initialize the screen
WIDTH, HEIGHT = 800, 550#change the numbers to adjust the screen size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption
clock = pygame.time.Clock()

player_size = 50
player_x, player_y = WIDTH/2, HEIGHT/2
player_drawer_x, player_drawer_y =  player_x, player_y#this sprite is in charge of drawing the player
player_dir = 90
player_speed = 2

apple_size = 50
apple_x, apple_y = WIDTH/2, HEIGHT/2
apple_drawer_x, apple_drawer_y =  player_x, player_y#this sprite is in charge of drawing the player

# Game loop
running = True
while running:
  
  player_rect = pygame.Rect(player_x,player_y, player_size, player_size)
  player_drawer_rect = pygame.Rect(player_drawer_x, player_drawer_y, player_size, player_size)
  apple_rect = pygame.Rect(apple_x,apple_y, apple_size, apple_size)
  apple_drawer_rect = pygame.Rect(apple_drawer_x, apple_drawer_y, apple_size, apple_size)
  
        
# Drawing the player
  if player_drawer_y != player_y:
    pygame.draw.rect(screen, BLACK, (player_drawer_rect))#this is to erase the trail
    player_drawer_y = player_y
    pygame.draw.rect(screen, RED, (player_rect))
  if player_drawer_x != player_x:
    pygame.draw.rect(screen, BLACK, (player_drawer_rect))
    player_drawer_x = player_x
    pygame.draw.rect(screen, RED, (player_rect))

# Drawing the apple
  if apple_drawer_y != apple_y:
    pygame.draw.rect(screen, BLACK, (apple_drawer_rect))#this is to erase the trail
    apple_drawer_y = apple_y
    pygame.draw.rect(screen, BLUE, (apple_rect))
  if apple_drawer_x != apple_x:
    pygame.draw.rect(screen, BLACK, (apple_drawer_rect))
    apple_drawer_x = apple_x
    pygame.draw.rect(screen, BLUE, (apple_rect))


# Keyboard stuff
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN and last_key != "down":
      if event.key == pygame.K_UP:
        last_key = "up"
        player_dir = 180
    if event.type == pygame.KEYDOWN and last_key != "up":
      if event.key == pygame.K_DOWN:
        player_dir = 0
        last_key = "down"
    if event.type == pygame.KEYDOWN and last_key != "right":
      if event.key == pygame.K_LEFT:
        player_dir = 270
        last_key = "left"
    if event.type == pygame.KEYDOWN and last_key != "left":
      if event.key == pygame.K_RIGHT:
        player_dir = 90
        last_key = "right"
  
# Player_movement
  player_x += math.sin(player_dir*math.pi/180)*player_speed
  player_y += math.cos(player_dir*math.pi/180)*player_speed  

# Collision system
  if player_rect.colliderect(apple_rect):
    apple_x, apple_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    pygame.draw.rect(screen, BLUE, (apple_rect))
  
# Update the display
  pygame.display.flip()

# Cap the frame rate
  clock.tick(FPS)
