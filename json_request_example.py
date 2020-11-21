import pandas
import json
import requests

req = requests.get('https://services6.arcgis.com/8mobQf5ZkZ3Ps1Rs/arcgis/rest/services/Medicos_em_2019_WFL1/FeatureServer/7/query?where=1%3D1&outFields=*&outSR=4326&f=json',stream=True, timeout=None)

if req.status_code == 200:
    reddit_data = json.loads(req.content)

print(req.content)
