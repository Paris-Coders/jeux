# Introduction

Ce cours vous expliquera comment utiliser git, GitHub et le code source à trou du jeu de shoot em up que j'ai préparé afin que vous créez votre jeu plus facilement.

# Logiciels de gestion de versions

Les logiciels de gestion de versions permettent de sauvegarder des fichiers ainsi que otutes les versions que ses ont pu avoir durant la vie du projet. Cela veut dire, qu'il est possible de revenir à une ancienne version du fichier, si vous vous rendez compte que vos modifications sont mauvaises.
Ainsi, si dans votre projet, vous modifiez plusieurs fichiers pour rajouter une fonctionnalité, mais que celle-ci s'avère inutile, ou non fonctionnelle, le logiciel de gestion de versions, sera capable de revenir à la version avant la série de modification. Mais, ce n'est pas tout. Ces logiciels facilitent le travail en collaboration. Lorsque deux personnes travaillent sur un même projet et que chacune d'elle aura fini sa version, elle vont envoyer leurs modifications sur le serveur. Le logiciel de gestion de versions va fusionner les modifications locales avec la version sur le serveur. S'il y a des conflits (des morceaux ne pouvant être fusionnés en gardant les changements des deux personnes), alors une validation manuelle sera nécessaire.
Et encore plus fort, vous pouvez créer des branches sur votre projet. Lorsque vous travaillez votre projet, mais vous ne voulez pas le casser en testant une nouvelle fonctionnalité (ou autre), vous pouvez créer une branche et les modifications suivantes seront appliquées à la branche. Si vous devez corriger le code "principal", vous pouvez toujours revenir à la branche principale, faire votre correction et revenir à la branche de votre fonctionnalité et continuer votre travail sur la nouvelle fonctionnalité. Les deux branches seront indépendantes. Lorsque vous finissez votre travail sur la nouvelle fonctionnalité, vous pouvez la fusionner avec la branche principale.

Au final, un logiciel de gestion de versions est utile, que ce soit, pour un projet sur lequel vous êtes seul, ou en entreprise. Les principales raisons sont :

* la sauvegarde (souvent sur un serveur centralisé) ;
* la gestion des versions (possibilité de revenir en arrière) ;
* les branches (pour avoir une version distribuable, tout en travaillant sur la prochaine version) ;
* le travail collaboratif (gestion des conflits) ;
* ....

Historiquement, on utilisait `CVS`, puis `SVN`. Dernière, le plus populaire logiciel dans la communauté, c'est `git`.

## Fonctionnement

L'idée d'un logiciel de gestion de versions c'est d'avoir un serveur qui stocke le code source (et ses versions). Lorsqu'un développeur souhaite travailler il fait une copie en local de la dernière version connue par le serveur et travaille dans son coin. Une fois qu'il a finit, il renvoie sa nouvelle version au serveur.
Chaque développeur fait ainsi. On appelle cette opération un "push" (pousser ses modifications pour qu'elles soient disponibles pour tous). Pour les autres développeurs, s'ils veulent connaître les dernières modifications, elles vont pouvoir faire un "pull" (tirer la dernière version en local).

## Git

Git est un projet initié par Linus Torvalds (créateur du noyau Linux) pour répondre au besoin du projet du noyau Linux. En effet, il trouvait que les autres logiciels ne répondaient pas à ses exigences et aux contraintes du projet du noyau Linux.
Depuis, Git est devenu très populaire dans la communauté Open Source et même en entreprise. Il est assez simple (pour quiconque ayant compris le principe des logiciels de gestion de versions) et est très performant.

### Utilisation

Nous allons partir d'un projet déjà existant.
Pour copier un projet existant, il faut le copier (ou plus précisément, le cloner) à partir du serveur :

   git clone git@github.com:Paris-Coders/jeux.git

Ensuite, pour chaque étape de votre projet, vous pouvez créer un commit (chaque commit, doit être une modification du code, dans le sens, un ajout de fonctionnalité, ou une étape du projet).
Pour ajouter des fichiers à être commiter, il faut utiliser `git add`, sinon il sera ignoré.

   git add monNouveauFichier

(Vous pouvez aussi supprimer des fichiers avec `git rm`).   
Ensuite, vous pouvez faire un commit :

   git commit
   
Le logiciel vous demandera un message, un message qui sert à expliquer au reste de l'équipe ce que vous avez fait lors de ce commit.
   
Vous pouvez faire autant de commit que vous le souhaitez, sans jamais les envoyer au serveur. Ce n'est pas un soucis en soit, mais le mieux est d'envoyer une copie du projet assez souvent (à la fin d'une journée) pour le sauvegarder. Pour cela, vous allez faire un push :

   git push
   
Si vous travaillez avec une autre personne, vous voulez récupérer ses modifications avec un `pull` :

   git pull
   
Voilà les bases de Git.   

### TortoiseGit

Sous Windows, au lieu d'utiliser une ligne de commande, vous pouvez utiliser [TortoiseGit](https://code.google.com/p/tortoisegit/), qui s'intègre au gestionnaire de fichier afin d'éviter toutes les commandes.

### Aide

Beaucoup de tutoriels et d'informations sont maintenant disponible sur Git :
* http://git-scm.com/book/fr/v1
* http://doc.ubuntu-fr.org/git
* ...

## GitHub

GitHub est une forge logicielle (comme SourceForge, GoogleCode...). Vous pouvez y stocker votre projet gratuitement à condition qu'il soit sous licence OpenSource. GitHub est devenu populaire, car en plus d'être une simple forge, le site permet d'afficher ses fichiers, de commenter les commits, de faire des forks des autres projets, de faire des pull requests et ainsi de suite.
Il propose tous les outils nécessaires pour faire un projet en collaboration avec d'autres développeurs même si vous ne les connaissez pas nécessairement.

### Forker un projet

Lorsque vous voyez un projet qui vous intéresse (et dans lequel vous voulez contribuer), vous avez deux choix :
* vous intégrer à l'équipe en contactant le créateur du projet ;
* faire un fork.

Cette seconde option, accessible avec le bouton en haut à droit du site, permet de faire une copie complète du projet sous votre compte. Ainsi, vous pouvez apporter vos améliorations au projet qui vous plait, sans pour autant impacter le projet de base. Ces amélioriations restent dans votre projet et ne sont pas accessibles au projet de base (et donc ne gêne pas le créateur du projet de base). Si au final, vous avez fini vos améliorations et vous souhaitez les proposer au créateur du projet original, vous le pouvez en faisant un pull requests. Il pourra ainsi revoir/valider votre travail et l'intégrer dans son projet. Ainsi, il vous ai facile de participer et améliorer un projet, sans pour autant gêner ou vous intégrez dans le projet principal.

### Documentation

Tout ce que propose le site est documenté : https://help.github.com/

# Projet de shoot em up

Je vous propose un code source à trou, pour le projet de shoot em up. Vous pouvez le forker sur GitHub ici : https://github.com/Paris-Coders/jeux/tree/master/shmup ou le cloner :

   git clone git@github.com:Paris-Coders/jeux.git

Le code est complètement documenté. Il n'introduit absolument aucune nouveauté par rapport aux cours que j'ai donné. Je pense qu'il faudra environ 10h de travail pour faire le jeu (en lisant les cours).
Pour faire le projet, il suffit de lire les commentaires et de remplacer les lignes avec `[TODO]` par le code approprié.
