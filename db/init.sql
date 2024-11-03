DO $$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'my_database') THEN
      CREATE DATABASE my_database;
   END IF;
END $$;


\c my_database;
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    name1 VARCHAR(50),
    name2 VARCHAR(50),
    name3 VARCHAR(50),
    phone VARCHAR(15),
    message TEXT
);
