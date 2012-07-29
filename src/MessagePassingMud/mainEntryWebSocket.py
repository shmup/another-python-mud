'''
Created on Nov 27, 2011

@author: Nich
'''
import tornado.ioloop
import tornado.web
from network.WebSocketServer import MainHandler, EchoWebSocket, LoginHandler
from network.send_map_data import show_map_callback
from physics.gravity import gravity_callback
from map.game_map import GameMap
from data.data_store import DataStore
from player.player import Player
from player.inventory import inventory_callback
from model.data_map import DataMap
from model import Base, engine
from map.map_generators import generate_sector
from upgrades.jetpack import Jetpack
import os
#from map.start_ship import generate_starting_ship


Base.metadata.create_all(engine)

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "network\web"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket", EchoWebSocket),
    (r"/login", LoginHandler),
], **settings)


if __name__ == "__main__":
    ##Init
    
    gmap = GameMap(generate_sector, DataMap)
    
    #Global state
    DataStore.instance().data["game_map"] = gmap
    DataStore.instance().data["default_player"] = Player("Nicholas", (0, 0), gmap)
    DataStore.instance().data["default_player"].add_upgrade(Jetpack()) 
    DataStore.instance().data["all_players"] = []
    DataStore.instance().data["account_connection"] = {}
    
    
    application.listen(8888)
    gravity = tornado.ioloop.PeriodicCallback(gravity_callback, 500, tornado.ioloop.IOLoop.instance())
    send_map = tornado.ioloop.PeriodicCallback(show_map_callback, 50, tornado.ioloop.IOLoop.instance())
    send_inventory = tornado.ioloop.PeriodicCallback(inventory_callback, 1000, tornado.ioloop.IOLoop.instance())
    #db_dump = tornado.ioloop.PeriodicCallback(dump_to_db, 5000, tornado.ioloop.IOLoop.instance())
    #gravity.start()
    send_inventory.start()
    send_map.start()
    #db_dump.start()
    tornado.ioloop.IOLoop.instance().start()
    