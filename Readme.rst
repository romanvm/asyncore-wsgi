asyncore-wsgi
=============

This is a single-threaded asynchronous WSGI server with WebSockets support
based on `asyncore <https://docs.python.org/3.6/library/asyncore.html>`_ module.
It should be compatible with Python 2.7 and 3.

Example:

.. code-block:: python

    from from wsgiref.simple_server import demo_app
    from asyncore_wsgi import AsyncWebSocketHandler, make_server


    class SimpleEchoHandler(AsyncWebSocketHandler):

        def handleMessage(self):
            print('Received WebSocket message: {}'.format(self.data))
            self.sendMessage(self.data)

        def handleConnected(self):
            print('WebSocket connected')

        def handleClose(self):
            print('WebSocket closed')


    httpd = make_server('', 8000, demo_app, ws_handler_class=SimpleEchoHandler)
    httpd.serve_forever()

The server in the preceding example serves a demo WSGI app from
the Standard Library and the echo WebSocket handler on ``'/ws'`` path.

WebSocket part was borrowed from
`this project <https://github.com/dpallot/simple-websocket-server>`_.

License
-------

MIT, see LICENSE.txt
