# Broken Authentification

#### Page: _/index.php?page=signin_

## Description de la vulnérabilité:
On remarque qu'il n'y a aucun délai et pas de système de catcha lorsqu'on tente de se connecter plusieurs fois sans succès.
Un script a la racine de ce dossier permet de réaliser un brute force sur l'utilisateur `admin`.
On trouve le mot de passe `shadow`.
On peut ainsi se connecter en administrateur.


## Scénario d'attaque :
Des worldlists constituées des mots de passe les plus utilisés sont disponibles sur le net.
Un script a la racine de ce dossier utilisant l'une de ces bases permet de réaliser un brute force sur l'utilisateur `admin`.


## Correctifs:
- Utiliser des mécanismes de protection contre le brute force, comme le bannissement d'une IP envoyant trop de requête de tentation de connexion ou bien utiliser un système de catcha.
- Locker les comptes recevant de nombreuses tentatives de connexion quelques dizaines de minutes.
