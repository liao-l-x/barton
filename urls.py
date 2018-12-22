import tornado.web
from View import log,index,test,bottom,dm_cr
from View.sql import seosor_data_select
from View import test1

setting = {
    'template_path': 'Paje/templates',
    'static_path': 'Paje/static',
    'static_url_prefix': '/Paje/static/',
}

application = tornado.web.Application([
    #前端
    (r"/log.html",log.log,),
    (r'/dm.html',index.index_dm),
    (r'/test.html',test.test ),
    #数据
    (r'/dm_data.html',seosor_data_select.dm_data),
    (r'/history_data.html',seosor_data_select.history_data),
    (r"/dm_cr",dm_cr .ChatHandler),#动态监控的数据，为保证时效性，不经过数据库

    #底层
    (r'/dm_data', bottom.dm_data),
    #test
    (r"/chat", test1.ChatHandler),
],**setting)


