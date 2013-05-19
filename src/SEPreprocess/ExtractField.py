#! /usr/bin/python
#-*- encoding:utf-8 -*-

"""This module is used to extract fields information from field_config.txt.
Usage: python ExtractField.py"""
import __init__
import inspect
import ReadConfig
from SEUtility import File_RW 

def ExtractField():
    """This function will read fields information"""
    _config_dict = ReadConfig.ReadConfig()
    _fr = None
    _field_list = []
    with open(_config_dict['fieldFile'],'r') as _fr:
        _field_descriptor = _fr.readline().split()      #read the first line of the field_config.txt
        #print _field_descriptor

        for line in _fr:
            _field_content = line.split()               #read each field and its infomation

            #fill every field into a list
            i = 0
            _field_dict = {}
            while(i < len(_field_content)):
                # replace str "1" with True and "0" with False
                if("1" == _field_content[i]):
                    _field_content[i] = True
                elif("0" == _field_content[i]):
                    _field_content[i] = False
                else:
                    #print "Error!",__file__,inspect.currentframe().f_back.f_lineno
                    pass
                _field_dict[_field_descriptor[i]] = _field_content[i]
                i += 1

            _field_list.append(_field_dict)

    #print _field_list
    return _field_list


if "__main__" == __name__:
    ExtractField()
