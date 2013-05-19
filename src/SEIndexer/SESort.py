#! /usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
import operator
import __init__
from SEUtility.File_RW import DictPrint,ReadIntoDict


#sort a file.
def SortContent(filename):
#    _fr = open(filename,'r')
#    _dict = {}
#    for line in _fr:
#        line = line.rstrip()
#        _temp = line.split()
#        _dict[_temp[0]] =int(_temp[1])
    #DictPrint(_dict)
    _dict = ReadIntoDict(filename)
    sort_list = sorted(_dict.iteritems(),key=operator.itemgetter(1),reverse=True)
    _fw = open(filename,'w')
    for elem in sort_list:
        _fw.write(elem[0]+"\t"+str(elem[1])+"\n")
    _fw.close()

#sort a dict
def SortDict(_dict):
    sort_list = sorted(_dict.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sort_list

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if len(sys.argv) < 2:
        print "Usage: python sort_export_index.py filename"
        sys.exit(0)
    SortContent(sys.argv[1])

if __name__ == "__main__":
    main()
