# Broken Access Control

#### Page: _Toutes_


## Description de la vulnérabilité:
Un cookie valable sur toutes les pages de l'application web contient la clef `I_am_admin`.
La valeur de cette clef est:
```
68934a3e9455fa72420237eb05902327
```
Soit `false` en MD5.

On hash `true` en MD5 soit:
```
b326b5062b2f0e69046810717534cb09
```
On modifie la valeur du cookie puis on actualise la page. On est connecté en administrateur.

Par ailleurs, on remarque que les attributs `secure` et `httpOnly` sont set a `False`, ce qui est un defaut de sécurité.
`secure` force l'utilisation de HTTPS pour l'envoi du cookie afin de mitiger les attaques de type man-in-the-middle.
`httpOnly` indique aux navigateurs Web de ne pas autoriser les scripts.

## Scénario  d'attaque:
Modifier la valeur du cookie et lui attribuer la valeur de `true` en md5 permet d'être connecté en administrateur sur l'application web et ainsi d'accéder aux fonctionnalités d'administration.


## Correctifs:
- Utiliser des `id` de session, générer aléatoirement et les renouveler régulièrement.
- Se baser sur un système de token ou d'id de session pour accorder ou non des privilèges plus élevés à un utilisateur.
- Définir à `true` les attributs `secure` et `http_only`.
