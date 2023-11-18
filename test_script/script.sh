#!/bin/bash

# URL сервера, куда отправляется POST-запрос
url="http://localhost:8080/get_form"

# Данные для отправки 
pr_date="33.22.3223"
pr_phone="+7 916 380 00 77"
pr_name="alexey"


echo "№1ВХОД: дaнные совпадающей с формой "
echo "\tpr_date="33.22.3223"\n\tpr_phone="+7 916 380 00 77"\n\tpr_name="alexey""
echo "ВЫХОД:"
curl -X POST -d "pr_date=$pr_date&pr_name=$pr_name" --data-urlencode "pr_phone=$pr_phone" "$url"


echo "\n№2ВХОД: добавляем к №1 еще 1 поле -> Полей больше чем в форме"
field="field"
echo "ВЫХОД:"
curl -X POST -d "pr_date=$pr_date&pr_name=$pr_name&field=$field" --data-urlencode "pr_phone=$pr_phone" "$url"


echo "\n№3ВХОД: убираем из №1 одно поле"
echo "ВЫХОД"
curl -X POST -d "pr_date=$pr_date&pr_name=$pr_name" "$url"


echo "\n№4ВХОД: ошибно пишем ключ из №1"
echo "ВЫХОД"
curl -X POST -d "pr_=$pr_date&pr_name=$pr_name" --data-urlencode "pr_phone=$pr_phone" "$url"

my_date="33.22.3223"
my_phone="+7 916 380 00 77"
my_name="alexey"
my_email="alex@gmail.com"


echo "\n№5ВХОД: другие дaнные совпадающей с формой "
echo "\tmy_date="33.22.3223"\n\tmy_phone="+7 916 380 00 77"\n\tmy_name="alexey"\n\tmy_email="alex@gmail.com""
echo "ВЫХОД:"
# отправляем запрос 1 к 1 
curl -X POST -d "my_date=$my_date&my_name=$my_name&my_email=$my_email" --data-urlencode "my_phone=$my_phone" "$url"

