from tornado.websocket import WebSocketHandler

class ChatHandler(WebSocketHandler):

     users = set()  # 用来存放在线用户的容器
    #连接时执行
     def open(self):
         self.users.add(self)  # 建立连接后添加用户到容器中
    #客户端发信息时执行
     def on_message(self, message):
         pass
     #客户端退出时执行
     def on_close(self):
         self.users.remove(self) # 用户关闭连接后从容器中移除用户
     def check_origin(self, origin):
         return True  # 允许WebSocket的跨域请求