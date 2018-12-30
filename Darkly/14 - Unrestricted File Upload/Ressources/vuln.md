# Unrestricted File Upload

#### Page: _/index.php?page=upload_


## Description de la vulnérabilité :
Cette page permet d'envoyer une image sur le serveur de l'application.

Pour realiser cela, une requete POST est utilisée.
Le payload contient trois champs:
```
MAX_FILE_SIZE: 100000
uploaded:
Upload: Upload
```

En utilisant `curl` on tente d'envoyer un script php.

```
curl -X POST -F "uploaded=@./badscript.php;type=image/jpeg" -F "Upload=Upload" "http://[2a01:cb04:620:e100:a00:27ff:fef1:90dd]/index.php?page=upload
```

L'option `F` nous permet de specifier que l'on souhaite envoyer des data MIME en
--form-string
On spécifie le `type` `image/jpeg` afin de bypasser la vérification de type sur
le fichier passé en payload.


## Scénario d'attaque :
Les conséquences d'un téléchargement de fichier illégitime sont variés, même peuvent permettre notamment: le controle total du système, un dysfonctionnement du système de fichiers ou de la base de données, le transfert d'attaques par rebonds, des attaques côté client ou un simple déplacement sur le serveur.  
La gravité de la vulnérabilité dépend de ce que l'application fait avec le fichier téléchargé et surtout de son emplacement de stockage.
On peut imaginer de nombreux scenarios. Un attaquant pourraient upload des charges utiles qui seront executés cote client chez d'autres utilisateurs. L'upload d'un
fichier d'une taille de plusieurs centaine de giga octets pourraient permettre un
déni de service. Un attaquant pourrait compromettre le systeme sur lequel se trouve
le serveur en realisant une RCE.


## Correctifs :
- Listes des extensions à filtrer côté serveur comme `.php5`, `.pht`, `.phtml`, `.shtml`, `.asa`, `.cer` , `.asax`, `swf` ou `.xap`.
- Utiliser des fonctions comme `getimagesize ()` permettant d'attester le type
MIME et la taille du payload.
- Renommer le fichier envoyé par l'utilisateur afin qu'il ne puisse pas être appelé
par un script.
- Effectuer des scans anti-malware sur tous les fichiers envoyés par les utilisateurs.
- Imposer des limites en nombre d'upload.
- Imposer aux utilisateurs de s'authentifier avant de pouvoir upload des fichiers.
