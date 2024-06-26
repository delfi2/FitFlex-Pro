import json
import requests

def get_lluvia():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=precipitation'
    r = requests.get(url)
    data=json.loads(r.text)
    lluvia = data['current']['precipitation']
    return lluvia
