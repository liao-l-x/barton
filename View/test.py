import tornado.web,tornado.ioloop
from Plug_ins.val_log import auth
from Models.ct_sql import sersor_data_select
from Models.bar_sql import sersor_select
import json
class test(tornado.web.RequestHandler):
    @auth
    def get(self, *args, **kwargs):
        self.render("test.html")
    @auth
    def post(self,auth, *args, **kwargs):
        dict = {}
        bartonId = auth[self.get_cookie("is_login")][0]["bartonId"]  # 获取鸡舍id
        for ct in sersor_select(bartonId):  # 获取所有的传感器sid stext(name)  数据————[ { 'sid':*},{*:* },* ]
            y = sersor_data_select(ct['sid'])  # 有数据是列表 [ { 'sid':*}]  ，没有数据就是 tuple
            dict[ct['sid']] = y[0]['s_dm']  # "传感器id":"传感器数据"
        self.write(json.dumps(dict))