# Boring pygame stuff below :)
import pygame, sys, math, random, time
 
# Initialize Pygame
pygame.init()

# Constants
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FPS = 60
font = pygame.font.Font(None, 36)

# Screen stuff
WIDTH, HEIGHT = 1500, 550#change the numbers to adjust the screen size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption
clock = pygame.time.Clock()
screen.fill(WHITE)

# Player stuff
player_size = 50
player_x, player_y = WIDTH/2, 450
player_drawer_x, player_drawer_y =  player_x, player_y#this sprite is in charge of drawing the player
player_dir = 90
player_speed = 1

# Bullet stuff
bullet_width, bullet_height = 10, 25
bullet_x, bullet_y = player_x, player_y
bullet_speed = 10
shooting = False
bullet_drawer_x, bullet_drawer_y = bullet_x, bullet_y

# Other junk
last_key = 0
points = 0

# Game loop
running = True
while running:
  
  player_rect = pygame.Rect(player_x,player_y, player_size, player_size)
  player_drawer_rect = pygame.Rect(player_drawer_x, player_drawer_y, player_size, player_size)
  bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
  bullet_drawer_rect = pygame.Rect(bullet_drawer_x, bullet_drawer_y, bullet_width, bullet_height)
        
  if not shooting:      
    bullet_x = player_x+player_size/2
    bullet_drawer_x = bullet_x
        
# Drawing the player
  if player_drawer_x != player_x:
    pygame.draw.rect(screen, WHITE, (player_drawer_rect))
    player_drawer_x = player_x
    pygame.draw.rect(screen, RED, (player_rect))

# Drawing the bullet
  if bullet_drawer_y != bullet_y:
    pygame.draw.rect(screen, WHITE, (bullet_drawer_rect))
    bullet_drawer_y = bullet_y
    pygame.draw.rect(screen, RED, (bullet_rect))

# moving the bullet
  if shooting:
    bullet_y -= bullet_speed
    if bullet_y <= 0:
      bullet_x, bullet_y = player_x, player_y
      shooting = False
      
# Player keyboard stuff
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player_dir = 270
        last_key = "left"
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        player_dir = 90
        last_key = "right"
# Bullet keyboard stuff
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        if not shooting:
          shooting = True
  
# Player_movement
  player_x += math.sin(player_dir*math.pi/180)*player_speed
  player_y += math.cos(player_dir*math.pi/180)*player_speed  

# Update the display
  pygame.display.flip()

# Cap the frame rate
  clock.tick(FPS)
