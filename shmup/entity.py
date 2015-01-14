#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python m'oblige à faire une classe dans un tel cas (pour contenir plusieurs éléments dans un objet).
class Entity:
	"""
	Une entité contient le sprite de l'objet à afficher et sa position
	"""
	
	def __init__(self):
		sprite = None
		x = 0
		y = 0
