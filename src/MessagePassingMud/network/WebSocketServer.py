'''
Created on Jun 6, 2012

@author: Nich
'''

import tornado.web
import tornado.websocket
import network.login as login



class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("Hello, " + name)
        self.render("web\mapper_test.html")

class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name"><br/>'
                   'Password: <input type="text" name="password">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        res = login.do_login(self.get_argument("name"), self.get_argument("password"))
        if res == "accepted":
            self.set_secure_cookie("user", self.get_argument("name"))
            self.redirect("/")
        elif res == "bad_password":
            self.write("Bad password")
        elif res == "account_not_found":
            self.write("Account not found")

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self): #@ReservedAssignment
        print("WebSocket opened")
        self.data_handler = login.login_handler(self)
        
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

