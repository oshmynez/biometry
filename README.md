# biometry

Создать два микросервиса 
Gateway
Statistic

В первом микросервисе нужно реализовать прием http запросов от клиента и процессы авторизации и аутентификации эндпоинты должны быть следующими
Запрос на проверку данных
Запрос на создание данных (например паспортные данные)

В втором микросервисе нужно реализовать прием запросов от микросервиса Gateway 
Общения между микросервисами должно быть через gRPC
Должны быть реализованы две сущности Transaction and Operation
Все запросы в базу данных должны осуществляться через соответствующие репозитории
Нужно создать 3 запроса:
Запрос для создании операции
Запрос для создании транзакции 
Запрос для обновления статуса операции

Также применить безопасное общения между сервисами 
Все контейнеры должны запускаться через docker-compose

Микросервисы должны быть на питоне фреймворк FastAPI в качестве базы данных должен быть PostgreSQL.

> Первоначально для запуска необходимо запустить файл **prot.sh**
> а потом выполнить команду **docker-compose up -d**

