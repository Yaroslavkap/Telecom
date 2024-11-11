import asyncio
import json
import aio_pika
from aio_pika import connect_robust, IncomingMessage

class QueueHandler:
    def __init__(self, db):
        self.db = db
        self.connection = None
        self.channel = None

    async def start_listening(self):
        try:
            self.connection = await connect_robust(host='rabbitmq')
            self.channel = await self.connection.channel()
            await self.channel.set_qos(prefetch_count=1)

            await self.channel.declare_queue('messages_queue', durable=True)

            async def on_message(message: IncomingMessage):
                async with message.process():
                    data = json.loads(message.body)
                    await self.db.insert_record(data)
                    print("Сообщение обработано и записано в базу данных")

            queue = await self.channel.get_queue('messages_queue')
            await queue.consume(on_message)

            print("Ожидание сообщений. Для выхода нажмите CTRL+C")
            await asyncio.Future()

        except Exception as e:
            print("Ошибка при прослушивании очереди:")
            await self.connection.close()
