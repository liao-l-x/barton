import tornado.web
from View import log,index,test
from View.sql import seosor_data_select

setting = {
    'template_path': 'Paje/templates',
    'static_path': 'Paje/static',
    'static_url_prefix': '/Paje/static/',
}

application = tornado.web.Application([
    (r"/log.html",log.log,),
    (r'/dm.html',index.index_dm),
    (r'/test.html',test.test ),

    (r'/dm_data.html',seosor_data_select.dm_data),
    (r'/history_data.html',seosor_data_select.history_data),

],**setting)


