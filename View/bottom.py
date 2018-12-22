import tornado.web,tornado.ioloop
from View.dm_cr import ChatHandler

class dm_data(tornado.web.RequestHandler):
    """
    代码逻辑：接受底层的get 的数据，在调用websverer 发送的前端
    """
    def get(self):
        data_dict = {}
        Sn = self.get_argument("Sn")
        Sd = self.get_argument("Sd")
        data_dict['Sn']=Sn
        data_dict['Sd']=Sd
        for u in ChatHandler.users:  # 向在线用户广播消息
            u.write_message(message=data_dict, binary=False)
        self.write("cg")


#底层socket代码
"""
import socket

sock = socket.socket()
sock.connect(('192.168.31.134',8080))
def socket_get(url):
    mysock ="GET "+url+" HTTP/1.1\r\nHost: restapi.amap.com\r\n\r\n"
    sock.send(mysock.encode('utf-8'))
    response = b''
    chunk = sock.recv(1024)
    print(chunk)
    while chunk:  # 循环接收数据，若没有数据了说明已接收完
        response += chunk  # 字符串拼接
        chunk = sock.recv(1024)
    sock.close()
    return response
p =socket_get("/dm_data?Sn=5&Sd=34")

print(p.decode('utf-8'))
"""
#前端js代码
"""
var ws = new WebSocket("ws://192.168.31.134:8080/chat");
         ws.onmessage = function(e) {
             var  dict = $.parseJSON(e.data)
            
             switch (dict["Sn"]){
                 case "1":
                     my$("Temp").innerHTML="温度传感器："+dict["Sd"];
                     break;
                 case "2":
                     my$("Humi").innerHTML="湿度传感器："+dict["Sd"];
                     break;
                 case "3":
                     my$("Light").innerHTML="光照传感器："+dict["Sd"];
                     break;
                 case "4":
                     my$("Gas").innerHTML="有害气体传感器："+dict["Sd"];
                     break;
                 case "5":
                     my$("Co2").innerHTML="二氧化碳传感器："+dict["Sd"];
                     break;
                 case "6":
                     my$("Air").innerHTML="气压传感器："+dict["Sd"];
                     break;
                 case "7":
                      my$("Wind").innerHTML="风速传感器："+dict["Sd"];
                     break;
             }
"""