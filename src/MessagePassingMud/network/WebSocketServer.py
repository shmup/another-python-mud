'''
Created on Jun 6, 2012

@author: Nich
'''

import tornado.web
import tornado.websocket
import MessagePassingMud.network.login as login

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")
        self.data_handler = login.handle_login(self)
        
    def set_data_handler(self, data_handler):
        self.data_handler = data_handler

    def push(self, message):
        self.write_message(message)
    
    def on_message(self, message):
        if not self.data_handler is None:
            self.data_handler.send(message)
        

    def on_close(self):
        print("WebSocket closed")

