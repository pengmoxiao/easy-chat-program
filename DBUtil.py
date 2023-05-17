import pymysql
import bcrypt


class DBUtil:
    con = None

    def __init__(self, host, port, user,
                 passwd, db, charset):
        # print(host, port, user, passwd, db, charset)
        self.__host = host
        self.__port = port
        self.__user = user
        self.__passwd = passwd
        self.__db = db
        self.__charset = charset
        self.getMySQLConn()

    def getMySQLConn(self):
        global con
        print("连接数据库中......")
        con = pymysql.connect(host=self.__host, port=self.__port, user=self.__user,
                              passwd=self.__passwd, db=self.__db, charset=self.__charset)
        print("连接成功!")

    def getCursor(self):
        cursor = con.cursor()
        return cursor

    def createTable(self, sql):
        ret = self.getCursor().execute(sql)
        return ret     

    def query(self, sql):
        cursor = self.getCursor()
        cursor.execute(sql)
        ret = cursor.fetchall()
        return ret
    
    def executeUpdate(self,sql):
        try:
            cursor = self.getCursor()
            cursor.execute(sql)
            con.commit()
            return 1
        except:
            return 0
        
    def change_password(self, username, new_pwd):
    # 加密过程
        salt = bcrypt.gensalt(rounds=10)
        encrypt_passwd = bcrypt.hashpw(new_pwd.encode(), salt)
        sql = "update users set password='{}' where username='{}'".format(str(encrypt_passwd,"utf-8"),username)
        self.executeUpdate(sql)

    def register(self, username,pwd,role):
    # 加密过程
        salt = bcrypt.gensalt(rounds=10)
        encrypt_passwd = bcrypt.hashpw(pwd.encode(), salt)
        sql = "insert into users(username,password,role)values('{}','{}','{}')".format(
                username,str(encrypt_passwd, "utf-8"),role)
        self.executeUpdate(sql)

    def checkLogin(self, user, passwd):
        try:
            cursor = self.getCursor()
            sql = "select * from users where username ='"+user+"'"
            cursor.execute(sql)
            data = cursor.fetchall()
            if (len(data) > 0):  # 至少用户名存在
                encrypt_pwd = data[0][2]
                ret = bcrypt.checkpw(passwd.encode(), encrypt_pwd.encode())
                if ret:
                    return int(data[0][3]) #普通返回0，管理员返回1
                else:
                    return -1  #用户名存在，但密码错误
            else:
                return -1  #用户名都不存在
        except:
            return -1 #服务器s或网络出错
        
if __name__ == '__main__':
    db = DBUtil("gz-cdb-fvxckd3j.sql.tencentcdb.com", 63770, "root",
                    "N3DS7P7fSbJSMCtM", "test", "utf8mb4")
    db.change_password('admin','a')