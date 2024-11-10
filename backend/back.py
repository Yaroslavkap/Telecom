import json
import asyncio
import tornado.ioloop
import tornado.web
import aio_pika



RABBITMQ_HOST = 'rabbitmq'
QUEUE_NAME = 'messages_queue'

class MessageHandler(tornado.web.RequestHandler):
    def initialize(self, rabbitmq_channel):
        self.rabbitmq_channel = rabbitmq_channel

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") 
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")

    def options(self):
        self.set_status(204)
        self.finish()

    async def post(self):
        try:
            message = json.loads(self.request.body)
            required_fields = {"name1", "name2", "name3", "phone", "message"}
            if not all(field in message for field in required_fields):
                self.set_status(400)
                self.write({"error": "Missing fields in the request"})
                return

            await self.send_to_rabbitmq(message)

        except json.JSONDecodeError:
            self.set_status(400)
            self.write({"error": "Invalid JSON format"})

    async def send_to_rabbitmq(self, message):
        await self.rabbitmq_channel.default_exchange.publish(
            aio_pika.Message(body=json.dumps(message).encode()),
            routing_key=QUEUE_NAME
        )
        print("Сообщение отправлено в очередь RabbitMQ(async)")


async def main():
    connection = await aio_pika.connect_robust(host=RABBITMQ_HOST)
    channel = await connection.channel()
    await channel.declare_queue(QUEUE_NAME, durable=True)

    app = tornado.web.Application([
        (r"/submit", MessageHandler, dict(rabbitmq_channel=channel)),
    ])
    app.listen(8888)
    print("Сервер Tornado запущен на http://localhost:8888(async)")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
