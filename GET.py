import requests

    url ="https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

try:
    r = requests.head("https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json")
    print(r.status_code)

except requests.ConnectionError:
    print("failed to connect")
