#!/usr/bin/python
# -*- coding: utf-8 -*-
from entity import *
from explosion import *

# Ce sont des dictionnaires, afin de retrouver un sprite (ou un son) à partir de son nom
spriteData = {}
soundsData = {}

# Listes d'Entity
player = Entity()
enemies = []
# On peut aussi ajouter des bonus, qui sont d'autres entités, encore

explosions = []

""" 
Plusieurs techniques existe pour gérer les entité. Vous pouvez par exemple
dire que la toute première entité du jeu est le joueur (une entité dont les x/y
sont controllés à l'aide du clavier)
"""


def loadData():
	"""Charge les données du jeu"""
	
	# Permet d'avoir accès aux variables globales (et non d'avoir de nouvelle variable avec les mêmes noms)
	global spriteData
	global soundsData
	
	# [TODO] On charge les sprites et autre sons dont nous avons besoin

def render(screen):
	"""Affiche les éléments du jeu
	
	Paramètres:
	screen - l'écran où afficher le jeu
	"""
	# [TODO] Efface l'écran avec une couleur (souvent noir) (pygame)
	
	# Affiche tous les éléments du jeu
	# [TODO] Affiche joueur
	for enemy in enemies:
		print "TODO affiche enemy"
		
	# [TODO] Afficher explosions
	for explosion in explosions:
		print "TODO affiche explosion"
	# [TODO] Affiche le jeu à l'écran (aussi appeler flip) (pygame)

def update(deltaTime):
	"""Met à jour l'état du jeu
	
	Paramètres:
	deltaTime - le temps entre deux update (souvent 16ms)
	"""
	
	# [TODO] Récupérer les interactions clavier pour déplacer le joueur
	
	# [TODO] Déplacer les éléments du jeu
	for enemy in enemies:
		# Déplacer les enemies (vers la gauche, par exemple)
		print "TODO update enemy"
		
	for explosion in explosions:
		updateExplosion(deltaTime,explosion)
		# Suivant le code de retour, il faut enlever l'explosion de la liste

def run():
	"""
	Fonction principale du jeu.
	La boucle du jeu se trouve ici.
	"""
	screen = None # [TODO] Contiendra la variable de l'écran (pygame).
	
	isRunning = True
	
	loadData()
	
	# Boucle principale
	# [TODO] Il faudra très certainement ralentir la boucle avec une sorte de limiteur de FPS
	while isRunning:
		render(screen)
		update(16) # [TODO] Cette valeur ne devrait pas être fixe et devrait dépendre du vrai temps entre deux appels à la fonction
		
		# [TODO]
		# Ici, un test pour vérifier si l'utilisateur quitte la fenêtre
		# doit être rajouté. Si c'est le cas, la variable isRunning doit être
		# modifiée pour forcer la fin de la boucle
