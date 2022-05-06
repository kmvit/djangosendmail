## Установка и запуск

1. Склонировать репозиторий с Github:

````
git clone https://github.com/kmvit/djangosendmail.git
````
2. Создать виртуальное окружение:

````
python -m venv env
````

4. Активировать окружение: 

````
source\venv\bin\activate
````
5. Установить зависимости:

```
pip install -r requirements.txt
```

7. Создать и применить миграции в базу данных:
```
python manage.py makemigrations
python manage.py migrate
```
8. Запустить сервер
```
python manage.py runserver
```
9. Запустить celery
```
celery -A djangomailservice worker -l info
```
10. Запустить flower

```
celery -A djangomailservice flower --port=5555
```
Переходим по адресу http://127.0.0.1:8000/api/