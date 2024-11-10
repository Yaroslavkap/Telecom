import asyncpg
import asyncio

class Database:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            min_size=1,
            max_size=10
        )

    async def insert_record(self, data):
        async with self.pool.acquire() as conn:
            query = """
                INSERT INTO messages (name1, name2, name3, phone, message)
                VALUES ($1, $2, $3, $4, $5)
            """
            await conn.execute(query, data['name1'], data['name2'], data['name3'], data['phone'], data['message'])

    async def close(self):
        if self.pool:
            await self.pool.close()

