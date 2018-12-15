import tornado.web,tornado.ioloop
# import Models.log_sql.log_select as log_select
from Models.log_sql import  log_select
from Plug_ins.Session import session #自定义的session插件


class log(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html",username='',userpwd='')
    def post(self):
        username = self.get_argument("username",None)#用户名
        userpwd = self.get_argument("userpwd",None)#密码
        # session_u = self.get_argument("cookie",None)
        z_user = log_select(username)#数据库查询
        if z_user != ():
            if z_user[0]['userpwd']== userpwd :
                # session().session_add(info=z_user,user=self) #添加session
                self.set_cookie('is_login',session().session_add(info=z_user))
                self.redirect("/index.html")#登入成功转跳到主页
        else:
            self.render("login.html",
                        username=username,
                        userpwd=userpwd)#登入失败，再次还回登入界面，记忆上传的用户名密码

