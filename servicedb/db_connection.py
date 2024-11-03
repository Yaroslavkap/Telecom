import psycopg2

class Database:
    def __init__(self):
       
        self.conn = psycopg2.connect(
            host="db",
            database="my_database",
            user="my_user",
            password="my_password"
        )
        self.conn.autocommit = True

    def insert_record(self, data):
        
        with self.conn.cursor() as cursor:
            query = """
                INSERT INTO messages (name1, name2, name3, phone, message)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (data['name1'], data['name2'], data['name3'], data['phone'], data['message']))
