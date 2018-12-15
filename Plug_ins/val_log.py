import Plug_ins.Session
# 处理刷新页面的请求
def auth(fun):
    def wrapper(self,*args,**kwargs):
        cooike_v = self.get_cookie("is_login")
        if cooike_v in Plug_ins.Session.Session_dict.keys():
            return fun(self,Plug_ins.Session.Session_dict,*args,**kwargs)
        else:
            self.redirect('/log.html')
    return wrapper