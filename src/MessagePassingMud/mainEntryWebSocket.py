'''
Created on Nov 27, 2011

@author: Nich
'''
import tornado.ioloop
import tornado.web
from network.WebSocketServer import MainHandler, EchoWebSocket
from physics.gravity import gravity_callback
from map.game_map import dump_to_db


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket", EchoWebSocket),
])

if __name__ == "__main__":
    application.listen(8888)
    gravity = tornado.ioloop.PeriodicCallback(gravity_callback, 1000, tornado.ioloop.IOLoop.instance())
    #db_dump = tornado.ioloop.PeriodicCallback(dump_to_db, 5000, tornado.ioloop.IOLoop.instance())
    gravity.start()
    #db_dump.start()
    tornado.ioloop.IOLoop.instance().start()
    