# -*- coding: utf-8 -*-

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='channel_for_reply')

# count = 5

# while (count > 0):
#     channel.basic_publish(
#         exchange='', routing_key='asgi_channel', body='test')
#     count -= 1

connection.close()
