# praktikum_new_diplom
![workflow](https://github.com/NikolayRudakkov/yambd_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## **Об авторе:**


* Имя: Николай Рудаков	
* Род деятельности: Студент курса Яндекс.Практикум Python-разработчик
* Контакты: https://github.com/NikolayRudakov/


## **Описание:**

Foodgram это ресурс для публикации рецептов.
Пользователи могут создавать свои рецепты, читать рецепты других пользователей, подписываться на интересных авторов, добавлять лучшие рецепты в избранное, а также создавать список покупок и загружать его в pdf формате

---

## Подготовка и запуск проекта
### Клонирование репозитория
Склонируйте репозиторий на локальную машину:
```bash
git clone https://github.com/skarabey147/foodgram-project-react.git
cd foodgram-project-react/
```

### Перейдите в каталог inftra: ###
```bash
cd infra/
```

### Создайте .env файл и наполните его: ###
```bash
touch .env
```
Структура наполнения .env файла представлена в файле .env.example

### Запустите docker-compose в detach-режиме: ###
```bash
docker-compose up -d
```
____

## Внутри контейнера web ##

#### Выполните миграции: ####
```bash
docker-compose exec web python3 manage.py migrate
```
  
#### Заполните базу данных из csv файлов: ####
```bash
docker-compose exec web python3 manage.py populate_ingredient ingredients.csv
```
  
#### Создайте суперюзера: ####
```bash
docker-compose exec web python3 manage.py cratesuperuser
```

Теперь сервис доступен по адресу http://localhost/, а админка – http://localhost/admin/

