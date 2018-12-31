# Stocked XSS

#### Page: _/index.php?page=feedback_


## Description de la vulnérabilité:
Après avoir testé de très nombreux payload XSS, on a fini par obtenir le flag
en écrivant seulement `script` dans le champ `mtxtMessage`.  
No comment.

## Scénario d'attaque:
Une vulnérabilité de type XSS stockée se produit lorsque les données fournies par un utilisateur sont stockées sur un serveur (dans une base de données, des fichiers, ou autre), et ensuite réaffichées sans que les caractères spéciaux HTML aient été encodés.
Un attaquant peut par exemple injecter du code afin de récupérer des cookies de session sur un serveur C2 ou sur une adresse mail qu’il aurait définie.  
Lorsque le code est exécuté côté client chez un autre utilisateur, le script
malveillant stocké en base s'exécute. Le script récupère les informations
contenues dans `document.cookie` contenant souvent des tokens ou des
`id` de session utilisateur. Le script envoie ses informations à l'attaquant
qui peut les utiliser afin d'usurper la session d'un autre utilisateur.



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
