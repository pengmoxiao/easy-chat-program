from DBUtil import *

db = DBUtil("gz-cdb-fvxckd3j.sql.tencentcdb.com", 63770, "root",
                    "N3DS7P7fSbJSMCtM", "test", "utf8mb4")
name = input("请输入用户名：")
password = input("请输入密码:")
ret = db.checkLogin('admin','a')
print(ret)