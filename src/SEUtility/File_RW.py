#! /usr/bin/env python 
# -*-encoding:utf-8 -*-

from __future__ import print_function
from sys import stdout
import codecs
import sys

def DictPrint(input_dict,out_file=stdout):
    """print the dict content as the format [(key)\t\t(value)]"""
    for key,value in input_dict.items():
        print("{0}\t\t{1}".format(key,value),file=out_file)

def SetPrint(input_set,out_file=stdout):
    for elem in input_set:
        print(elem,file=out_file)

def BinaryListPrint(input_list,out_file=stdout):
    for elem in input_list:
        print(elem[0],'\t',elem[1],file=out_file)

#def list_print(input_list,out_files=stdout):
#    for _each_list in input_list:
#        for elem in _each_list:
#            print(elem,sep='\t',file=out_file)
#        print()

def ReadFile(filename):
    _content = set()
    _fr = open(filename,"r")
    for line in _fr:
        _content.add((line.rstrip()))
    _fr.close()
    #print _content
    return _content

def ReadIntoDict(filename):
    _dict = {}
    _fr = codecs.open(filename,"r","utf-8")
    for line in _fr:
        temp = line.split()
        if(2 != len(temp)):
            continue
        _dict[temp[0].rstrip()] = int(temp[1])
    _fr.close()
    return _dict

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding("utf-8")
    if len(sys.argv) < 2:
        print("Usage: python File_RW.py filename")
        sys.exit(0)
    print(ReadFile(sys.argv[1]))
