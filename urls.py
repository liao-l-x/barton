import tornado.web
from View import log,index,test

setting = {
    'template_path': 'Paje/templates',
    'static_path': 'Paje/static',
    'static_url_prefix': '/Paje/static/',
}

application = tornado.web.Application([
    (r"/log.html",log.log,),
    # (r'/index.html',index.index),
    (r'/test.html',test.test ),

],**setting)


