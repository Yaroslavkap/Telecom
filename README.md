## Описание
При запуске поднимает 5 контейнеров

├── frontend  
├── backend   
├── rabbitmq  
├── servicedb  
├── db  

Frontend, Backend и servicedb запускаются при помощи образов на astra linux. Frontend собирается в webpack.    
На Frontend части присутствует форма для обращений. После отправки обращение переходит на backend, где формируется объект и отправляется в очередь rabbitmq. Servicedb просматривает очередь и сохраняет полученные данные в БД PostgreSQL.

## Запуск

docker-compose up --build  


#### Frontend будет находится по адресу http://localhost:80/
#### Интерфейс rabbitmq http://localhost:15672/  

#### Для просмотра БД  

docker exec -it telecom-db-1 psql -U my_user -d my_database  (где "telecom-db-1" - название контейнера с БД)
SELECT * FROM messages;

