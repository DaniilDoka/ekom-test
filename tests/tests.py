#!/usr/bin/python
import requests

url = 'http://localhost:6666/get_form'
data = [
    {
        'User Form': { 
            'username': 'danil',
            'myphone': '+7 895 234 65 24',
            'myemail': 'danil@mail.ru'
        },
        'Order Form': {
            'username': 'nedanil',
            'date_of_birth': '2013-13-13',
            'user_phone': '+7 455 254 65 45'
        },
        'Error Form': {
            'myphone': '+7 865 435 12 34',
            'mydate': '15.15.2024'
        },
    }
]

for d in data:
    for f_name, f in d.items():
        resp = requests.post(url, json=f)
        if 'form_name' in resp.json():
            print(f'----------{f_name}\n{f}\ncompared with {resp.json()['form_name']}\n----------')
        else:
            print(f'----------{f_name}\n{f}\nform not found\n----------')
            print(resp.json())
