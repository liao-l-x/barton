import pymysql

# conn = pymysql.connect(host='192.168.31.215', port=3306, user='barton', passwd='123456', db='barton', charset='utf8')

def log_select(username):
    """
    id 查询
    :param nid: sqlbd tinyint
    :return:
    """
    conn = pymysql.connect(host='192.168.31.215', port=3306, user='barton', passwd='123456', db='barton',
                           charset='utf8')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select bartonId,userpwd,username,uid from user_bar where username = %s ",(username))
    userpwd = cursor.fetchall() #获取信息
    conn.commit()
    cursor.close()
    conn.close()
    return userpwd
if __name__ == "__main__":
    tset = log_select('root')
    print(tset)