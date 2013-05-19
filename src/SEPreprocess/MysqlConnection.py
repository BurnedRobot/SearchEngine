#! /usr/bin/env python 
#-*- encoding:utf-8 -*-

import __init__
from MySQLdb import connect
import getpass
import ReadConfig

class Db_Access_Info:
    host = ''
    user = ''
    passwd = ''
    db = ''
    def __init__(self):
        _dict = ReadConfig.ReadConfig()
        self.host = _dict['host']
        self.user = _dict['user']
        self.passwd = _dict['passwd']
        self.db = _dict['db']

    def input(self):
        print "Please input the info to access database"
        self.host = raw_input("Host Name:\t")
        self.user = raw_input("User:\t\t")
        self.passwd = getpass.getpass("PassWord:\t")
        self.db = raw_input("Database:\t")

Globle_Db = Db_Access_Info()
#Globle_Db.input()
class MysqlConnection(object):
    __db__ = None
    __cursor__ = None

    def __init__(self):
        self.__db__ = connect(host=Globle_Db.host,user=Globle_Db.user,passwd=Globle_Db.passwd,
                            db=Globle_Db.db,charset='utf8')
        self.__cursor__ = self.__db__.cursor()

    def close(self):
        self.__cursor__.close()
        self.__cursor__ = None
        self.__db__ = None
        
    def get_cursor(self):
        assert self.__cursor__ != None
        return self.__cursor__
        
    def execute(self,query_cmd):
        assert self.__cursor__ != None
        self.__cursor__.execute(query_cmd)


if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    conn = MysqlConnection()
    mysql_cursor = conn.get_cursor()
    mysql_cursor.execute("""select count(id) from table1 where sex='男'""")
    print mysql_cursor.fetchone()
    mysql_cursor.execute("""select id,summary from table1 where sex='男'""")
    print mysql_cursor.fetchone()
