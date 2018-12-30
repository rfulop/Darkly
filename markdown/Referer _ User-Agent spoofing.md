# Referer / User-Agent spoofing
#### Page: _/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c_

## Description de la vulnérabilité:

En inspectant le code source de la page on tombe sur les informations:
```
'You must cumming from : "https://www.nsa.gov/" to go to the next step'
```
et
```
Let's use this browser : "ft_bornToSec". It will help you a lot.
```
En suivant les indications *laissées pour nous*, on forge une requete GET avec le `User-Agent` et le `Referer` correspondant.

## Scénario d'attaque:
Il ne s'agit pas d'une vulnerabilité.
Dans certains cas, modifier les headers des paquets HTTP permet d'acceder à d'autres vulnerabilités côté serveur, comme les Cross-Site Request Forgery ou encore les XSS.

## Correctifs: 
- Certains headers HTTP ne sont pas sécurisables. Ainsi, si on souhaite filtrer l'origine des paquets HTTP on peut utiliser un système de token ou une vérification sur des `ids` de session.
- Ne pas écrire des informations sensibles en commentaires dans le code.
- Utilser les `Security Headers` définies par l'OWASP:
```
X-Frame-Options: SAMEORIGIN [1]
X-XSS-Protection: 1; mode=block [2]
X-Content-Type-Options: nosniff
Content-Type: text/html; charset=utf-8
```