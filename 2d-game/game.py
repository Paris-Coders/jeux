#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame

screenSize=(640,480)

# Ce sont des dictionnaires, afin de retrouver un sprite (ou un son) à partir de son nom
spriteData = {}


""" 
Plusieurs techniques existe pour gérer les entité. Vous pouvez par exemple
dire que la toute première entité du jeu est le joueur (une entité dont les x/y
sont controllés à l'aide du clavier)
"""


def loadData():
	"""Charge les données du jeu"""
	
	# Permet d'avoir accès aux variables globales (et non d'avoir de nouvelle variable avec les mêmes noms)
	global spriteData
	
	# [TODO] On charge les sprites dont nous avons besoin
	
	# [TODO] On doit aussi lire le fichier de la carte et la charger.

def render(screen):
	"""Affiche les éléments du jeu
	
	Paramètres:
	screen - l'écran où afficher le jeu
	"""
	screen.fill((0,30,30))
	
	# [TODO] Affiche la carte
	# Il y a un "piège". La carte est constituée de plusières couches
	
	pygame.display.flip()
	

def update(deltaTime):
	"""Met à jour l'état du jeu
	
	Paramètres:
	deltaTime - le temps entre deux update (souvent 16ms)
	"""
	# Cette fois, il n'y a rien à faire ici.
	# Les choses que l'ont pourrait tout de même faire :
	# - animations de certains sprites (mouvement de l'eau)
		

def run():
	"""
	Fonction principale du jeu.
	La boucle du jeu se trouve ici.
	"""
	screen = pygame.display.set_mode(screenSize)
	
	isRunning = True
	
	loadData()
	
	# Boucle principale
	fpsLimiter = pygame.time.Clock()
	while isRunning:
		deltaTime = fpsLimiter.get_time()
		render(screen)
		update(deltaTime)
		
		fpsLimiter.tick(60)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
