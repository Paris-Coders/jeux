#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python m'oblige à faire une classe dans un tel cas (pour contenir plusieurs éléments dans un objet).
class Explosion:
	"""
	Une explosion contient le sprite de l'objet à afficher, sa position
	et un compteur de temps
	L'explosion inclut aussi imageX et imageY permettant de savoir quel sous image
	afficher. Ceux-ci seront mis à jour (ainsi que counteur) dans la fonction updateExplosion
	
	La fonction __init__() est un constructeur. Celle-ci permet de remplir la classe
	avec ses valeurs (passés en paramètres, ou par défaut)
	"""

	def __init__(self, sprite=None, x=0, y=0):
		self.sprite = sprite
		self.x = x
		self.y = y
		self.counter=0
		
		# Valeurs pour l'affichage
		self.imageX = 0
		self.imageY = 0
		

def updateExplosion(deltaTime, explosion):
	"""Mise à jour d'une explosion
	
	Paramètres:
	deltaTime - le temps depuis la dernière mis à jour
	explosion - l'explosion a mettre à jour
	
	Valeur de retour:
	True si l'explosion est toujours active, sinon False (et devra être supprimé)
	"""
	# [TODO] Appliquer le code du cours (animation)
	return True
