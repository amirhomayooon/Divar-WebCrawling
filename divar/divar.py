from distutils import text_file
from email import header
from decouple import config
import requests

url = config('url')

json = config('json')
header = {
    'Content-Type': 'application/json'
}

res = requests.post(url, headers=header, json=json)
data = res.json()
last_post_date = data['last_post_date']

list_of_tokens = []

count = 0
while True:
    json = config('json2')
    res = requests.post(url, json=json, headers=header)
    data = res.json()
    last_post_date = data['last_post_date']

    for widget in data['web_widgets']['post_list']:
        token = widget['data']['token']
        list_of_tokens.append(token)
        count += 1

    if count >= 100:
        break

text_file = open('tokens.txt', 'w', encoding='utf8')
text_file.write('.'.join(list_of_tokens))
text_file.close
