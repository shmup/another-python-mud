'''
Created on Nov 27, 2011

@author: Nich
'''
import tornado.ioloop
import tornado.web
from MessagePassingMud.network.WebSocketServer import MainHandler, EchoWebSocket


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket", EchoWebSocket),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()