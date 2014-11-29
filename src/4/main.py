#!/usr/bin/python

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((320,240))

ball = pygame.image.load("./data/ball.gif")
ballrect = ball.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
		
	keysState = pygame.key.get_pressed()
	if keysState[pygame.K_RIGHT]:
		ballrect.x+=1
			
	# Clear screen
	screen.fill((0,30,30))
	screen.blit(ball,ballrect)
			
	pygame.display.flip()
