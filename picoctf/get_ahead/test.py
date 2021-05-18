import requests
url = "http://mercury.picoctf.net:53554/favicon.ico"

r = requests.get(url)

print(r.content)