# Introduction

Ce cours sur les jeux vidéo fait directement suite au [précédent cours](https://github.com/Paris-Coders/jeux/blob/master/cours-4.md).
De plus, pour ce cours, je vous ai préparé un petit pack de ressources afin de ne pas perdre de temps à chercher et modifier des sprites pour notre jeu. Vous pouvez le télécharger ici : https://1fichier.com/?vd6cx71psj ou ici : http://alexandre-laurent.developpez.com/ressources/shoot/SpritePack.zip. J'ai récupéré les images grâce à la liste des sites de ressources disponible ici : http://jeux.developpez.com/medias/.
Ce nouveau cours a parcouru les points suivants :
 * ré-organisation du code ;
 * ralentissement de la boucle de jeu ;
 * gestion des vaisseaux et des projectiles.


# Ré-organisation du code

Le code que nous avons jusque là ne faisait qu'afficher une balle et la déplacer. Malgré tout, il faisait déjà trente ligne et plusieurs sections se distinguaient très clairement :
 * l'initialisation et chargement des données ;
 * la gestion des touches ;
 * l'affichage.

Ce sont des sections qui sont présentes dans tous les jeux vidéo. Comme nous allons faire un programme qui va grossir avec le temps, il faut l'organiser. Nous allons donc faire des fonctions, qui vont rappeler/souligner les sections que l'on distingue. Pour rappel, une fonction ne doit faire qu'une et une unique chose. D'ailleurs, son nom indique l'action qu'elle fait.
L'avantage de faire des fonctions c'est que par la suite, nous allons pouvoir les déplacer dans de nouveaux fichiers pour encore mieux organiser le code. Pour l'instant, il n'y a pas encore ce besoin.
Voici le nouveau code, une fois réorganisée :

```python
#!/usr/bin/python

import pygame
import sys

# Variable globales
playerSprite=None
playerRect=None

# Fonctions
def loadData():
	global playerSprite
	global playerRect
   
	playerSprite = pygame.image.load("./data/player.png")
	playerRect = playerSprite.get_rect()
   

def display():
	screen.fill((0,30,30))
   
	screen.blit(playerSprite,playerRect)
   
	pygame.display.flip()
   
def update():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	   
	keysState = pygame.key.get_pressed()
	if keysState[pygame.K_ESCAPE]:
		sys.exit()
	if keysState[pygame.K_RIGHT]:
		playerRect.x+=1
	if keysState[pygame.K_LEFT]:
		playerRect.x-=1


# Le programme démarre ici
pygame.init()

screen = pygame.display.set_mode((320,240))

loadData()

# Boucle de jeu
while 1:
	display()
	update()
```

# Ralentissement de la boucle de jeu

En lisant ce titre, vous pouvez penser que je suis tombé sur la tête. En effet, quel est l'intérêt de ralentir un jeu ?
Regardez bien, notamment, si vous lancez votre gestionnaire de tache. Le programme actuel, rien que pour afficher une balle, utilise 100 % du CPU (ou 100/nombre_de_coeur). C'est aberrant, même si au final, on pourrait estimer que ce n'est pas grave. Le joueur, lorsqu'il joue, il ne fait rien d'autre avec sa machine. Cette réflexion était vraie il y a quelque 10 ans. Maintenant, nous avons des jeux sur nos téléphones portables. Le fait d'utiliser 100 % du CPU entraîne une diminution significative de l'autonomie de la machine. En effet, sur portable, il est mille fois mieux, d'avoir un jeu qui consomme le moins de ressources possibles.
Il y a un second souci, c'est la vitesse de déplacement de la balle. Actuellement, le code (notamment celui dans la boucle) est parcouru le plus rapidement possible par l'ordinateur. Ça veut aussi dire, que là, vous affichez plus de 1000 fois la balle, par seconde. C'est inutile.

## Mise en place d'un compteur de FPS

Pour mieux se rendre compte de ce phénomène, nous allons mettre un compteur de FPS (Image par Seconde). Comment ? Nous affichons une image à chaque passage de la boucle while. Donc, il nous suffit de rajouter un compteur, pour avoir le nombre d'image.
Ensuite, le compteur de FPS est un compteur qui se base sur les secondes. Il suffit donc d'exécuter une action (affichage/réinitialisation du compteur) chaque seconde. Avec Pygame, vous pouvez obtenir le nombre de millisecondes depuis le début de l'exécution du programme : `pygame.time.get_ticks()`. Il suffit de vérifier si depuis le précédent affichage, il s'est passé une seconde. Voici le code :

```python
oldTime = 0
nbFrames = 0
while 1:
	display()
	update()
   
   
	if pygame.time.get_ticks() - oldTime > 1000:
		print "FPS : " + str(nbFrames)
		oldTime = pygame.time.get_ticks()
		nbFrames = 0
```

Note : le fait d'afficher du texte dans la console (avec print) est lent (cela peut prendre quelques millisecondes). Si vous avez un souci de performance, cela peut venir de print.

## Mise en place du contrôle des FPS

Maintenant, il faut ralentir notre jeu. Nous voulons une limite à 60 FPS (par héritage de nos anciens écrans cathodiques qui étaient souvent à 60 Hz). L'astuce est de dire : si l'affichage et l'update (si un tour de boucle) a pris moins de 16 ms alors, nous pouvons attendre (mettre en pause le programme).

Il est possible de le coder soit même. Il n'y a absolument rien de compliquer. Toutefois, au lieu de refaire la roue, nous pouvons simplement utilisez les fonctionnalités de Pygame. Ici, Pygame propose un objet "Clock" (http://www.pygame.org/docs/ref/time.html) qui permet de définir une limite.

Voici le résultat :

```python
oldTime = 0
nbFrames = 0
fpsLimiter = pygame.time.Clock()
while 1:
	display()
	update()
   
	fpsLimiter.tick(60)

	if pygame.time.get_ticks() - oldTime > 1000:
		print "FPS : " + str(nbFrames)
		oldTime = pygame.time.get_ticks()
		nbFrames = 0
```

Par contre, si vous exécutez le programme, vous verrez souvent afficher : 62 FPS. Pas de panique. C'est simplement que Pygame utilise un timing en milliseconde. Le temps par image, lorsque l'on veut du 60 FPS est de : 16.666... ms (1000/60). Comme Pygame utiliser des entiers, il ne lui est pas possible de faire plus précis. Du coup, le jeu est cadencé à 62 FPS et cela ne gêne absolument pas.

## Mise en place d'un delta

Il reste un dernier problème. Si vous exécutez le jeu sur un PC plus lent, ou si l'anti virus se déclenche, le jeu a de forte chance de ralentir et de ne plus pouvoir maintenir les 60 FPS. Si cela est le cas, la vitesse de déplacement de la balle va varier. En effet, actuellement, nous ajoutons simplement +1 à la position de la balle. Cela veut dire que lorsque nous obtenons 60 FPS, elle peut bouger de 60px par seconde. Par contre, si nous sommes bloqué à 30 FPS, elle ne bougera qu'à 30px par seconde.
Cette différence n'est pas acceptable. En effet, les game designer qui vont créer les règles du jeu, ne veulent pas que les règles changent de PC en PC, sinon, l'expérience de jeu ne sera plus la même. Pour régler ce souci, il faut intégrer une notion de delta.
Le delta, c'est le temps entre deux affichage/deux mise à jour du jeu. Pour le calculer, il suffit de prendre le temps actuel et de le soustraire avec le temps lors du tour précédent :

```python
fpsLimiter = pygame.time.Clock()
deltaTime = 0
oldTime = 0
while 1:
	display()
	update(deltaTime)
   
	fpsLimiter.tick(60)
	curTime = pygame.time.get_ticks()
	deltaTime = curTime - oldTime
	oldTime = curTime
```

Lorsque le jeu fonctionne à 60 FPS, le deltaTime est de 16/17.
Lorsque le jeu fonctionne à 30 FPS, le deltaTime est de 32/33.
On donne le deltaTime à la fonction `update()` afin qu'elle puisse l'utiliser pour intégrer ce delta dans la vitesse de déplacement de la balle :

```python
def update(deltaTime):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	   
	keysState = pygame.key.get_pressed()
	if keysState[pygame.K_ESCAPE]:
		sys.exit()
	if keysState[pygame.K_RIGHT]:
		playerRect.x+=1 * deltaTime
	if keysState[pygame.K_LEFT]:
		playerRect.x-=1 * deltaTime
```

Vous avez ainsi, un jeu, qui peu importe la vitesse du PC, fonctionnera toujours de la même façon.

# Progression dans le Shoot'em'up

Maintenant que nous avons une bonne base, du code propre et fiable, nous pouvons ajouter des éléments à notre jeu. Par exemple, il est très facile d'ajouter un enemi. Il suffit de rajouter le chargement d'un sprite dans la fonction `loadData()` et ajouter une ligne pour le copier, dans la fonction `display()`.
Certes, il ne bouge pas, mais au moins, notre vaisseau aura une cible pour tirer dessus.

On remarque aussi, que chaque élément dans notre jeu à besoin de deux variables :

 * le sprite à afficher ;
 * le rectangle pour positionner ce sprite à l'écran.

Maintenant, parlons des projectiles (bullets).

Tous les projectiles utilisent le même sprite. Donc il n'y a qu'une seule variable à faire pour conserver le sprite utiliser pour les projectiles. Par contre, pour chaque projectile, il faut une position, sa position sur l'écran. Donc, nous allons garder la position de chacun des projectiles dans un tableau.

Dans la fonction `display()` : nous parcourons ce tableau avec une boucle for, pour afficher chaque projectile

Si nous faisons ainsi, le projectile restera fixe à l'écran, ce n'est pas super pour un projectile. Du coup, dans la fonction update() nous pouvons rajouter un code pour le déplacer. À l'identique de la fonction `display()`, la fonction `update()` contiendra donc une boucle for pour parcourir tous les projectiles et les déplacer. Bien, nous les déplaçons, mais de une, ils sortent de l'écran, de deux, il traverse l'ennemi.
Pour le premier cas, on peut rajouter un simple test pour savoir si le projectile est sorti de l'écran. Dans un tel cas, alors, nous le supprimons.
Pour le second cas, le test est de savoir si le projectile touche l'ennemi. Plus précisément, chaque objet dans notre jeu est compris dans un rectangle. Le rectangle contient la position (le point en haut à gauche) et la largeur et hauteur. Donc, pour savoir si le projectile touche l'ennemi, il faut savoir si le rectangle du projectile, touche celui de l'ennemi.
Nous allons faire une fonction pour tester cette condition. La fonctionne accepte en paramètre deux éléments : les deux rectangles à tester.

Pour trouver quel sont les bons tests à faire, je vous conseille de prendre une feuille de papier et de dessiner les différents cas possibles.

Lorsque le projectile touche l'ennemi, il suffit de faire en sorte de ne plus afficher l'ennemi et de supprimer le projectile.

Lorsque le joueur appuie sur la barre espace, un projectile est crée. Pour cela, il suffit de rajouter un élément dans la liste, les boucles présentes dans `display()` et `update()` gérerons le nouveau projectile sans difficultés.


# Exercices

 * Améliorez le jeu, pour qu'il prenne en compte tous ce qui vient d'être vu. Au final, vous devez avoir un joueur qui tire des projectiles et qui détruit l'ennemi ;
        la détection de collision entre rectangle est classique en jeux vidéo. C'est un peu comme une roue :)
 * Vous pouvez faire en sorte que les ennemies bougent :)
 * N'hésitez pas à améliorer le code pour le rendre plus générique (gestion de plusieurs ennemis sans avoir énormément de variable ...)
