import pika
import time
import sys

ip = sys.argv[1:]
port = sys.argv[2:]

user = ""
password = ""

while (len(user) and len(password)) <= 0:
    user = input("RabbitMQ user: ")
    password = input("RabbitMQ password: ")

connection = pika.BlockingConnection(pika.ConnectionParameters(
    str(ip), port, '/', pika.PlainCredentials(user, password)))


def callback(ch, method, properties, body):
    print(f'{body.decode()} is received')
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="my_app", on_message_callback=callback)

print("Runnning Consumer Application...")

while True:
    try:
        channel.start_consuming()

    except KeyboardInterrupt:
        print('Keyboard Interrupt, CTRL + C pressed')
        print('Program closed')
        channel.stop_consuming
        sys.exit()
