#! /usr/bin/env python
# -*- encoding:utf-8 -*-
"""Usage: python ListSearcher [field] [file_name]"""
from __future__ import print_function
import __init__
import os.path,sys
from SEPreprocess.ReadConfig import ReadConfig
from SEUtility.ShowResult import ShowResult
from Searcher import Search
from SEUtility.File_RW import ReadFile

def ListSearcher(field,file_name):
    _dict = ReadConfig()
    if(os.path.isdir(_dict["resultDir"]) is False):
        os.makedirs(_dict["resultDir"])
    #print (_dict["resultDir"]+field+".xls")
    _fw = open(_dict["resultDir"]+"/"+field+".xls","w")
    _content_list = ReadFile(file_name)
    for word in _content_list:
        cmd = field + ":" +word
        totalNum = Search(command = cmd)
        print(word,"\t",totalNum)
        print(word,"\t",totalNum,file = _fw)
    _fw.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(0)
    ListSearcher(sys.argv[1],sys.argv[2])
