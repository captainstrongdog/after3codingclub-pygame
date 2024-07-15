import pygame, sys, math, random, time

# Initialize Pygame
pygame.init()

# Constants
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255, 255, 255)
FPS = 60 


# Initialize the screen
WIDTH, HEIGHT = 800, 550#change the numbers to adjust the screen size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

player_size = 50
player_x, player_y = HEIGHT/2, WIDTH/2
player_eraser_x, player_eraser_y =  player_x, player_y#this sprite is in charge of erasing the player's trail

# game loop
running = True
while running:
  
  player_rect = pygame.Rect(player_x,player_y, player_size, player_size)
  player_eraser_rect = pygame.Rect(player_eraser_x, player_eraser_y, player_size, player_size)
  
#movement
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        player_y -= 10
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        player_y += 10
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player_x -= 10
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        player_x += 10
        
#erase the players trail
  if player_eraser_y != player_y:
    pygame.draw.rect(screen, BLACK, (player_eraser_x, player_eraser_y, player_size, player_size))
    player_eraser_y = player_y
    pygame.draw.rect(screen, RED, (player_eraser_x, player_eraser_y, player_size, player_size))
  if player_eraser_x != player_x:
    pygame.draw.rect(screen, BLACK, (player_eraser_x, player_eraser_y, player_size, player_size))
    player_eraser_x = player_x
    pygame.draw.rect(screen, RED, (player_eraser_x, player_eraser_y, player_size, player_size))
    
  pygame.display.set_caption("points:")
  text = font.render(f"press the arrow keys to start, use the arrow keys to move.", True, WHITE)
  screen.blit(text, (10, 10))

    
    
# Update the display
  pygame.display.flip()

# Cap the frame rate
  clock.tick(FPS)
