# -*- coding: utf-8 -*-

from channels.routing import route
channel_routing = {
    'asgi_channel': 'mysite.consumers.rabbitmq_request_consumer',
    # 'websocket.connect': 'consumers.ws_connect',
    # 'websocket.receive': 'consumers.ws_message',
    # 'websocket.disconnect': 'consumers.ws_disconnect',
}
