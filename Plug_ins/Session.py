import time
import hashlib

Session_dict = {}
class session:
    def __init__(self):
        md = hashlib.md5()  # 构造一个md5
        md.update(str(time.time()).encode("utf-8"))
        self.session_key =  md.hexdigest()# type :srt #获得的加密字符串
    def session_add(self,info):#从数据库查到的字典，包含username.userpwd id
        """
        :param info: 从数据库查到的字典，包含username.userpwd id
        """
        dict = {}
        dict[self.session_key] = info
        # user.set_cookie['is_login'] = 12132434#self.session_key
        Session_dict.update(dict)
        return  self.session_key
    def session_del(self,key):
        """
        :param key: 需要退出登入的用户还回的cookie
        :return: 退出用户的信息
        """
        value = Session_dict.pop(key)
        return value



