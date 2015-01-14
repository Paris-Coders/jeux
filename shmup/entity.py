#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python m'oblige à faire une classe dans un tel cas (pour contenir plusieurs éléments dans un objet).
class Entity:
	"""
	Une entité contient le sprite de l'objet à afficher et sa position
	
	La fonction __init__() est un constructeur. Celle-ci permet de remplir la classe
	avec ses valeurs (passés en paramètres, ou par défaut)
	"""

		
	def __init__(self, sprite=None, x=0, y=0):
		sprite = sprite
		x = x
		y = y
		
