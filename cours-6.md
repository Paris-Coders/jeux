# Introduction

Ce cours peut être vu comme la dernière étape sur le shoot'em'up. En effet, après l'avoir lu et l'avoir mis en pratique, vous aurez assez de connaissances pour faire un jeu et un jeu complet, amusant à jouer. Plus précisément, je vais vous donner les dernières briques nécessaires pour finaliser le jeu. Ensuite, vous aurez tous les outils nécessaires pour faire le jeu et ce ne sera plus qu'une question de les assembler, de les manipuler pour obtenir ce que vous souhaitez.

Cette fois encore, je vous fournit le pack de ressources que j'ai utilisé pour le cours. Il incorpore une nouvelle image et un son. Vous pouvez le télécharger ici : https://1fichier.com/?f9s0bbsmsj et là : http://alexandre-laurent.developpez.com/ressources/shoot/DataPack.zip.

Donc, dans ce cours, nous allons voir :
* les animations ;
* les fonds (backgrounds) ;
* les sons ;
* le texte.


# Les animations

Actuellement, dans notre jeu, les projectiles touchent bien l'ennemi, mais cela ne suffit pas à donner une bonne impression au joueur. En effet, le projectile et l'ennemi disparaissent mais de façon immédiate. Le mieux serait donc d'afficher une explosion, pour bien montrer la raison de la disparition du vaisseau ennemi. Une explosion dure quelque temps. De plus, celle-ci est animée, dans le sens, ce n'est pas juste un sprite que l'on va afficher à une certaine position, mais un sprite qui "évolue".
Pour cela, on va utiliser une nouvelle ressource, qui est aussi un fichier image, mais que l'on appelle spritesheet (feuille de sprites). Voici la notre :
![explosion](http://alexandre-laurent.developpez.com/ressources/shoot/explosion.png)

On voit bien que c'est une image. Celle-ci est composé de 25 "sous images", que l'on appelle sprite. Pour que l'animation soit jolie et réussie, il faut afficher les images, les une après les autre. C'est la même chose qu'un dessin animé, ou encore, [un flipbook](https://www.youtube.com/watch?v=IehWY6JFjWo). Bien entendu, il ne faut pas afficher l'image complète, mais une sous partie de celle-ci. Nous avons de la chance (enfin, c'est normal, le concepteur de la bibliothèque pygame connaît les besoins que nous avons), la fonction [pygame.surface.blit()](http://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit) possède un troisième argument (optionnel) que nous avions ignoré jusqu'à présent. Ce troisième argument, appelé area, permet d'indiquer le rectangle de l'image source, que nous voulons copier. Ainsi, nous pourrons afficher qu'une sous partie de notre spritesheet.
Avant de faire du code pour afficher l'animation et surtout, la jouer, nous devons observer et retirer quelques informations de notre spritesheet. Celle-ci fait 320px sur 320. Elle comporte 25 étapes (ou 25 sprites), réparti sur une grille de 5x5. Cela veut dire que chaque sprite fait 64px sur 64.

La première méthode "naïve" que nous pourrions mettre en place et de dire : nous affichons un sprite différent à chaque image du jeu. Il suffit de faire une nouvelle fonction et chaque fois qu'elle est appelée, on incrémente un compteur (compteur utilisé pour savoir quel sprite on affiche). En théorie, cela fonctionne. Le souci, c'est que nous ne voulons pas nécessairement :
* jouer toutes les animations du jeu à la même vitesse ;
* jouer les animations à la vitesse de mis à jour du jeu.

En effet, ici, nous faisons une mise à jour du jeu toutes les 16 ms (car nous sommes en 60 FPS). Si on affiche un nouveau sprite de l'animation toutes les 16 ms, l'animation (qui fait 25 sprites) ce finira au bout de : 16 * 25 = 400. 400 millisecondes, pour l'explosion. C'est court, vraiment court. Nous, nous aimerions plus, que l'animation dure quelque chose comme 1,5 secondes (c'est une question d'esthétique et de rendu, après, vous êtes libre de faire ce que vous voulez). Donc, cette première méthode ne fonctionne pas très très bien et est très contraignante. Nous aimerions plutôt avoir des animations indépendantes et dont le temps d'affichage puisse être libre.
Cela est plutôt simple. Notre jeu possède une notion du temps : le delta time. Si nous passons le deltatime à la fonction gérant l'affichage de notre animation, nous aurons une notion du temps. Ensuite, grâce à ce temps, nous allons déterminer quel est le sprite à afficher. Par exemple, si nous voulons afficher un sprite tous les 100 millisecondes, le premier sprite s'affiche de 0 à 100 ms, le second de 100 à 200 ms, le troisième de 200 à 300 ms et ainsi de suite. Il suffit donc, de diviser le temps passé, par le temps que nous souhaitons alloué à chaque étape de l'animation. Le code de la fonction est donc :

```python
def explosionUpdate(deltaTime):
	explosionTimeCounter+=deltaTime
	explosionStep = explosionTimeCounter/100
```

`explosionStep` contient donc l'étape (le sprite) à afficher. Le problème, c'est que la fonction [pygame.surface.blit()](http://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit) doit recevoir une zone source à afficher. Ce qui veut dire que nous devons indiquer un rectangle (le point de départ en haut à gauche de la zone que nous voulons copier + la largeur et hauteur du rectangle). La hauteur et la largeur du rectangle, nous la connaissons, car nous savons que chacun des sprites de notre feuille fait 64x64. Par contre, le point en haut à gauche de la zone que nous voulons copier change à chaque étape de l'animation. Actuellement, nous n'avons que le numéro de l'étape pour la calculer. Cherchons comment la retrouver à partir de ce numéro d'étape.

**Le numéro d'étape dans notre cas, va de 0 à 24. Le zéro est en haut à gauche (soit le premier sprite) et le 24 et en bas à droite. Nous allons de gauche à droite et de haut en bas.**

Voyons ce que nous avons en source et ce que nous voulons comme résultat.

Étape   -> position du coin haut gauche
0          -> (0,0)
1          -> (64,0)
2          -> (128,0)
3          -> (192,0)
4          -> (256,0)
5          -> (0,64)
6          -> (64,64)

Et ainsi de suite. Ok, nous savons que la taille des sprites fait 64x64. Du coup, nous pouvons diviser les coordonnées de notre point haut gauche par 64, ce qui donne :

Étape   -> position du coin haut gauche   ->  Indice dans la grille
0          -> (0,0)                                      -> (0,0)
1          -> (64,0)                                    -> (1,0)
2          -> (128,0)                                  -> (2,0)
3          -> (192,0)                                  -> (3,0)
4          -> (256,0)                                  -> (4,0)
5          -> (0,64)                                    -> (0,1)
6          -> (64,64)                                  -> (1,1)

C'est pas mal. Par rapport aux indices, on commence à voir un certain "motif". Par exemple, pour l'indice des Y, nous voyons que cela ressemble étrangement à ce que fait une division.

0 -> 0
1 -> 0
2 -> 0
3 -> 0
4 -> 0
5 -> 1
6 -> 1
...
10 -> 2
11 -> 2
12 -> 2
...

Et, aussi logiquement que vous pouvions le concevoir, cette division est une division par 5, le nombre d'images que nous avons par ligne.
Pour les coordonnées en X, c'est un principe très identique :
0 -> 0
1 -> 1
2 -> 2
3 -> 3
4 -> 4
5 -> 0
6 -> 1
...
10 -> 0
11 -> 1
12 -> 2
...

C'est toujours lié à 5. On voit d'ailleurs que le résultat ne dépasse jamais 5. En informatique, un outil qui permet de restreindre une séquence de cette façon, c'est le modulo (%). En effet, ici, le résultat, c'est toujours le reste de la division par 5. 5, encore une fois, car c'est le nombre d'image que nous avons par ligne.

Voilà ! Nous savons passer du numéro d'étape, à la position sur l'image du sprite à dessiner. Il suffit d'appliquer :

```python
def explosionUpdate(deltaTime):
    # Gestion du temps
    explosionTimeCounter+=deltaTime
    explosionStep = explosionTimeCounter/100
   
    # Transformation du numero d'étape en indice sur la grille
    imageX = explosionStep%5
    imageY = explosionStep/5
   
    # Affichage. On multiplie bien sur par 64 pour avoir la position du point sur l'image
    screen.blit(explosionSprite,explosionPos,[64*imageX,64*imageY,64,64])
```
Voilà, c'était tout et nous avons des animations.
Grâce à la fonction, nous pouvons faire en sorte d'appliquer des animations pour tous les éléments de notre jeu. Il suffit d'enlever les nombre écrit en dur et de les passer en paramètre à la fonction.
Les animations peuvent être utilisées pour les explosions, mais aussi pour de nombreux effets et éléments de notre jeu. Les projectiles, les monstres, le joueur et même pour des éléments animés dans le fond du jeu.


# Les fonds (backgrounds)

Souvent, dans les shoot'em'up, on voit un fond qui défile. En effet, cela donne une bien meilleure impression au joueur et cela rend le jeu plus joli. Plusieurs techniques existent pour les fonds. La première technique serait de faire une image de fond, de la longueur du niveau qui défilerai de droite à gauche. Cela fonctionnerait "correctement". Sauf que l'image risque d'être immense pour les grands niveaux et donc, de prendre beaucoup de place : sur le disque dur, en mémoire vive et du temps pour afficher (même si nous n'en affichons qu'une sous partie).
Pire, pour avoir une impression de profondeur, nous allons faire en sorte que plusieurs niveaux de fonds soient affichées et que ceux-ci bougent à des vitesses différentes (effet parallax, comme dans [Enchanted Land](https://www.youtube.com/watch?v=xoXL9gZBJQ0) (et plein d'autres)). Pour chaque niveau de fonds, il faudrait une image différente. En plus, ces images seraient en grande partie transparente, mais malgré que les pixels soient transparents, ils devront être testés, au moins pour savoir s'ils doivent être affichés ou non ce qui va prendre énormément de temps.
Au lieu de faire une technique aussi lourde, en termes de performances et de mémoire, nous pouvons faire mieux. Si on regarde mieux la vidéo, on peut voir que les éléments du fond se répète énormément.
Au lieu d'avoir une grande image, il suffit d'avoir juste des sprites, par exemple, le sprite d'un arbre, que l'on va copier régulièrement à l'écran et le faire défiler. On fera de même pour les nuages, les maisons et autre. D'une part, cela prendra moins de mémoire, car nous n'aurons que des petits sprites, que nous allons afficher autant de fois que nécessaire. De plus, l'ordinateur ne tentera plus d'afficher des pixels transparents et donc, ce sera un gain de vitesse.

Pour les collisions, encore une fois, plusieurs techniques existent. On pourrait tester par exemple, la couleur du fond du pixel en bout du vaisseau. Ainsi, s'il n'est pas noir, on saurait que le vaisseau est dans le décor. Malheureusement, il faut une couleur "neutre" qui ne soit jamais utilisé dans le fond. Cela est plutôt rare et il faut mieux utiliser une technique fiable à 100 % pour éviter que le joueur ne triche.
Par contre, on peut utiliser une technique de masque. Le masque c'est une texture qui n'est pas afficher, qui est bicolore (chaque pixel et blanc ou noir). Lorsque le vaisseau est sur un des pixels blancs du masque, alors nous savons que c'est une collision. Le masque doit bien sur suivre le fond et donc bouger à la même vitesse.

# Le son

Afin d'accompagner l'explosion, une bonne idée est de rajouter un effet sonore. Encore une fois, pygame rend les choses très simples.
Au début du programme, il faut initialiser le composant sonore de pygame :

```python
pygame.mixer.init()
```
charger le fichier de son :
```python
explosionSound = pygame.mixer.Sound("./data/explosion.wav")
```
puis, il suffit de le jouer :
```python
explosionSound.play()
```

Il n'y a rien d'autre à faire (bien que l'on pourra lire la documentation pour découvrir les options des différentes fonctions).

Pour les musiques, c'est la même chose. Par contre, il est conseillé d'utiliser les formats MP3 et OGG. En effet, un fichier WAV de trois minutes risque de prendre 30 Mo sur le disque dur. Les formats MP3 ou OGG sont donc plus appropriés. Les WAV seront utilisés pour les sons cours, les bruitages.

Le texte

Pour finaliser notre jeu, nous aimerions afficher le score du joueur. Encore une fois, pygame facilite cela. De même que pour le son, il faut initialiser un autre composant :
```python
pygame.font.init()
```
charger le fichier :
```python
textFont = pygame.font.Font(None,16)
```
Ici, on utilise la police par défaut de pygame. On peut remplacer "None" par le chemin du fichier de police. Le second argument est la taille de la police.

Finalement, on affiche :
```python
textSurface = textFont.render("Score " + str(score), 1, (255, 255, 255))
screen.blit(textSurface,[screen.get_width()/2-textSurface.get_width()/2,screen.get_height()-textSurface.get_height(),0,0])
```
Cela se fait en deux étapes, car pygame n'est pas capable d'afficher le texte directement à l'écran. Il crée d'abord une surface (un sprite), dans laquelle le texte sera dessiné. Ensuite, il suffit de copier ce sprite à l'écran. Je vous invite à lire la documentation de render() pour mieux comprendre les paramètres que j'utilise. Pour les paramètres de la fonction blit(), je crée un rectangle avec les coordonnées pour centrer le texte.


# Conclusion

Et voilà ! Nous avons tout pour faire un jeu complet. Nous savons afficher des sprites, faire bouger le joueur, jouer des animations, jouer du son, afficher du texte. Il ne suffit plus qu'à assembler le tout, à rajouter des variables ici et là, pour le score, pour les bonus. En effet, les bonus, ce ne sont que des sprites, que l'on fait bouger et que dès que le joueur en touche un, il gagne, par exemple, un nouveau type de projectile, plus gros.
Avec ces briques de base, vous pouvez tout faire maintenant. 
