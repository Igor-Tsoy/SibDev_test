# Тестовое задание SibDev

### Установка и запуск сервиса

Копируем данный репозиторий

~~~
$ git clone https://github.com/Rimasko/juniorTest.git
$ cd juniorTest
~~~

Запускаем сборку docker-compose

~~~
$ docker-compose build
~~~

Запускаем сервис

~~~
$ docker-compose up
~~~

### Работа с сервисом

По адресу http://0.0.0.0:8000/ (http://192.168.99.100:8000/ для Docker Toolbox) можно POST запрос с файлом .csv (также при необходимости содержится форма для отправки файла).

Получить результат:
* handle/table/ - в виде html таблицы
* handle/json/ - в JSON
* handle/xml/ - в xml