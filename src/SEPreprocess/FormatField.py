#!/usr/bin/python
#-*- encoding:utf-8 -*-

from __future__ import print_function
import __init__,codecs
from ReadConfig import ReadConfig
from MysqlConnection import MysqlConnection


def FormatField():
    _config_dict = ReadConfig()
    conn = MysqlConnection()
    sql = "describe" + " " + _config_dict['table']
    conn.execute(sql)
    cursor = conn.get_cursor()
    _field_list = _OrganizeField(cursor)
    _WriteField(_field_list)

def _OrganizeField(cursor):
    _field_list = []
    temp = cursor.fetchone()
    while(temp is not None):
        _Process_Fieldlist(temp,_field_list)
        temp = cursor.fetchone()
    print(_field_list)
    return _field_list

def _Process_Fieldlist(cursor_fetch,field_list):
    elem = []
    field_name = str(cursor_fetch[0])
    if("id" == field_name):
        elem.append(field_name)
        elem.append("1")
        elem.append("0")
    else:
        elem.append(field_name)
        if( -1 != str.find(str(cursor_fetch[1]),"int(") ):
            elem.append("0")
            elem.append("1")
        elif( -1 != str.find(str(cursor_fetch[1]),"char(") ):
            elem.append("1")
            elem.append("0")
        else:
            print("Something wrong occurred in _Process_Fieldlist !")
            return 
    elem.append("1")
    print(elem)
    field_list.append(elem)

def _WriteField(field_list):
    _config_dict = ReadConfig()
    _fw = codecs.open(_config_dict['fieldFile'],'w','utf-8')
    print("FieldName\t\tStringField\t\tNumericField\t\tDisplay")
    print("FieldName\t\tStringField\t\tNumericField\t\tDisplay",file=_fw)
    for elem in field_list:
        strtemp = "{0}\t\t{1}\t\t{2}\t\t{3}".format(elem[0],elem[1],elem[2],elem[3])
        print(strtemp)
        print(strtemp,file=_fw)
    _fw.close()

if "__main__" == __name__:
    FormatField()
