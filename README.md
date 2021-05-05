# polls
Для запуска приложения нужно:
1. Скачать репозиторий:\
```git clone https://github.com/Necro-master/polls.git```
2. Установить все зависимости:\
```pip install -r requirements.txt```
3. Создать и запустить redis в докере:\
```docker run --name=redis-devel --publish=6379:6379 --hostname=localhost --restart=on-failure --detach redis:latest```
4. Запустить celery:\
```celery worker -A EmolayPolls --loglevel=debug --concurrency=1```
5. Запустить миграцию \
```python manage.py makemigrations```\
```python manage.py migrate```
6. Запустить сервер Django\
```python manage.py runserver```
7. Создать супер пользователя\
```python manage.py createsuperuser```
## Что еще нужно знать?
- Добавлять опросы можно через админку. Далее на главной странице будет список всех опросов, которые можно пройти.
- В каждом опросе есть вопрос "Введите ваше имя". Оно нужно для генерации pdf.
- Если пользователь не суперюзер, то он не может посмотреть результаты голосования.
- Ответы пользователей отображаются жирным шрифтом.
