# Path traversal

#### Page: _/page=_


## Description de la vulnérabilité:
On remarque tenter de se déplacer dans l'arborescence en utilisant le paramètre `page` dans l'application génère de curieuses alertes.

On teste les URLs les plus communes pouvant contenir des fichiers sensibles lorsqu'ils ne sont pas protégés.

On trouve le flag à:

```
../../../../../../../etc/passwd
```

## Scénario d'attaque :
Fuzzing de wordlists d'URLs.


## Correctifs:
- Réaliser des autorisations appropriées afin d'accéder à des répertoires et des fichiers.
- Filtrer les entrées de l'utilisateur.
