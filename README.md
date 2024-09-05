#Nekta test task

При сборке контейнера создается 2 пользователя:
С доступом к административной панели:
```
{
    "username": "admin",
    "password": "admin"
}
```
Без доступа к административной панели:
```
{
    "username": "user",
    "password": "user"
}
```

<server_uri> = localhost:8000
## Авторизация
Для получения token необходимо отправить POST-запрос, в body которого будут логин и пароль в формате:
```
{
    "username": "user",
    "password": "user"
}
```
Пример ответа на запрос token:
```
{
    "token": "c201907d550639c3e3d14fc3d2fdfadc5a6268a3"
}
```

Для доступа к ендпоинтам, кроме, '<server_uri>/v1/token/', необходим что-бы в header запроса был активный token в таком виде:
```
{
  "Authorization": "Token c201907d550639c3e3d14fc3d2fdfadc5a6268a3",
}
```

### Заявки
- Получение списка заявок
  - GET <server_uri>/v1/request/

- Получение информации о заявке по ID
  - GET <server_uri>/v1/request/<id>

- Создание заявки
  - POST <server_uri>/v1/request-add/

Пример body для создания заявки:
```
{
    "title": "Пример загаловка заявки",
    "content": "Пример текста заявки"
}
```
  
### Сообщения
- Получение списка сообщений по заявке
  - GET <server_uri>/v1/messages/<id>/

- Отправка сообщения в заявку
  - POST <server_uri>/v1/message-add/

Пример body для отправки сообщения в заявку с id == 1:
```
{
    "request": 1,
    "content": "Пример текста для сообщения"
}
```
