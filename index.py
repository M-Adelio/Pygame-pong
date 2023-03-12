import pygame, random
from pygame.locals import *

direction = 0

velx = -10
vely = 0

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Pong")

players = [(50,250), (550,250)]
players_sprite = pygame.Surface((10,50))
players_sprite.fill((255,255,255))

ball = (290, 290)
ball_sprite = pygame.Surface((10,10))
ball_sprite.fill((255,255,255))

def p1_movement(direction,players):
    players[0] = (50, players[0][1] + direction * 9)
    if players[0][1] >= 550:
        players[0] = (50, 550)
    if players[0][1] <= 0:
        players[0] = (50, 0)

def p2_movement(ball,players):

    players[1] = (players[1][0], players [1][1] + 9) if players[1][1] < ball[1] else players[1]
    players[1] = (players[1][0], players [1][1] - 9) if players[1][1] > ball[1] else players[1]

def ball_movement(velx, vely, ball):  
    if ball[0] == 60:
        if ball[1] >= players[0][1] and ball[1] <= players[0][1] + 50:
            velx *= -1
            vely = (players[0][1] + 25 - ball[1] + 5) / -random.randint(1,4)


    if ball[0] == 540:
        if ball[1] >= players[1][1] - 10 and ball[1] <= players[1][1] + 50:
            velx *= -1
            vely = (players[1][1] + 25 - ball[1] + 5) / -3

    if ball[1] >= 600 or ball[1] <= 0:
        vely *= -1
            
    ball = (ball[0] + velx, ball[1] + vely)
    return ball, velx, vely
        
clock = pygame.time.Clock()

while True:
    
    clock.tick(20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direction = -1
                
            if event.key == K_DOWN:
                direction = 1

        if event.type == KEYUP:
            direction = 0

    screen.fill((0,0,0))

    p1_movement(direction,players)
    p2_movement(ball,players)
    ball, velx, vely = ball_movement(velx, vely, ball)
    if ball[0] >= 600:
        ball = (290, 290)
        players = [(50,250), (550,250)]
        vely = 0
        
    if ball[0] <= 0:
        pygame.quit()

    for pos in players:
        screen.blit(players_sprite,pos)

    screen.blit(ball_sprite, ball)

    pygame.display.update()
