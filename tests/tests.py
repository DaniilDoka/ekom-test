#!/usr/bin/python
import requests
from pymongo import MongoClient

client = MongoClient('mongodb://root:pass1234@localhost:27017/')
db = client['mydb']
print(db.command('ping'))

collection = db['test']
collection.insert_one({ 'name': 'User Form', 'user_phone':'phone', 'user_mail':'email', 'user_name':'text' })
collection.insert_one({ 'name': 'Order Form', 'order_date':'date', 'user_name':'text', 'user_phone':'phone' })

url = 'http://localhost:6666/get_form'
data = [
    {
        'User Form': { 
            'username': 'danil',
            'myphone': '+7 895 234 65 24',
            'myemail': 'danil@mail.ru',
            'testtxt': 'aaaa'
        },
        'Order Form': {
            'username': 'nedanil',
            'date_of_birth': '2013-13-13',
            'user_phone': '+7 455 254 65 45',
            'other_phone': '+7 555 334 54 23'
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
