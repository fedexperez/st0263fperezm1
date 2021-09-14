import pika
import sys

ip = sys.argv[1]
port = sys.argv[2]

user = ""
password = ""

while (len(user) and len(password)) <= 0:
    user = input("RabbitMQ user: ")
    password = input("RabbitMQ password: ")

connection = pika.BlockingConnection(pika.ConnectionParameters(
    str(ip), int(port), '/', pika.PlainCredentials(user, password)))
channel = connection.channel()

channel.queue_declare(queue='my_app', durable=True)

message = ''

print("Runnning Publisher Application...")

while True:
    try:
        message = input('Message: ')
        if message != '':
            channel.basic_publish(
                exchange='my_exchange',
                routing_key='test',
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                ))
            print(f" [x] Sent {message}")

    except KeyboardInterrupt:
        print('Keyboard Interrupt, CTRL + C pressed')
        print('Program closed')
        connection.close()
        sys.exit()
