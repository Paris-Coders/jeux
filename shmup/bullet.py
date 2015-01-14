#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python m'oblige à faire une classe dans un tel cas (pour contenir plusieurs éléments dans un objet).
class Entity:
	"""
	Une bullet est proche de l'entité. Elle contient un sprite, une position
	mais aussi une direction (dx/dy).
	
	La fonction __init__() est un constructeur. Celle-ci permet de remplir la classe
	avec ses valeurs (passés en paramètres, ou par défaut)
	"""

	def __init__(self, sprite=None, x=0, y=0, dx=1, dy=0):
		self.sprite = sprite
		self.x = x
		self.y = y
		
		self.dx=dx
		self.dy=dy
