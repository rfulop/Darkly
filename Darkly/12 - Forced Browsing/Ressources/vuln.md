# Forced browsing

#### Page: _/.hidden/_


## Description de la vulnérabilité :
On remarque de nombreux dossiers dans le dossier `.hidden` a la racine de l'application web. Chacun d'entre eux contient un fichier `README` dans lequel se trouvent d'étranges phrases.
On récupère le flag on testant l'ensemble des `README`.


## Scénario d'attaque :
Un script permet de tester l'ensemble des `README` présents dans les dossiers.


## Correctifs :
- Il est difficile de comprendre l'utilité de ce type de méthode afin de dissimuler des informations confidentielles.
