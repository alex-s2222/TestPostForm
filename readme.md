# TEST TASK SEARCH FORM

---
## ТРЕБОВАНИЯ 
1. Docker, docker-compose (запуск)
2. shell/bash (отправка тестовых запросов)

---

## ИСХОДНЫЕ ДАННЫЕ
1. Файл с исходными формами находится -> [ФОРМЫ](https://github.com/alex-s2222/TestPostForm/blob/main/backend/db/inition.py)
2. web - flask
3. database - mongodb
---

## ЗАПУСК (от имени суперпользовалеля)
1. Создание образов (сервера и базы данных)
```
docker-compose build
```

2. Запуск (Сервера и базы данных) <br>

```
docker-compose up
```
2.  *для запуска в фоновом режиме, добавить ключ -d
```
docker-compose up -d
```
3. Запуск тестовых запросов (shell)
```
sh script.sh 
```
4. Запуск тестовых запросов (bash) *(*менее крассивый вывод*)
```
bash script.sh 
```
