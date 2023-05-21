import os,getpass
from DBUtil import *

db = DBUtil("gz-cdb-fvxckd3j.sql.tencentcdb.com", 63770, "root",
                    "N3DS7P7fSbJSMCtM", "test", "utf8mb4")
os.system("cls")

print("欢迎使用德猴制作的聊天工具!")
username = input("请输入用户名：")
password = getpass.getpass("请输入密码:")

ret = db.checkLogin(username,password)

print(ret)
# if (ret == -1):
#     print("登陆失败，服务器或网络出错")
# elif (ret == 0):
#     print(db.getnick(username))