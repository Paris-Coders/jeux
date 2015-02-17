#!/usr/bin/python
import pygame
import sys

import filler

screenWidth=640
screenHeight=480
gridWidth = 20
gridHeight = 20
tileWidth = screenWidth/gridWidth
tileHeight = screenHeight/gridHeight

def createGrid(sizeX, sizeY):
	grid = [[]] * sizeX
	for x in range(len(grid)):
		grid[x] = [0] * sizeY
		
	return grid

def clearGrid(grid):
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			grid[x][y] = 0

def display(grid):
	screen.fill((0,0,30))
	
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			if grid[x][y] != 0:
				screen.fill((255,0,0), [x * tileWidth, y * tileHeight, tileWidth,tileHeight])
	
	pygame.display.flip()
		
	
def update(grid):
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
	
	if pygame.mouse.get_pressed()[0] == True:	
		mouse_pos=pygame.mouse.get_pos()
		grid_pos = ( mouse_pos[0] / tileWidth, mouse_pos[1] / tileHeight )
		#grid[mouse_pos[0] / tileWidth][mouse_pos[1] / tileHeight] = 1
		filler.fillGrid(grid,grid_pos[0], grid_pos[1],4)
	
	keysState = pygame.key.get_pressed()
	if keysState[pygame.K_ESCAPE]:
		sys.exit()
	if keysState[pygame.K_SPACE]:
		clearGrid(grid)

pygame.init()

screen = pygame.display.set_mode((screenWidth,screenHeight))

grid = createGrid(gridWidth,gridHeight)

while 1:
	display(grid)
	update(grid)
