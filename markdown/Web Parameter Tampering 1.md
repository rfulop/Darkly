# Web Parameter Tampering 1

#### Page: _/index.php?page=recover_


## Description de la vulnerabilte:
En inspectant la page `?page=recover`, on remarque qu'elle ne contient qu'un unique bouton `submit`.
On inspecte la request POST, qui contient un champs `mail` avec pour valeur `webmaster@borntosec.com`.
L’inspection du HTML permet de découvrir le champ en `hidden`:
```
<input name="mail" value="webmaster@borntosec.com" maxlength="15" type="hidden">
```

En modifiant la valeur du champs `mail` avant l'envoie de la requete, on peut alors envoyer des courriels a n'importe quel adresse email depuis l'application web.

## Scénario d'attaque:
Mail bombing depuis l'application web.

## Correctifs:
- Mettre en place une politique interne afin d'appliquer le principe de base en securite web: Don't trust user input
- Gerer les parametres sensibles et non necessaire a l'experience utilisateur cote back.