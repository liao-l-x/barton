import pymysql


def test_insert(name,pwd):
    """
    添加数据
      id 自增
    :param name: varchar(20)
    :param pwd: varchar(30)
    :return: unll
    """

    conn = pymysql.connect(host='192.168.31.215', port=3306, user='root', passwd='123456', db='test1', charset='utf8')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("INSERT INTO user1 values(null,%s,%s)",(name,pwd))
    conn.commit()  # 提交
    cursor.close()
    conn.close()
def tset_select(nid):
    """
    id 查询
    :param nid: sqlbd tinyint
    :return:
    """
    conn = pymysql.connect(host='192.168.31.215', port=3306, user='root', passwd='123456', db='test1', charset='utf8')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select username,password from user1 where id = %s ",(nid))
    pwd = cursor.fetchall() #获取信息
    conn.commit()
    cursor.close()
    conn.close()
    return pwd
def tset_update(path,nid):
    #改
    conn = pymysql.connect(host='192.168.31.215', port=3306, user='root', passwd='123456', db='test1', charset='utf8')
        # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("update user1 set password = %s where id =%s",(path,nid))
    conn.commit() #提交
    cursor.close()
    conn.close()
    return cursor.lastrowid
def tset_delete(nid):
    #改
    conn = pymysql.connect(host='192.168.31.215', port=3306, user='root', passwd='123456', db='test1', charset='utf8')
        # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from user1 where id =%s",(nid))
    conn.commit() #提交
    cursor.close()
    conn.close()
    return cursor.lastrowid
