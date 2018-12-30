import sys
import requests
from bs4 import BeautifulSoup

URL = "http://10.12.1.138/.hidden/"

s = ''

resp = [
        "Demande Ã  ton voisin du dessus  ",
        "Demande Ã  ton voisin du dessous ",
        "Demande Ã  ton voisin de gauche  ",
        "Demande Ã  ton voisin de droite  ",
        "Non ce n'est toujours pas bon ...",
        "Tu veux de l'aide ? Moi aussi !  ",
        "Toujours pas tu vas craquer non ?",
        ]

def f(s):
    r = requests.get(URL+s)
    soup = BeautifulSoup(r.text, 'html.parser')

    l = []
    for link in soup.find_all('a'):
        l.append(link.get('href'))
    l = l[1:]
    if 'README' in l:
        #print('README on %s' % URL+s+'README')
        r = requests.get(URL+s+'README')
        data = r.text.replace('\n', '')
        
        if data not in resp:
            print('README on %s' % URL+s+'README')
            print("'%s'" % r.text)
            #sys.exit()  

    for e in l:
        f(s+e)

f(s)
