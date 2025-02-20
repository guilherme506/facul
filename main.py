import requests  
import json
r = requests.get("https://rickandmortyapi.com/api/character/558")
persongem = json.loads(r.text)
print(persongem["name"])