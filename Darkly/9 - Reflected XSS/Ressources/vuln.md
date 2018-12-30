# Reflected XSS

#### Page: _/index.php?page=media&src=nsa_



## Déscription de la vulnérabilité:
On remarque qu'une image a la page `/` est inclut dynamiquement par une methode
GET et l'utilisation de la balise HTML `object`.
La requete utilise les parametres `media` et `src`.

On teste different encodage du payload XSS:
```
<script>alert(0);</script>
```
On finit par determiner qu'un encodage en base64 sur le type image permet d'obtenir le flag.

```
page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgwKTwvc2NyaXB0Pg==
```

## Scénario d'attaque:
Les XSS réfléchies figurent parmi les vulnérabilités web les plus recontrées.
Puisque le code s'exécute sur le client de l'utilsateur, elles ne sont
pas tout le temps exploitables et souvent considérées comme peu dangereuses par
les développeurs web.  
Cependant, en utilsant l'ignegnerie sociale, un attaquant peut par exemple convaincre un utilisateur de suivre une URL piégée qui injecte du code dans la page de résultat.
Cela pourrait permettre à l'attaquant d'obtenir le contrôle sur le contenu de cette page.

## Correctifs:
- Retraiter systématiquement le code HTML produit par l'application avant l'envoi
au client
- Verifier les entrees utilisateurs
- Filtrer les variables affichées ou enregistrées avec des caractères `<` et `>`
- En PHP, utiliser les fonctions `htmlspecialchars()`​, `htmlentities()​` et `strip_tags()`
- Utiliser des modules serveurs comme `mod_security` disponible pour les serveurs Apache, IIS7 et Nginx afin d'effectuer des verification sur les requetes.
- Utiliser le header HTTP:
```
X-XSS-Protection: 1; mode=block
```
permettant de désactiver l’exécution de scripts non-autorisés.
