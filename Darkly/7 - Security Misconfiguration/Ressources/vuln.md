# Security Misconfiguration

#### Page: _/robots.txt_

## Description de la vulnérabilité:
Un fichier `robots.txt` contenant des commandes à destination des robots d'indexation des moteurs de recherche est parfois présent à la racine des applications web.
C'est le cas ici.
Robots.txt nous indique deux routes à exclure de l'indexation. La route `/whatever` contient un fichier nomme htpasswd qui contient un couple d'identifiants mot de passe:
root:8621ffdbc5698829397d97767ac13db3
Le mot de passe contient 32 caractères, caractéristique des hash md5.
En utilisant une rainbow table publique, on retrouve la chaîne de caractère a l'origine du md5: `shadow`.
On se connecte à l'application web avec les identifiants root.

## Scenario d'attaque:
Une fois qu'on a accès à l'interface d'administration d'une application web, on peut tout imaginer..

## Correctifs:

- Ne pas utiliser md5 qui n'est plus considéré comme solide depuis l'été 2004.
- Ne pas entrer ses identifiants dans des fichiers (utiliser des gestionnaires de mot de passe Open Source comme Keypass).
- Si on souhaite tout de même utiliser un fichier .htpasswd, il faut utiliser un fichier .htaccess avec d'empêcher l'accès a certains fichiers.
Il contiendrait au minimum ce code:
```
AuthName "Page d'administration protégée"
AuthType Basic
AuthUserFile "/PATH/.htpasswd"
Require valid-user
```
