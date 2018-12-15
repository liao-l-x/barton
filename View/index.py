import tornado.web,tornado.ioloop
from Plug_ins.val_log import auth


class index_dm(tornado.web.RequestHandler):
    @auth
    def get(self,auth):#auth是session的字典
        self.render("index.html")