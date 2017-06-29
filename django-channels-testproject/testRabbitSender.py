# -*- coding: utf-8 -*-

import pika
import time


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='asgi_channel')

count = 1

while (count > 0):
    channel.basic_publish(
        exchange='', routing_key='asgi_channel', body= "Тестовый проект: задача на обработку.")
    # print(time.strftime("%a, %d %b %Y %H:%M:%S") + " " + "Тестовый проект: задача на обработку.")
    count -= 1

connection.close()
