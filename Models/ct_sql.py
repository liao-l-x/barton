import pymysql
import  time
def sersor_data_insert(data,sid):
    """
    :param data: 传感器数据
    :param sid: 传感器id
    :return:
    """
    conn = pymysql.connect(host='192.168.31.215', port=3306, user='barton', passwd='123456', db='barton',
                           charset='utf8')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("insert into sersor_data values(null,%s,%s,%s)",(data,time.time(),sid))
    cursor.fetchall() #获取信息
    conn.commit()
    cursor.close()
    conn.close()
    return "执行完成！"

def sersor_data_select(sid):
    """
    查一条数据
    :param sid: 传感器id
    :return: 时间最近的一条传感器数据
    """
    conn = pymysql.connect(host='192.168.31.215', port=3306, user='barton', passwd='123456', db='barton',
                           charset='utf8')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select s_dm,s_dtime from sersor_data where s_d_sid=%s order by s_dtime desc limit 0,1",(sid))
    data = cursor.fetchall() #获取信息
    conn.commit()
    cursor.close()
    conn.close()
    return data

def sersor_history_select(sid):
    """

    :param sid: 传感器id
    :return: 后X 条数据
    """
    conn = pymysql.connect(host='192.168.31.215', port=3306, user='barton', passwd='123456', db='barton',
                           charset='utf8')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select s_dm,s_dtime from sersor_data where s_d_sid=%s order by s_dtime desc  limit 0,10", (sid))
    data = cursor.fetchall()  # 获取信息
    conn.commit()
    cursor.close()
    conn.close()
    return data

if __name__ == "__main__":
    # import random
    # for y in range(10):
    #     for i in range(1,8):
    #         sersor_data_insert(random.uniform(10,35),i)
    # print("生成数据并写入成功--7个传感器，每个10条数据！")
    pass