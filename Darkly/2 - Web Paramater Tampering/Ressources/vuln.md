# Web Parameter Tampering 2

#### Page: _/index.php?page=survey_


## Description de la vulnérabilité :
La page permettant d'attribuer des notes aux `subject` utilise une requête de type GET possédant deux paramètres `sujet` et `valeur`.
Il est possible d'attribuer à `valeur` un nombre < 1 et > 10 afin de fausser le résultat de `average`.


## Scénario d'attaque :
En modifiant la valeur de la note, on pourrait faire diminuer ou augmenter la moyenne de façon non contrôlé.


## Correctifs :
- Utiliser une méthode de validation côté back, permettant d'ignorer toutes les valeurs non compris dans l'intervalle délimité.
- Stocker un id pour chaque utilisateur afin de prendre en compte les requêtes provenant d'utilisateurs n'ayant pas encore voté.
