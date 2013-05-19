#! /usr/bin/python
#-*- encoding:utf-8 -*- 

"""Usage:"""
import __init__
import os.path
import xml.etree.ElementTree as ET
from SEUtility import File_RW

SE_CONFIG_PATH = '../../config/config.xml'

def ReadConfig(bDisplay = False):
    """This function will extract information from config.xml and write them into a dict"""
    tree = ET.parse(SE_CONFIG_PATH)
    root = tree.getroot()
    _config_dict = {}
    for child in root:
#        print child.tag,child.text
        if("fieldFile" == child.tag or "stopwordsFile" == child.tag):
            temp = os.path.realpath(SE_CONFIG_PATH)
            child.text = os.path.normpath(os.path.join(os.path.dirname(temp),child.text))
        else:
            pass
        _config_dict[child.tag] = child.text
    if(bDisplay is not True):
        return _config_dict
    else:
        File_RW.DictPrint(_config_dict)
        return _config_dict

if "__main__" == __name__:
    ReadConfig(True)
