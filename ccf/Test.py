import sys
import pygame

pygame.init()
size = width,height = 1000,800
screen = pygame.display.set_mode(size)
color = (0,0,0)

ball = pygame.image.load("/home/mrxiuer/图片/Test.png")
ballrect = ball.get_rect()
clock = pygame.time.Clock()

speed = [1,1]

while True:
    clock.tick(180)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if ballrect.left <0 or ballrect.right>width:
        speed[0] = -speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1] = -speed[1]
    screen.fill(color)
    ballrect = ballrect.move(speed)
    screen.blit(ball,ballrect)
    pygame.display.flip()