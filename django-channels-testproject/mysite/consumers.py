# -*- coding: utf-8 -*-


# import json
from channels.channel import Channel
# from channels.channel import Group
from django.http import HttpResponse
from channels.handler import AsgiHandler
import time


def rabbitmq_request_consumer(message):
    print("*********************")
    print(message.content['message'])
    print(time.strftime("%a, %d %b %Y %H:%M:%S") + " " + "Принято сообщение: " + message.content['message'])

    # Channel("channel_for_reply").send({"message": "SUUUUUUPER " + time.strftime("%a, %d %b %Y %H:%M:%S")})
    Channel("channel_for_reply").send({"message": u"Ответ на задачу."})
    print(time.strftime("%a, %d %b %Y %H:%M:%S") + " " + "Отправлено сообщенние: Ответ на задачу")



# asgi_rabbitmq 5.2, pika 0.10


################################################
################################################
################################################
################################################
################################################


# Задачи:
# 1) собрать пакет с asgi_rabbitmq(с заменённым файлом core.py)
# 1.1) добавить пакет umsgpack
# 1.2) добавить файлы в пакет django channels
# 2) сделать скрипт для установки и настройки rabbitmq
# 3) дать права пользователю guest
# sudo rabbitmqctl set_permissions -p / guest ".*" ".*" ".*"
# end


# обновить код api(settings.py, routing.py, consumers.py, filters.py)


################################################
################################################
################################################
################################################
################################################
