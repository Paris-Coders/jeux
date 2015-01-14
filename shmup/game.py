#!/usr/bin/python
# -*- coding: utf-8 -*-

def render(screen):
	"""Affiche les éléments du jeu
	
	Paramètres:
	screen - l'écran où afficher le jeu
	"""

def update():
	"""Met à jour l'état du jeu"""

def run():
	"""
	Fonction principale du jeu.
	La boucle du jeu se trouve ici.
	"""
	screen = None # Contiendra la variable de l'écran (pygame).
	
	isRunning = True
	
	
	# Boucle principale
	while isRunning:
		render(screen)
		update()
		
		# Ici, un test pour vérifier si l'utilisateur quitte la fenêtre
		# doit être rajouté. Si c'est le cas, la variable isRunning doit être
		# modifiée pour forcer la fin de la boucle
