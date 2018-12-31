# Reflected XSS

#### Page: _/index.php?page=media&src=nsa_



## Description de la vulnérabilité:
On remarque qu'une image a la page `/` est inclut dynamiquement par une méthode
GET et l'utilisation de la balise HTML `object`.
La requête utilise les paramètres `media` et `src`.

On teste différents encodages du payload XSS:
```
<script>alert(0);</script>
```
On finit par déterminer qu'un encodage en base64 sur le type image permet d'obtenir le flag.

```
page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgwKTwvc2NyaXB0Pg==
```

## Scénario d'attaque:
Les XSS réfléchies figurent parmi les vulnérabilités web les plus rencontrées.
Puisque le code s'exécute sur le client de l'utilisateur, elles ne sont
pas tout le temps exploitables et souvent considérées comme peu dangereuses par
les développeurs web.  
Cependant, en utilisant l'ingénierie sociale, un attaquant peut par exemple convaincre un utilisateur de suivre une URL piégée qui injecte du code dans la page de résultat.
Cela pourrait permettre à l'attaquant d'obtenir le contrôle sur le contenu de cette page.

## Correctifs:
- Retraiter systématiquement le code HTML produit par l'application avant l'envoi
au client
- Verifier les entrées utilisateurs
- Filtrer les variables affichées ou enregistrées avec des caractères `<` et `>`
- En PHP, utiliser les fonctions `htmlspecialchars()`​, `htmlentities()​` et `strip_tags()`
- Utiliser des modules serveur comme `mod_security` disponible pour les serveurs Apache, IIS7 et Nginx afin d'effectuer des vérifications sur les requêtes.
- Utiliser le header HTTP:
```
X-XSS-Protection: 1; mode=block
```
Permettant de désactiver l’exécution de scripts non autorisés.
