import pymysql
# 连接数据库
con = pymysql.connect(host="api.lemonban.com",
                                  port=3306,
                                  user="future",
                                  password="123456",
                                  charset="utf8",
                                    # cursorclass=pymysql.cursors.DictCursor
                                  # cursorclass=pymysql.cursors.DictCursor 返回的是字典格式数据，默认是元组
                                  )
# 创建游标对象
print(con)
sql = "SELECT * FROM futureloan.member WHERE id < 5"
cur = con.cursor()
# 执行dql语句
a = cur.execute(sql)
print(a)
