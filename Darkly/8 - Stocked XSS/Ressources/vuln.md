# Stocked XSS

#### Page: _/index.php?page=feedback_


## Déscription de la vulnérabilité:
Après avoir tésté de très nombreux payload XSS, on a fini par obtenir le flag
en écrivant seulement `script` dans le champ `mtxtMessage`.  
No comment.

## Scénario d'attaque:
Une vulnérabilité de type XSS stockée se produit lorsque les données fournies par un utilisateur sont stockées sur un serveur (dans une base de données, des fichiers, ou autre), et ensuite ré-affichées sans que les caractères spéciaux HTML aient été encodés.
Un attaquant peut par exemple injecter du code permettant de récupére sur un
serveur C2 ou une adresse email des cookies de session.  
Lorsque le code est éxécuté coté client chez un autre utilisateur, le script
malveillant stocké en base s'éxucute. Le script recupere les informations
contenues dans `document.cookie` contenant souvent des tokens ou des
`id` de session utilisateur. Le script envoie ses informations à l'attaquant
qui peut les utiliser afin d'usurper la session d'un autre utilisateur.



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
