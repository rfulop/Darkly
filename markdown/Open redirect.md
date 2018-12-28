# Open redirect
#### Page: _/index.php_

## Description de la vulnerabilité:
En bas de la page, on remarque des liens vers les réseaux sociaux dont la redirection est assuré par un champ  `redirect` dans une requête GET.
En modifiant la valeur de ce champ, on est en mesure de rediriger un utilisateur vers une URL .

## Scénario d'attaque:
Une attaque par hameçonnage dans laquelle un attaquant usurperait un site web. Si les utilisateurs ne font pas attention a la barre d'URL, ils pourraient saisir leurs identifiants sur un site web malveillant imitant un site légitime, et les communiquer à un attaquant.

## Correctifs :
- Ne pas utiliser de redirection.
- Une méthode de validation si on choisit tout de même d'utiliser une requête de redirection.
- Créer une liste d'URL de confiance.
- Forcer toutes les redirections partant de l'application Web à passer par une page informant les utilisateurs qu'ils quittent le site et leur demander de confirmer l'action.