'''
Created on Jun 6, 2012

@author: Nich
'''

import tornado.web
import tornado.websocket
import network.login as login

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self): #@ReservedAssignment
        print("WebSocket opened")
        self.data_handler = login.handle_login(self)
        
    def set_data_handler(self, data_handler):
        self.data_handler = data_handler

    def push(self, dest, message):
        import json
        self.write_message(json.dumps({dest:message}))
    
    def on_message(self, message):
        if not self.data_handler is None:
            self.data_handler.send(message)
        
    def on_close(self):
        print("WebSocket closed")

