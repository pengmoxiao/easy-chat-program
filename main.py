import os,getpass
from DBUtil import *

db = DBUtil("gz-cdb-fvxckd3j.sql.tencentcdb.com", 63770, "root",
                    "N3DS7P7fSbJSMCtM", "test", "utf8mb4")
# os.system("cls")

# print("欢迎使用德猴制作的聊天工具!")
# name = input("请输入用户名：")
# password = getpass.getpass("请输入密码:")

# ret = db.checkLogin(name,password)
# if (ret == 2)

# print(ret)

db.create_chat("a","b","c")