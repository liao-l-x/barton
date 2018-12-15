import tornado.web
from urls import application


from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)


if __name__ == "__main__":

    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

