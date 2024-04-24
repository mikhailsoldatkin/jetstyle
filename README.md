#### 1. Создать файл .env, заполнить данными из env.example
#### 2. Запустить проект

```
 docker compose up -d
```

#### 3. Провести миграции в терминале контейнера jetstyle_app:

```
python manage.py migrate
```
