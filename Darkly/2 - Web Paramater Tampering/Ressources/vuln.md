# Web Parameter Tampering 2

#### Page: _/index.php?page=survey_


## Description de la vulnérabilité:
La page permettant d'attribuer des notes aux `subject` utilise une requête de type GET possedant deux parametres `sujet` et `valeur`.
Il est possible d'attribuer à `valeur` un nombre < 1 et > 10 afin de fausser le resultat de `average`. 


## Scénario  d'attaque:
En modifiant la valeur de la note, on pourrait faire diminuer ou augmenter la moyenne de façon non controlé.


## Correctifs:
- Utiliser une methode de validation côté back, permettant d'ignorer toutes les valeurs non compris dans l'interval délimité.
- Stocker un id pour chaque utilisateur afin de prendre en compte les requêtes provenant d'utilisateurs n'ayant pas encore voté.