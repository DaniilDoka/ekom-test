# Web-приложение для определения заполненных форм.
используется: **Mongodb, docker compose, python 3.12, venv**
# запуск
для старта:
```
docker compose build

docker compose up
```
# получение формы
приложение запускается на порту 6666(можно переназначить все в конфиге, **app/.env**)

чтоб получить форму, нужно полсать post запрос на метод **/get_form**

значения можно отправлять любые
![image](https://github.com/user-attachments/assets/988772f1-ebf4-40a7-b681-3bf3c5aec563)

# тест
тестовая программа находится в директории **tests**

запуск:
```
source venv/bin/activate
pip install -r requirements.txt
python tests/tests.py
```

можно добавить свои данные для проверки

```
tests/tests.py
```
![image](https://github.com/user-attachments/assets/d26a90cd-173e-4dff-a750-9fd52e0d0d93)
