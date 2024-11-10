import asyncio
from queue_handler import QueueHandler
from db_connection import Database

async def main():
    db = Database(host="db", database="my_database", user="my_user", password="my_password")
    await db.connect()

    queue = QueueHandler(db)
    await queue.start_listening()

if __name__ == "__main__":
    asyncio.run(main())
