'''
Created on Nov 27, 2011

@author: Nich
'''
import tornado.ioloop
import tornado.web
from network.WebSocketServer import MainHandler, EchoWebSocket
from physics.gravity import gravity_callback
from map.game_map import GameMap
from data.data_store import DataStore
from player.player import Player
from player.inventory import inventory_callback
from model.data_map import DataMap
from model import Base, engine
from map.map_generators import generate_tile
from upgrades.jetpack import Jetpack


Base.metadata.create_all(engine)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket", EchoWebSocket),
])

if __name__ == "__main__":
    ##Init
    
    
    gmap = GameMap(generate_tile, DataMap)
    
    #Global state
    DataStore.instance().data["game_map"] = gmap
    DataStore.instance().data["default_player"] = Player("Nicholas", (0, 0), gmap)
    DataStore.instance().data["default_player"].add_upgrade(Jetpack()) 
    DataStore.instance().data["all_players"] = []
    DataStore.instance().data["account_connection"] = {}
    
    
    application.listen(8888)
    gravity = tornado.ioloop.PeriodicCallback(gravity_callback, 500, tornado.ioloop.IOLoop.instance())
    send_inventory = tornado.ioloop.PeriodicCallback(inventory_callback, 1000, tornado.ioloop.IOLoop.instance())
    #db_dump = tornado.ioloop.PeriodicCallback(dump_to_db, 5000, tornado.ioloop.IOLoop.instance())
    gravity.start()
    send_inventory.start()
    #db_dump.start()
    tornado.ioloop.IOLoop.instance().start()
    