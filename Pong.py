#pygame stuff
import pygame, time, math, random

pygame.init()

#varibles
 
WIDTH , HEIGHT = 800 , 550
FONT = pygame.font.Font(None, 36)
GRAY = (105,105,105)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
FPS = 120

collisions = 0

paddle_width = 10
paddle_height = 75

player_x, player_y = WIDTH-50, HEIGHT/2 - (paddle_height/2)
NPC_x, NPC_y = 50, player_y
ball_x, ball_y = WIDTH/2 , HEIGHT/2

ball_size = 10 # 10 by 10
ball_angle = random.randint(80,100)
ball_speed = 2.5
ball_eraser_x, ball_eraser_y = ball_x, ball_y

left_edge_x, left_edge_y = WIDTH-50, HEIGHT/2
right_edge_x, right_edge_y = 50, HEIGHT/2
edge_height = HEIGHT/2
edge_width = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
  
#naming sprites
  ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
  ball_eraser = (ball_eraser_x, ball_eraser_y, ball_size, ball_size)
  player_rect = pygame.Rect(player_x,player_y, paddle_width, paddle_height)
  player_hitbox_1 = pygame.Rect(player_x-10, player_y, paddle_width+10, paddle_height/3)
  player_hitbox_2 = pygame.Rect(player_x-10, player_y+paddle_height/3, paddle_width+10, paddle_height/3)
  player_hitbox_3 = pygame.Rect(player_x-10, player_y+paddle_height-paddle_height/3, paddle_width+10, paddle_height/3)
  NPC_hitbox_1 = pygame.Rect(NPC_x+10, NPC_y, paddle_width+10, paddle_height/3)
  NPC_hitbox_2 = pygame.Rect(NPC_x+10, NPC_y+paddle_height/3, paddle_width+10, paddle_height/3)
  NPC_hitbox_3 = pygame.Rect(NPC_x+10, NPC_y+paddle_height-paddle_height/3, paddle_width+10, paddle_height/3)

#drawing sprites  
  pygame.draw.rect(screen, GRAY, (player_rect))
  pygame.draw.rect(screen, BLACK,(ball_rect))

#wall collision
  if ball_y <= 0:
    ball_angle = -ball_angle+540
    ball_touching_top_wall = True
  else:
    ball_touching_top_wall = False
    
  if ball_y >= HEIGHT:
    ball_angle = -ball_angle+540
    ball_touching_bottom_wall = True
  else:
    ball_touching_bottom_wall = False
      
#collision detection
  if ball_rect.colliderect(player_hitbox_1):
    ball_angle = -ball_angle+random.randint(-10, -5)
  if ball_rect.colliderect(player_hitbox_2):
    ball_angle = -ball_angle
  if ball_rect.colliderect(player_hitbox_3):
    ball_angle = -ball_angle+random.randint(5, 10)
  if ball_rect.colliderect(NPC_hitbox_1):
    ball_angle = -ball_angle+random.randint(5, 10)
  if ball_rect.colliderect(NPC_hitbox_2):
    ball_angle = -ball_angle
  if ball_rect.colliderect(NPC_hitbox_3):
    ball_angle = -ball_angle+random.randint(-10, -5)

#error fixing
  if ball_rect.colliderect(player_hitbox_2) and ball_rect.colliderect(player_hitbox_3):
    x = random.randint(0,1)
    if x == 1:
      ball_angle = -ball_angle
    if x == 2:
      ball_angle = -ball_angle+random.randint(5, 10)  
  if ball_rect.colliderect(player_hitbox_1) and ball_rect.colliderect(player_hitbox_2):
    x = random.randint(0,1)
    if x == 1:
      ball_angle = -ball_angle+random.randint(-10, -5)
    if x == 2:
      ball_angle = -ball_angle
  if ball_rect.colliderect(NPC_hitbox_2) and ball_rect.colliderect(NPC_hitbox_3):
    x = random.randint(0,1)
    if x == 1:
      ball_angle = -ball_angle
    if x == 2:
      ball_angle = -ball_angle+random.randint(5, 10)  
  if ball_rect.colliderect(NPC_hitbox_1) and ball_rect.colliderect(NPC_hitbox_2):
    x = random.randint(0,1)
    if x == 1:
      ball_angle = -ball_angle+random.randint(-10, -5)
    if x == 2:
      ball_angle = -ball_angle
      
  if ball_touching_bottom_wall is True:
    NPC_rect = pygame.Rect(NPC_x, paddle_height, paddle_width+10, paddle_height)
  if ball_touching_top_wall is True:
    NPC_rect = pygame.Rect(NPC_x, 800, paddle_width+10, paddle_height)
    
#erasing ball trail
  if ball_eraser_x != ball_x:
    pygame.draw.rect(screen, BLACK,(ball_eraser_x-15, ball_y-15, 30,30))
    ball_eraser_x = ball_x
  if ball_eraser_y != ball_y:
    pygame.draw.rect(screen, BLACK,(ball_x-15, ball_eraser_y-15, 30, 30))
    ball_eraser_y = ball_y

#erasing NPC trail
  if ball_y != NPC_y:
    pygame.draw.rect(screen, BLACK, (NPC_x, NPC_y, paddle_width, paddle_height))
    NPC_y = ball_y
    pygame.draw.rect(screen, GRAY, (NPC_x, ball_y, paddle_width, paddle_height))
    
#movement  
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or event.key == pygame.K_w:
          pygame.draw.rect(screen, BLACK, (player_rect))
          player_y -= 30
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
          pygame.draw.rect(screen, BLACK, (player_rect))
          player_y += 30
          
  ball_x += math.sin(ball_angle*math.pi/180)*ball_speed
  ball_y += math.cos(ball_angle*math.pi/180)*ball_speed
  pygame.draw.rect(screen, GRAY,(ball_rect))    
    
    
  pygame.display.flip()
  clock.tick(FPS)
