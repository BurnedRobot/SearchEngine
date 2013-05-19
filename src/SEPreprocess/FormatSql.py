#! /usr/bin/python
#-*- encoding:utf-8 -*-
"""This module is used to format a sql requery"""

import __init__
import ReadConfig
import ExtractField

def FormatSql(bDisplay = False,bUserInput = False):
    """bDisplay is used to control whether to show sql query or not.
    bUserInput is used to let user to input sql query."""
    if(bUserInput is not False):
        sql = raw_input("Please input your sql query:")
        return sql
    else:
        _field_list = ExtractField.ExtractField()
        _config_dict = ReadConfig.ReadConfig()
        sql = 'select '
        i = 0
        while i < len(_field_list) - 1:
            sql = sql + _field_list[i]['FieldName'] + ','
            i += 1
        sql += _field_list[i]['FieldName']
        sql += " from " + _config_dict['table']
        if(bDisplay is not False):
            print sql
            return sql
        else:
            return sql
        
if "__main__" == __name__ :
    FormatSql(True)
