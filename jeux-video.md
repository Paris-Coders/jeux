# Introduction

**Un jeu vidéo**

Lors de la rencontre du 8 novembre 2014, nous avons commencé à nous intéresser aux projets. Moi, je propose un projet de jeu vidéo.
Commençons d'abord à expliquer pourquoi programmer un jeu vidéo, ce n'est pas aussi simple que cela n'y parait et peut être même, nous pouvons dire que c'est l'un des genres les plus ardus de la programmation.
Un jeu vidéo est composé :

  *  d'un programme ;
  *  de graphismes ;
  *  de modèles 3D ;
  *  de musiques et autres sons ;
  *  d'un site web (pour la communauté) ;
  *  ...

Mais vous allez me dire, "oui, ok, beaucoup de métiers se retrouvent ensemble dans la conception d'un jeu vidéo, mais la programmation, au final, c'est simple ?".

Alors, prenons le cas de World of Warcraft, un jeu massivement multijoueur qui est assez connu, vu qu'il existe depuis dix ans. Dans la partie programmation, nous retrouverons :

 *  le rendu (afficher des éléments à l'écran) ;
 *  la logique de jeu (faire en sorte que si le joueur passe dans une zone, tel ou tel événement se déclenche, ou encore, un système de points, ou encore un système de niveaux avec des classes...) ;
 *  le son (généralement, un peu mis à l'écart, mais il faut au minimum, un moyen pour lire des fichiers sons, les jouer et pouvoir faire des fondus sonores et même, de la spatialisation du son) ;
 *  l'intelligence artificielle (gérer le comportement des ennemies, des alliés...) ;
 *  le réseau (problème de latence, de sécurité, de synchronisation de données entre les joueurs...)
 *  ...

Vous voyez, beaucoup de problématiques se retrouvent regroupées dans un seul et unique programme. Pire, pour chacun des domaines que j'ai énoncé ci-dessus, vous aurez plusieurs problématiques et quelques fois, des sous domaines, car même en décomposant, cela reste un grand travail. Pour un jeu comme World of Warcraft, on peut compter une centaine de gens bossant dessus, pendant au minimum trois ans. Un tel jeu, c'est un travail réellement énorme.

De plus, ce n'est pas le plus facile. En effet, un jeu doit être en "temps réel". Cela veut dire que lorsque l'utilisateur appuie sur un bouton, le programme doit réagir sans tarder. De plus, un jeu affiche généralement 60 images par seconde. Cela veut dire que l'affichage (et son calcul par l'ordinateur) doit se faire en 16ms seulement. Ce sont des difficultés supplémentaires qu'il ne faut pas oublier. Pour d'autres types d'applications, ont peut se permettre de faire attendre l'utilisateur, mais ici, c'est limite impardonnable (cela va considérablement réduire son plaisir de jeu).

C'est pour cela, que les débutants, les amateurs et les studios indépendants ne peuvent pas viser des projets trop immenses. 
Faire un jeu vidéo, c'est un vrai métier (enfin, c'est même une série de métier du coup). Même si la finalité n'est que l'amusement des joueurs, il en reste que c'est un métier.

Alors, bien que cela soit "compliqué", nous, nous allons tout de même faire un jeu vidéo. Certes, cela ne sera pas World of 
Warcraft, ni Call of Duty, ni Assassin's Creed ou autre. Nous allons commencer, un peu comme tout le monde, avec un Mario, 
ou un Tetris. Cela peut paraître ennuyant, ou minimaliste, mais c'est un début nécessaire. Tout comme vous commencez par un 
"Hello World" dans un nouveau langage, nous commençons par un petit projet pour être sur d'y arriver.

Je dis tout cela, car, sur les forums, il y a un grand nombre de projets de débutants n'ayant jamais programmé, qui ne voit 
jamais le jour, car ils voient bien plus grand que leur réelle capacité. Après notre premier projet, on pourra voir 
un peu plus grand, lorsque l'on aura écarté les premières problématiques et que l'on se sentira à l'aise, mais il nous faut, 
simplement, des problèmes à notre niveau, pour progresser.

** Quel projet ? ** 

Donc, durant la séance, nous avons décidé à travers des propositions et un vote, d'attaquer un genre de jeu vidéo, que nous allons réaliser au fil des prochaines séances.

Voici les types de jeux proposés :

  * Jeux de plateformes (Mario) ;
  * Shoot em up (Gradius, 1944, Flying Shark...) ;
  * Tetris
  * Pac man
  * Angry Birds
  * Candy Crush
  * RPG (Final Fantasy)
  * Zelda

J'ai immédiatement écarté certains jeux. Angry Birds demande d'avoir un moteur physique, ce qui, en soit apporte une petite difficulté supplémentaire qui est la nécessité d'installer une nouvelle bibliothèque (ou module en Python) pour gérer la 2D et de l'utiliser. Le RPG est aussi écarté, notamment car pour qu'il devienne intéressant à jouer, il faut énormément de graphismes. Du coté de la programmation, ce n'est pas un réel soucis et, en soit, il n'y a pas grande difficulté. Juste, on peut faire un RPG tout en texte très facilement, mais c'est moins intéressant à jouer, alors que tout le code nécessaire pour que cela tourne, sera là.

Les votants ont décidé de partir sur un Shoot em up. Rapide rappel du genre : c'est souvent un jeu où le jouer dirige un vaisseau, qui tire sur la horde d'aliens ou autre monstres arrivent (souvent du coté droit, ou haut de l'écran). C'est un peu comme un Space Invaders, mais en plus dynamique.


** Pygame **

Nous sommes en Python et pour réaliser notre jeu, nous allons utiliser Pygame. Voici un petit cours d'histoire dans le monde 
de la création de jeux vidéo amateur.

Commençons par la SDL. Son créateur Sam Lantiga, a commencé à travailler dessus en 1998, pour créer des portages (commerciaux) 
de jeux Windows, sous Linux. Ensuite, il a été recruté chez Blizzard et actuellement il travaille chez Valve. 
Donc, vous pouvez en être sur, le gars s'y connaît en développement de jeux vidéo. La SDL, c'est une bibliothèque open source, 
gratuite, portable (qui fonctionne entre autre sur Windows, Linux et Mac OS) regroupant tout le nécessaire pour faire un jeu en 
2D (et assez pour faire un jeu en 3D). Actuellement, on peut compter plus de 700 jeux utilisant la SDL. 
Elle est fiable, vous pouvez en être sur.

Toutefois, la SDL (en version 1.2) commençait à se faire vieille, très vieille. Pour afficher des éléments à l'écran (tel des images) elle utilise uniquement le CPU. Le CPU n'étant pas fait pour cela, il devenait dur d'avoir un jeu fluide et rapide tout en ayant une résolution plus grande que 800x600 pixels. En 2010, je peux vous dire, une telle limitation dans le rendu, c'est une aberration. De plus, la SDL 1.2, avait quelques soucis et défauts de jeunesse. Alors, finalement, après une longue attente, la communauté guidée par le créateur, ont réalisé une nouvelle version : la SDL 2. Celle-ci utilise le GPU, résoud des soucis, corrige des erreurs de conception. Enfin, elle revient simplement sur le devant de la scène et elle a de quoi faire plaisir à tout le monde. Sachant que Sam travaille chez Valve, elle est utilisée très fréquemment dans Steam et sur certains jeux vendus sur la plateforme de Valve.

Bref, revenons à Pyhon et Pygame. Pygame, c'est une surcouche de la SDL 1.2. Cela veut dire, que bien que la SDL soit programmé en C, la surcouche Pygame vous permet de l'utiliser dans vos programmes Python et ainsi, avoir tous les avantages des deux (la bibliothèque et le langage). Mais, en réalité, ce n'est pas qu'une surcouche, car Pygame ajoute aussi quelques fonctionnalités très pratiques pour réaliser un jeu vidéo.

Vous allez me dire : pourquoi on utilise un truc qui utilise la SDL 1.2 alors qu'elle est obsolète. Vous avez plus que raison. Mais actuellement, je pense que malgré les lacunes de la SDL 1.2, nous n'allons pas atteindre ses limites. De plus, la SDL 2, est légèrement plus compliquée à utiliser. Pour ceux qui sont intéressés, il existe une surcouche pour Python de la SDL 2 -> pySDL2. 

Pygame est simple, pratique et malgré l'utilisation de la SDL 1.2, elle nous suffira amplement, ne vous inquiétez pas.

# Pygame

Quelle introduction ! Maintenant, partons sur ce que nous faisons de mieux : du code.

Alors, certains n'ont pu assisté à mes séances précédentes. En réalité, ce n'est pas un soucis. Déjà car vous pouvez lire le compte rendu sur le Google Group mais, aussi, faire un jeu n'est pas si compliqué que cela et vous allez le découvrir dès maintenant.

** Liens utiles **

Commençons, par les liens utiles.

Le site officiel de Pygame : http://www.pygame.org/news.html
La documentation officielle : http://www.pygame.org/docs/ (la référence est en bas)

Pour installer sous Windows : il suffit de récupérer le .msi sur la page de téléchargements : http://www.pygame.org/download.shtml
Sous Linux (Ubuntu, Debian, Mint) : sudo apt-get install python-pygame
Sous Mac : c'est similaire à Windows, mais avec le fichier .dmg disponible sur la page de téléchargements : http://www.pygame.org/download.shtml

La documentation officielle sera notre principale source d'information et de compréhension du fonctionnement de la bibliothèque. On peut avoir un tutoriel sous le code, pour comprendre comment l'utiliser, mais généralement, il faut toujours se référer à la documentation officielle, même pendant la lecture d'un tutoriel.

** Commençons ! **

Bon, Pygame, c'est un module. Pour pouvoir l'utiliser, il suffit de l'importer au tout début du programme :

    import pygame

Vous pouvez tester ainsi. Le programme ne fera rien de concret, mais, vous pourrez ainsi vérifier que Pygame est correctement installé sur votre machine. Si ce n'est pas le cas, vous aurez une erreur.

Pour démarrer pygame, il faut appeler la fonction init() :

    pygame.init()

Cela démarre Pygame, dans le sens où il va faire quelques préparations, initialisation en internet pour qu'il puisse fonctionnement correctement. Si vous l'oubliez, il y a de grandes chance que l'utilisation des autres fonctionnalités de Pygame vont planter.

Dans un jeu, nous effectuons le rendu dans une fenêtre. Pour créer cette fenêtre, on utilise la fonction set_mode() :

    screen = pygame.display.set_mode((320,240))

Ici, nous créons une fenêtre de 320,240 pixels. La référence de la fenêtre est gardée dans une nouvelle variable, ici appelée screen.
Pour Pygame, une fenêtre c'est une "surface". Une surface, c'est entre autre un tableau de pixels (un tableau contenant la valeur de couleur de chaque pixel). Lorsque vous chargez une image, Pygame vous fournit une surface, contenant les informations de l'image. L'écran est aussi une surface, mais, vers laquelle on copie d'autres images. Cette opération de copie s'appelle un "blit" (par héritage des vieilles consoles, micro ordinateur).

La SDL 1.2 (et donc Pygame), ne permette d'ouvrir qu'une seule et unique fenêtre par programme. Cette limitation est d'ailleurs retirée avec la SDL 2.

Si nous exécutons le programme à partir de là, on aura bien une fenêtre qui s'ouvre. Par contre, elle se ferme immédiatement. En effet, actuellement, le programme s'arrête juste après l'ouverture de la fenêtre.

On peut rajouter une boucle infinie, pour bloquer le programme :

    while 1:

(Équivalent à while True). Bon, c'est bien beau, mais en réalité, le système (Windows, Mac OS, Linux) ne va pas vraiment apprécier ce que nous faisons. En effet, le système communique souvent avec la fenêtre (et le programme qui gère la fenêtre), pour lui ordonner de : se redimensionner, réafficher telle ou telle partie et plein d'autres choses. D'ailleurs, lorsque vous déplacez la souris dans une fenêtre, le système va envoyer une série de messages décrivant se déplacement. Par contre, lorsque le programme est bloqué (par un while 1, par exemple), alors les messages du système ne sont pas traités. La fenêtre ne donnant plus de réponse au système, celle-ci va être déclarée en : "Ne reponds plus". Message classique d'un programme qui bogue. C'est simplement, car le programme ne communique plus correctement avec le système.

Avec ce code, c'est ce que nous faisons. Ce n'est donc pas une bonne chose. Voyons comment traiter les signaux du système. Dans Pygame, on appelle cela des événements. Ceux-ci sont gérés par Pygame et chaque fois que Pygame reçoit un événement, il le met dans une pile. Nous pouvons récupérer cette pile et voir, si un événement nous intéresse afin d'exécuter le code que nous souhaitons pour réagir à l'événement. Ainsi, si un utilisateur appuie sur une touche, le programme va regarder dans la pile des événements, voir si un événement d'appui de touche a été reçu et si oui, il va déplacer le personnage sur l'écran.
Pour commencer simplement, nous allons gérer la fermeture par la fenêtre avec la crois (en haut à droite, souvent). En effet, le clic sur cette croix, c'est aussi un événement qui est envoyé par le système. Voici comment le gérer :

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

Qu'avons nous ici ? Pour récupérer notre pile d'événements (sous forme d'une liste), on utilise pygame.event.get(). Du coup, nous devons parcourir un par un les événements, pour voir s'il y en a un qui nous intéresse. Chose que nous faisons avec le for. Et pour chaque événement, nous vérifions son type. S'il est du type qui nous intéresse (celui du clic sur la croix) alors nous quittons le programme.

Si chez vous sys n'est pas reconnu, alors rajoutez import sys au début du programme.

Bon, tout ça, c'est beau. Une fenêtre que l'on peut fermer. Il serait temps d'afficher une image, non ?

En Pygame, c'est simple. Il suffit de charger un fichier sur le disque ainsi :

    ball = pygame.image.load("./data/ball.gif")

Puis de l'afficher. Comme je le disais juste avant, l'image est maintenant en mémoire, contenue dans une surface. Elle doit être copiée dans notre surface écran. On peut le faire ainsi :

    screen.blit(ball, ball.get_rect())

Ici, on demande de blitter la ball, sur l'écran (screen). Pour la position (deuxième argument), on utilise le rectangle retourné par ball. Ce rectangle contiendra :
[0, 0, largeur_de_l_image, hauteur_de_l_image]

Donc, notre balle apparaitra en 0,0 (en haut à gauche de l'écran). Si on exécute ce code, rien ne s'affiche. En effet, la surface écran n'est pas envoyé à l'écran. Plus précisément, screen, c'est une surface en mémoire. Il faut donc demander précisément à Pygame de copier la surface sur l'écran :

    pygame.display.flip()

Ici, nous avons encore un héritage du monde de l'informatique. Flip(). Cela veut dire : retourner. En effet, les premiers ordinateur et console utilisait des écrans lents et surtout, l'affichage devait être synchronisée avec le balayage du tube cathodique. Si vous ne le faisiez pas, vous auriez des déchirures sur votre image et un effet un peu baveux. Mais, le fait d'envoyer une image à l'écran était lent. Donc, la technique était de préparée l'image à afficher, en mémoire (dans un tampon), puis, lorsque celle-ci est totalement prête, de demander à un composant matériel dédiée, de l'afficher. Ainsi, on peut l'afficher en attendant la synchronisation et surtout, sans devoir attendre que le CPU pose les éléments au fur et à mesure. Cette technique est appelée : Double Buffering. Du coup, c'est pour ça que l'on a toujours cette opération de : "affiche à l'écran ce que j'ai demandé".

Bon, c'est pas mal. On a enfin une image à l'écran. Par contre, un jeu, cela doit réagir à l'utilisateur (et pas juste lorsque l'on ferme la fenêtre). Donc, nous allons revenir sur nos événements et chercher s'il y en a d'autres qui nous intéresse. Et oui, il y en a d'autres, de type KEYDOWN (appui sur une touche) et on peut même vérifier la touche appuyée :

    if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ballrect.x+=1

Ici, on doit créer une nouvelle variable "ballrect" pour garder la position de la balle que l'on déplace (que l'on modifie).
Il faut savoir que la fonction blit() prend en argument un rectangle (cette fois, qui sera ballrect et non plus ball.get_rect()) car il est possible d'afficher des parties d'une image et non son intégralité. En effet, le rectangle contient une width (largeur) et une height (hauteur) en plus des x et y, permettant de définir la taille de l'image à copier (ou une taille inférieure, si besoin).

Si vous déplacez la balle, vous verrez un effet crade. La balle précédemment affichée reste et la balle affichée à la nouvelle position, l'est par dessus. C'est normal. Notre écran (ou notre surface écran) agit comme une ardoise magique. Chaque fois que vous voulez afficher/dessiner une nouvelle chose il faut effacer le dessin précédent. C'est aussi comme dans un dessin animé, chaque fois, le dessin précédent est effacé. Pour ce faire :

    screen.fill((0,0, 0))

Littéralement, on remplit notre écran d'une couleur (ici, le noir).

On a fait un bon morceau de chemin. On a une balle qui bouge (dans une direction, mais c'est à vous de le faire pour les autres :)).
Par contre, là, c'est ennuyeux, il faut appuyer plusieurs fois sur la touche, pour la déplacer. Généralement, les jeux ne se joue pas ainsi. Pour déplacer le personnage, on laisse le doigt appuyé. Faisons le dans notre jeu aussi !

Il faut savoir, qu'il y a un événement lorsque l'utilisateur appuie sur une touche. Mais aussi, il y en a un lorsque l'utilisateur relache une touche (KEYUP). On pourrait faire un super truc, avec des booléans, qui devient True, lorsque l'on reçoit le KEYDOWN et False lorsque l'on reçoit le KEYUP. Après, il suffit de faire un test sur le boolean pour savoir s'il est nécessaire de déplacer le personnage. Oui, c'est une solution qui fonctionne. Par contre, le jour où vous devez gérer 25 touches, il vous faudra 25 boolean (ou un tableau) et le code qui va avec. Nous sommes légèrement fainéants et surtout, il y a mieux : Pygame fait tout ça pour nous.
En effet, Pygame propose une méthode pour récupérer le tableau des touches appuyées ou non :

    keysState = pygame.key.get_pressed()
        if keysState[pygame.K_RIGHT]:
            ballrect.x+=1

Simplement, ce tableau, renvoyé par pygame.key.get_pressed() a une taille équivalent au nombre de touche du clavier. Dès qu'une touche est appuyé, Pygame met True à la case correspondante à la touche. Ainsi, vous pouvez savoir quand est appuyé ou non, une touche.

** Exercices supplémentaires **

Vous avez une balle qui bouge, mais que dans une direction. Libre à vous de rajouter les autres directions.
Moi, il m'embête de devoir utiliser la souris pour quitter l'application. J'aime bien quitter une application avec la touche échap (K_ESCAPE). Pouvez-vous faire en sorte que votre programme le fasse aussi ?
La balle peut sortir de l'écran. Pouvez-vous empêcher ce comportement ? Vous pouvez récupérer la taille de l'écran avec les fonctions proposées ici : http://www.pygame.org/docs/ref/surface.html
Si vous voulez aller vraiment plus loin, essayer d'intégrer d'autre image, de vaisseau par exemple, mais qui bouge toutes seules. Ou encore, un fond étoilé pour donner une impression de mouvement dans l'espace.

N'hésitez pas à nous présenter, ou à me présenter vos avancées et à me poser des questions.
