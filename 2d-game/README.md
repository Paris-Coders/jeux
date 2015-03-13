# Introduction

Le but de ce dossier est d'accueillir le code source pour le jeu 2D, d'action vu de dessus (The Legend of Zelda...).
Seul un code à trou est disponible. À vous de le compléter.
Pour le moment, le code ne fait qu'afficher une fenêtre

# Comment démarrer

Il suffit de `forker` le projet et de travailler sur la copie sous votre compte GitHub.
Si vous ne voulez pas travailler avec GitHub (ce qui serait dommage), vous pouvez simplement cloner le git.

# Les étapes

Le projet peut se résumérer en deux étapes :
* chargement de la carte (fichier ./data/world.map)
* affichage de la carte

# La carte

Le tileset de la carte contient beaucoup de zone transparante. Afin d'avoir un résultat cohérent, il faut donner un fond, sous les tuiles transparentes.
Pour cela, le rendu est fait en deux couches (comme si on afficher deux cartes l'une sur l'autre).

Le fichier de la carte peux se lire ligne par ligne, puis, chaque ligne peut être décomposée par nombre. Il est nécessaire de chercher dans la documentation, comment lire un fichier et en extraire des informations. Les deux couches se suivent. Il est possible de les sauvegarder dans deux tableaux à deux dimensions.

Chaque nombre identifie une tuile spécifique. La première tuile est numérotée 1 et la numérotation se fait de gauche à droite et de haut en bas. L'identifiant '0' correspond à une zone où l'on ne fait rien.
Avec un éditeur d'image (GIMP) on remarque rapidement que les tuiles ont une taille de 32x32. On peut même s'aider de la grille pour mieux repérer les tuiles.

# Bonus 

On peut toujours faire en sorte que certaines tuiles de la carte soient animées.
De plus, il serait plus malins, pour faciliter l'édition, d'utiliser un logiciel comme Tiled (un éditeur générique).
