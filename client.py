import requests

url = 'http://localhost:3000/data'
files = {'image' : open('image.png', 'rb')}


res = requests.post(url, files=files)

print(res.text)
