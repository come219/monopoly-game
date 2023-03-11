import requests
import json

url = 'http://localhost:8000/update'
data = {'x': 2, 'y': 3, 'value': 1}
response = requests.post(url, data=json.dumps(data))
print(response.text) # should print "OK"
