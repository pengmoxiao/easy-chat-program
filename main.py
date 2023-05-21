import os,getpass,sys
from DBUtil import *

def main(username):
    os.system("cls")
    print("你想干嘛~哎呦:")
    try :
        choice = int(input("1:进入单聊 2:修改密码 3:修改昵称\n"))
        if (choice == 1):
            os.system("pause")
        elif (choice == 2):
            change_password(username)
        elif (choice == 3):
            change_nick(username)
        else:
            os.system("cls")
            print("认真点!")
            main()
    except:
        os.system("cls")
        print("认真点!")
        main(username)

def change_password(username):
    os.system("cls")
    old_passwd = getpass.getpass("请输入原密码:")
    ret = db.checkLogin(username,old_passwd)
    if (ret == 0 or ret == 1):
        new_passwd = getpass.getpass("请输入新密码:")
        re_new_passwd = getpass.getpass("请再次输入新密码:")
        if (new_passwd == re_new_passwd):
            db.change_password(username,new_passwd)
            print("修改成功!")
            os.system("pause")
            main()
        else:
            print("两次密码不一致1")
            os.system("pause")
            main()
    else:
        print("原密码错误！")
        os.system("pause")
        main()

def change_nick(username):
    os.system("cls")
    old_passwd = getpass.getpass("请输入密码:")
    ret = db.checkLogin(username,old_passwd)
    if (ret == 0 or ret == 1):
        new_nick = input("请输入新的昵称:")
        db.change_nick(username,new_nick)
        print("修改成功!")
        os.system("pause")
        main()
    else:
        print("密码错误！")
        os.system("pause")
        main()



db = DBUtil("gz-cdb-fvxckd3j.sql.tencentcdb.com", 63770, "root",
                    "N3DS7P7fSbJSMCtM", "test", "utf8mb4")
os.system("cls")

print("欢迎使用德猴制作的聊天工具!")
username = input("请输入用户名：")
password = getpass.getpass("请输入密码:")

ret = db.checkLogin(username,password)

if (ret == -1):
    print("登陆失败，服务器或网络出错")
elif (ret == 0 or ret == 1):
    print("你好，",db.getnick(username),"，欢迎登录德猴的聊天工具!")
    os.system("pause")
    main(username)
elif (ret == -2):
    print("用户名或密码错误！")