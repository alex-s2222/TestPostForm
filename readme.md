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
1. Клонировать репозиторий
```
git clone https://github.com/alex-s2222/TestPostForm
```
2. Перейти в директорию 
```
cd TestPostForm
```
3. Создание образов (сервера и базы данных)
```
docker-compose build
```
4. Запуск (Сервера и базы данных) <br>
```
docker-compose up
```
5.  *для запуска в фоновом режиме, добавить ключ -d
```
docker-compose up -d
```
6. Запуск тестовых запросов (shell)
```
sh script.sh 
```
7. Запуск тестовых запросов (bash) *(*менее крассивый вывод*)
```
bash script.sh 
```
