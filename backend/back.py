import json
import tornado.ioloop
import tornado.web
import pika

# Конфигурация RabbitMQ
RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'messages_queue'

# Функция для отправки сообщения в очередь RabbitMQ
def send_to_rabbitmq(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitMQ'))
    # credentials = pika.PlainCredentials('guest', 'guest')
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=False)
    channel.basic_publish(
        exchange='',
        routing_key=QUEUE_NAME,
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    print(" Сообщение отправлено в очередь RabbitMQ")
    connection.close()
    #print("Эмуляция отправки сообщения в RabbitMQ:", message)



class MessageHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        
        self.set_header("Access-Control-Allow-Origin", "*") 
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")

    def options(self):
        self.set_status(204)
        self.finish()

    def post(self):
        try:
            message = json.loads(self.request.body)
            required_fields = {"name1", "name2", "name3", "phone", "message"}
            if not all(field in message for field in required_fields):
                self.set_status(400)
                self.write({"error": "Missing fields in the request"})
                return

            send_to_rabbitmq(message)
            self.write({"status": "Message received and sent to queue"})

        except json.JSONDecodeError:
            self.set_status(400)
            self.write({"error": "Invalid JSON format"})


def make_app():
    return tornado.web.Application([
        (r"/submit", MessageHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Сервер Tornado запущен на http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()


