import pika
import json

class QueueHandler:
    def __init__(self, db):
        self.db = db
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitMQ'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='messages_queue')

    def callback(self, ch, method, properties, body):
        data = json.loads(body)
        
        self.db.insert_record(data)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_listening(self):
        self.channel.basic_consume(queue='messages_queue', on_message_callback=self.callback)
        print("Ожидание сообщений. Для выхода нажмите CTRL+C")
        self.channel.start_consuming()
