## Запуск

docker-compose up --build  


#### Frontend будет находится по адресу http://localhost:80  

#### Для просмотра БД  

docker exec -it telecom-db-1 psql -U my_user -d my_database  
SELECT * FROM messages;

