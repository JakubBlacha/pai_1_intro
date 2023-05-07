import requests
def download():
    pobrane = requests.get("https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json")
    return pobrane