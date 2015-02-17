# Introduction

À vrai dire, maintenant il n'y a plus rien à rajouter sur le projet de shoot em up.
Vous avez tous les éléments pour concevoir le jeu et le finaliser. Toutefois, même si
vous avez appris la base et l'architecture d'un jeu vidéo, il nous reste quelques techniques
et procédés à découvrir. Dans cette leçon, nous allons nous pencher sur le système de tuile, notamment
utilisé dans les jeux 2D comme Zelda.
En seconde partie, nous allons aussi voir la récursivité, un procédé en informatique, permettant
de résoudre des problèmes spécifiques de manière rapide et efficace là où l'utilisation des boucles for
n'arrive pas à répondre au besoin.


# Un système de tuiles (TileMapping)

Prenons une image du jeu : The Legend of Zelda: A link to the past.

![](http://alexandre-laurent.developpez.com/ressources/zelda-link-to-the-past.jpg)

Pour rappel, ce jeu fonctionne sur Super Nintendo. Aujourd'hui, nous allons parler
de la carte (l'arrière plan) où se déplace le joueur. Une méthode naïve (très naïve)
serait de dire : on stocke sur le disque dur une image du monde et lors de l'affichage
nous copions un morceau de cette image.
Certes, cela fonctionne. Malheureusement, une image du monde complet de The Legend of Zelda: A Link to the past (sans les donjons)
fait plus de 2 Mo et cela, au format PNG (un format compressé). La mémoire vive de la console ne fait que
128 Ko. Cela va être très dur de travailler avec une si grande image.

Du coup, les développeurs ont été astucieux (comme toujours) et ont découpé la carte en petits morceaux (appelés tuiles)
et il conserve sur la cartouche et en mémoire, une carte contenant des nombres. Ces nombres indiquent quelles tuiles affichés.
On remarque par exemple, que les pierres et les buissons sont deux types de tuiles différentes.
Plus précisément, cette carte est un tableau à deux dimensions. Chaque case représente une tuile de 32px sur 32. La résolution était de 
512x448. Donc, le tableau permettant de reprensenter la carte pour cette partie de l'image est de 16x14 cases, chaque case contenant un nombre.

Lors de l'affichage, il suffit de faire un parcours du tableau cases par cases et d'afficher le sprite correspondant à la case lue.
Il est aussi très facile de connaître l'emplacement de la tuile sur l'écran, il suffit de faire `x*largeur_tuile , y*hauteur_tuile`.
Par défaut, l'affichage commence à partir de 0x0 (le coin en haut à droite). Mais Link peut se déplacer et en se déplaçant, l'écran (la fenêtre
sur le monde du jeu) doit se déplacer. Pour ce faire, on peut commencer à afficher à partir de -16 pixels et pour ne pas avoir de vide sur la droite
afficher une case de plus. À chaque image, on décalera l'origine de notre affichage, permettant ainsi de faire une translation (appelé scrolling).

Link, en plus de se déplacer, il peut soulever des pierres. Pour savoir lorsqu'il peut faire une telle action, il faut savoir où se trouve Link par rapport
aux pierres qui elles, sont enregistrés sur la carte (le tableau 2D). Prenons un exemple. J'ai Link en 280x178. Je peux rapidement déterminer sur quelle
case de ma carte il se trouve, en faisant l'opération inverse de celle utilisée pour l'affichage : `position_x_link/largeur_tuile , position_y_link/hauteur_tuile`
ce qui me donnera les coordonées sur la carte 8x5. Ainsi, s'il regarde à droite et que le joueur essaie de soulever une pierre, il me suffit de vérifier
que sur la carte, à la position 9x5, il y a une pierre. Si oui, alors il peut la soulever et le jeu enclenchera l'animation de soulèvement de la pierre.


## Les tableaux à deux dimensions

En Python, un tableau à deux dimensions est souvent implémenté comme une liste, contenant elle même des listes :
```python
	grid = [[]] * sizeX
	for x in range(len(grid)):
		grid[x] = [0] * sizeY
```
Ou encore plus simplement :
```python
	grid = [[0] * sizeY] * sizeX
```
L'accès à un des éléments est classique et évident :
```python
	grid[x][y]
```
où `x` et `y` sont des index (donc des nombres) indiquant la case que vous voulez accéder.

## Deux dimensions en une

Une astuce permet, dans un tableau à une dimension, de simuler la présence de deux. Plus précisement
nous n'avons qu'un tableau à une dimension (une liste simple) et nous souhaitons toujours accéder aux cases avec des coordonnées
x et y.
Prenons une liste remplie séquentiellement :
```python
	l = range(9)
```
On obtient :
```
	[0, 1, 2, 3, 4, 5, 6, 7, 8]
```
Mais, on veut que ce tableau de neuf cases, simule un tableau 2D de 3 sur 3 cases.
Soit :
```
	0, 1, 2
	3, 4, 5
	6, 7, 8
```
Pour cela, il nous faudra un peu de mathématiques. Regardons ce qui se passe :
* Les coordonnées 0,0 correspondent à la case 0
* Les coordonnées 1,0 correspondent à la case 1
* Les coordonnées 2,0 correspondent à la case 2
* Les coordonnées 0,1 correspondent à la case 3
* Les coordonnées 1,1 correspondent à la case 4
* ...
* Les coordonnées 2,2 correspondent à la case 8
Dans les variables disponibles, nous avons : x et y, la largeur (3) et la hauteur (3) du tableau. Pour les trois premières cases `x` donne directement le résultat.
Mais dès que l'on passe sur la seconde ligne, on obtient 3 et après, pour la case 4, on à 3+1. On pourrait continuer comme cela longtemps. D'ailleurs
une autre case intéressente à vérifier, c'est la case 6 qui correspond aux coordonnées 0,2. La formule que nous pouvons en déduire est : `x + y * largeur_du_tableau`
Ainsi, avec cette formule, nous pouvons utiliser des coordonnées 2D, pour accéder à un tableau 1D.


# La récursivité

La récursivité désigne le fait d'appeler une fonction à l'intérieur de cette même fonction.
Par exemple :
```python
	def foo():
		print "Fonction foo"
		foo()
```

Hum, soit. Mais à quoi cela peut bien servir ? À vrai dire, il arrive quelques fois que la méthode itérative (avec une boucle for)
ne permette pas de résoudre une problématique. Par contre, le même problème peut être résolu en très peu de ligne, avec une fonction récursive.

Pour faire une récursivité efficace (sans bogue/crash), il faut se rappeler de deux règles :
* une fonction récursive est une fonction qui s'appelle elle même ;
* la récurisivité doit avoir une condition d'arrêt.
En effet, le code que j'ai montré ci-dessus ne va jamais s'arrêter. C'est une boucle infinie (sans boucle) où `foo()` va toujours
se rappeler. En réalité, en informatique, chaque appel de fonction coute un peu de mémoire (qui est libérée à la fin de la fonction appelée). Le fait
de faire une fonction récursive comme `foo()` fait qu'à chaque appel, un peu plus de mémoire est utilisée et comme on n'en sort jamais,
celle-ci n'est jamais libérée. Au bout d'un moment, la mémoire est pleine et votre programme crashe.

L'exemple le plus simple en récursivité est : la [factorielle](https://fr.wikipedia.org/wiki/Factorielle).
Celle-ci se code très facilement :
```python
	def fact(n):
		if n < 2:
			return 1
		else
			return n * fact(n-1)
```

Voilà. On remarque que la condition d'arrêt est `n < 2`. Dans un tel cas (que l'on pense toujours atteignable avant que la mémoire ne soit épuisée)
la fonction fact() n'est plus rappelée. Comme elle retourne 1 (lorsque n = 1), nous voyons que l'appel de la fonction lorsque n = 2 va 
faire l'opération 2 * 1 et retourner le résultat (à la fonction appelante, qui peut être fact() elle même :)).

Dans le jeu vidéo, je n'ai pas trouvé beaucoup de cas d'utilisation de la récursivité à part en intelligence artificielle pour les parcours des arbres (et structure de données spécifique).
Toutefois, il y a un cas pour les jeux ayant un déplacement de personnage sur une grille (comme Advance Wars). Prenons un personnage et disons qu'il ne peux que se déplacer de trois cases.
Lorsque nous cliquons sur le personnage, on aimerait colorier les trois cases où il peux se déplacer, afin d'indiquer au joueur sa possible destination.
La méthode naïve, serait de parcourir toutes les cases du tableau et de calculer la différence (distance) entre la case parcourue et la case du joueur.
Oui, ça fonctionne, mais c'est un parcours bien trop grand pour la ridicule chose que nous voulons faire. Par contre, une fonction récursive est efficace dans ce cas.
La fonction récursive devra colorier la case présente et colorier les cases adjacentes. À chaque appel, on réduit la distance restante de un.

## Exercices

Ceci est votre exercice. J'ai placé un [code de base ici](https://github.com/Paris-Coders/jeux/tree/master/exo/recursivity), dans lequel le clic sur la fenêtre appelle la fonction fillGrid du fichier filler.py.
Celle-ci est notre fonction récursive. Trouvez le code pour faire en sorte que cela colorie que les cases autour de celle où vous avez cliqué, indiquant les cases à une distance adéquate, de votre clic.

Un second exercice serait de s'intéresser [aux fractales](https://fr.wikipedia.org/wiki/Fractales). La plus simple à mettre en place est : la [courbe de von Koch](https://fr.wikipedia.org/wiki/Flocon_de_von_Koch).
