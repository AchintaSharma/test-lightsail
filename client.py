import requests
import json

url = 'http://localhost:3000/data'
# files = {'image' : open('image.png', 'rb')}
data = {'data' : '100'}

res = requests.post(url, json=data)

print(res.text)
