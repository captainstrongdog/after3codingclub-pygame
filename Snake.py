import pygame, sys, math, random, time

# Initialize Pygame
pygame.init()

# Constants
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255, 255, 255)
FPS = 60


# Initialize the screen
WIDTH, HEIGHT = 800, 550 # Change the numbers to adjust the screen size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption
clock = pygame.time.Clock()

player_size = 50
player_x, player_y = HEIGHT/2, WIDTH/2
player_drawer_x, player_drawer_y =  player_x, player_y # This sprite is in charge of drawing the player
length = 3
player_dir = 90
player_speed = 2

# Game loop
running = True
while running:
  
  player_rect = pygame.Rect(player_x,player_y, player_size, player_size)
  player_drawer_rect = pygame.Rect(player_drawer_x, player_drawer_y, player_size, player_size)
  
        
# Drawing the player
  if player_drawer_y != player_y:
    pygame.draw.rect(screen, BLACK, (player_drawer_rect))# This is to erase the trail
    player_drawer_y = player_y
    pygame.draw.rect(screen, RED, (player_rect))
  if player_drawer_x != player_x:
    pygame.draw.rect(screen, BLACK, (player_drawer_rect))
    player_drawer_x = player_x
    pygame.draw.rect(screen, RED, (player_rect))

  # Player movement
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        player_dir = 180
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        player_dir = 0
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player_dir = 270
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        player_dir = 90
    
  player_x += math.sin(player_dir*math.pi/180)*player_speed
  player_y += math.cos(player_dir*math.pi/180)*player_speed  

  
# Update the display
  pygame.display.flip()

# Cap the frame rate
  clock.tick(FPS)
