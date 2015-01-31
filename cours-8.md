# Introduction

Après la parenthèse qu'à été le [septième cours](https://github.com/Paris-Coders/jeux/blob/master/cours-7.md), sur Git, nous revenons à la programmation et à la conception d'un jeu vidéo.
Voici le plan de ce nouveau cours :

 * les machines à états ;
 * la 2D, avec trois dimensions ? ;
 * un nouveau jeu ?
 
# Les machines à états

Les machines à états finaux (aussi appelé automate fini) sont des machines abstraites utilisées en mathématique et en informatique. Elles permettent de modéliser des processus logiques (aussi des protocoles de communication, ou de permettre l'étude de langages formels, mais cela nous intéresse moins dans le cas d'un jeu vidéo).
Une machine à états n'est qu'un ensemble d'états (que l'on dessinera par des bulles) et des transitions permettant de passer d'un état à un autre. La machine est obligée d'être dans un seul et unique état à la fois. Pour passer d'un état à un autre, il faut un événement (le changement d'un paramètre).

![Exemple machine à états](http://alexandre-laurent.developpez.com/ressources/machine_etats_exemple.png)

Ce simple exemple reproduit le comportement d'une lampe connectée à un interrupteur. Disons que par défaut notre lampe est éteinte. Elle ne passera dans l'état allumé, que dans le cas où un utilisateur appuie sur le bouton ON. Elle est maintenant allumée. De même, elle ne reviendra dans son état éteinte, que si l'utilisateur appuie sur le bouton OFF.
Une machine à états peut devenir gigantesque, suivant le comportement que l'on souhaite décrire. Pour une intelligence artificielle (qui soit convaincante pour son public) la machine à états sera énorme et plus elle le sera, plus elle la machine sera intelligente. Toutefois, comme le second nom (qui est tout aussi correct) l'indique, ce n'est qu'un automate fini. Il n'évoluera pas, il ne fera rien de plus que ce qu'à prévu son programmeur. Donc au final, ce n'est pas une "vraie intelligence artificielle". Toutefois l'illusion est effective à partir du moment où le public, n'est pas capable de deviner cette machine à états.

Revenons aux jeux. Générallement, les intelligences artificielles des jeux ne sont pas trop compliquée. Un cas classique est assez basique sera le suivant :

![Intelligence artificielle base](http://alexandre-laurent.developpez.com/ressources/machine_etats_IA.png)

Bon, cette intelligence artificielle a quelques lacunes, mais pour certains jeux, nous pouvons la considérer comme suffisante. Par contre, ne vous étonnez pas trop que le joueur arrive à la battre facilement, car dès qu'elle n'aura plus assez de vie, elle va fuire. Une seconde lacune, c'est la notion du champ de vision. En effet, l'intelligence artificielle ne va attaquer que si elle voit le joueur. Certes, c'est logique, mais après, tout dépend de comment le champs de vision est intégré. En effet, est ce que l'on va prendre en compte les obstacles ? Qu'elle est la distance de vision de l'ennemi ? Ce sont des paramètrs qui détermineront la difficulté de votre jeux, mais aussi l'amusement que procure votre jeux.

Les jeux vidéo utilisent les machines à états dans un second cas : les menus. En effet, généralement, votre jeu fonctionne et le joueur joue. Mais depuis très longtemps, les créateurs de jeux vidéo ont intégré la pause. Celle-ci gèle plus où moins le jeu (sans le stopper) et dès que l'on rappuie sur la touche, le jeu continue. Déjà, deux états se dessinent : un état `EN JEU` et un autre `PAUSE`. Mais on peut aller plus loin et mettre un état pour le menu, un état pour le game over et ainsi de suite. Grâce au menu, vous pouvez lancer une partie (et donc aller à l'état `EN JEU`) puis, du jeu, vous pouvez soit aller en pause, grâce à un bouton dédié, soit aller à l'état `GAME OVER` lorsque le joueur perd. De la pause, vous pouvez quitter le jeu et revenir au menu aussi et du game over, vous retournez obligatoirement au menu.
Le jeu aura ne sera que dans un seul de ces états à la fois et suivant les actions du joueur, on passe d'un état à l'autre, affichant des éléments différents suivants l'état.

Du côté de la programmation, la machine à état n'est pas très compliquée. La méthode naîve étant d'avoir une variable `etat` et un `switch/case` (juste des `if/else` en Python) comme suit :
```python
	if etat == "JEU":
		afficher_jeu()
	elif etat == "MENU":
		afficher_menu()
```

# La 2D, avec trois dimensions

En réalité, les jeux 2D utilisent une troisième dimension. Certes, elle n'est pas visible, le jeu est bien en 2D, mais les composants du jeu auront bien trois coordonnées : x, y et z.
Cette troisième coordonnées permet de déterminer l'ordre d'affichage des sprites. En effet, si vous affichez deux sprites ayant la même taille à la même position, le sprite visible sera le second sprite dessiné (comme pour la peinture). Ainsi, il est nécessaire dessiner le fond (l'arrière plan) en premier, puis les éléments du jeu (les personnages) par la suite. Si vous ne le faites pas dans cet ordre, vous n'allez voir que l'arrière plan.
Ça, c'était le cas simple avec juste un arrière plan. Mais pour donner plus de réalisme et de beauté à votre jeu, vous voulez plusieurs plans. Un arrière plan avec des montagnes, certes, mais aussi un plan pour les éléments du jeu et encore un plan, le premier plan, avec des arbres, qui viendront cacher ponctuellement les joueurs. Vous pouvez même faire plus. Bien entendu, vous n'allez pas gérer tout cela à la main, c'est fastidieux et source d'erreur. La bonne méthode est donc d'ajouter cette coordonnées z (que l'on peut aussi appelé `calque` ou `couche`) et de faire en sorte de demander à l'ordinateur de dessiner les éléments dans l'ordre déterminé par la coordonnée z.
Jusqu'à présent, nous n'avions qu'une boucle de dessin de ce genre :

```python
	for element in liste_elements:
		afficher(element)
```

Cela ne suffit plus. On pourrait mettre en place une solution avec deux boucles :

```python
	for profondeur in liste_des_couches:
		for element in liste_elements:
			if profondeur == element.z:
				afficher(element)
```

Mais cette solution à deux limitations :
* elle nécessite d'avoir la liste des couches (savoir combien de coordonnées z ont été utilisée). Alors oui, on peut demander à l'ordinateur de trouver cela pour nous, en parcourant ... nos objets (oui, encore une fois) ;
* il y a deux boucles for, imbriquées. Cela veut dire, que l'on parcourt tous nos éléments autant de fois qu'il y a de couche. Si j'ai mille éléments et huit couches composés d'un unique élément alors, je vais faire énormément de calculs (8000) pour afficher que huit éléments. C'est inneficace.

Il existe une solution qui, au premier abord, parait comme moins efficace : on va trier la liste des éléments selon leur coordonnée z. Ainsi, tous les éléments ayant la coordonnées z 0 seront au début de notre tableau et donc, affichés en premier. Puis viendront les éléments de la couche 1 et ainsi de suite.
Notre code sera donc :

```python
	tri(liste_elements)
	for element in liste_elements:
		afficher(element)
```

Voilà, c'est fini. Le soucis est réglé. Sachez qu'en informatique, le tri d'un tableau est un problème archi classique et qu'il a été résolu de très nombreuses fois, avec différents algorithmes efficaces. D'ailleurs, Python en propose un, optimisé, prêt à l'utilisation. En Python, la fonction toute prête pour effectuer le tri est `sort()` (ou `sorted()`). Comme toujours, référez vous à la [documentaiton officielle](https://docs.python.org/2/howto/sorting.html) pour plus d'informations.
Vous pouvez me dire : on tri le tableau à chaque affichage, cela va prendre un temps fou. D'une part, le tri est optimisé et aura beaucoup de chance de prendre moins de temps que la situation précédente, mais nous avons un second avantage : les algorithmes de tri (du moins, les grands classiques), pour un tableau trié, ne "perdent pas de temps" (juste un parcours du tableau sans plus).
Donc oui, le tri est la vraie solution pour ce cas là. En informatique pour certains problèmes, il arrive que l'on gagne beaucoup de temps de traitement, en commençant par trier les données, puis en faisant les vrais calculs/opérations que l'on souhaitait faire sur les données.


