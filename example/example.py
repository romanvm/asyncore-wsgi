# coding: utf-8
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: roman1972@gmail.com

import logging
import os
import sys
from wsgiref.simple_server import demo_app

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from asyncore_wsgi import AsyncWebSocketHandler, make_server


class SimpleEchoHandler(AsyncWebSocketHandler):

    def handleMessage(self):
        logging.info('Received WebSocket message: {}'.format(self.data))
        self.sendMessage(self.data)

    def handleConnected(self):
        logging.info('WebSocket connected')

    def handleClose(self):
        logging.info('WebSocket closed')


if __name__ == '__main__':
    httpd = make_server('', 8000, demo_app, ws_handler_class=SimpleEchoHandler)
    httpd.serve_forever()
