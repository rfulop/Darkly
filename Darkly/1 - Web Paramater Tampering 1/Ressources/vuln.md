# Web Parameter Tampering 1

#### Page: _/index.php?page=recover_


## Description de la vulnérabilité :
En inspectant la page `?page=recover`, on remarque qu'elle ne contient qu'un unique bouton `submit`.
On inspecte la request POST, qui contient un champs `mail` avec pour valeur `webmaster@borntosec.com`.

L’inspection du HTML permet de découvrir le champ en `hidden`:
```
<input name="mail" value="webmaster@borntosec.com" maxlength="15" type="hidden">
```

En modifiant la valeur du champs `mail` avant l'envoi de la requête, on peut alors envoyer des courriels a n'importe quel adresse e-mail depuis l'application web.

## Scénario d'attaque :
Mail bombing depuis l'application web pouvant provoquer un déni de service.

## Correctifs :
- Mettre en place une politique interne afin d'appliquer le principe de base en sécurité web: Don't trust user input.
- Gérer les paramètres sensibles et non-nécessaire à l'expérience utilisateur côté back.
