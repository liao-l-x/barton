import pymysql

def sersor_select(bid):#查询本鸡舍的所有传感器

    conn = pymysql.connect(host='192.168.31.215', port=3306, user='barton', passwd='123456', db='barton',
                           charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select sid from sersor where sbartonId = %s", (bid))
    info = cursor.fetchall()  # 获取信息
    conn.commit()
    cursor.close()
    conn.close()
    return info
if __name__ == "__main__":
    data = sersor_select(1)
    print(data)