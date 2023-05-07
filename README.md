import requests
def download():
    pobrane = requests.get("https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json")
    return pobrane
try:
    r=requests.head("https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json")
    print(r.status_code)
except requests.ConnectionError:
    print("failet to connect")
