#! /usr/bin/env python
# -*- encoding:utf-8 -*-
"""This module will be used to filte the word from input file with the stopword file.
Usage: python SEFilter.py filename """

import sys
import codecs
import __init__
from SEPreprocess.ReadConfig import ReadConfig
from SEUtility.File_RW import DictPrint,ReadIntoDict

def ImportStopword():
    _dict = ReadConfig()
    _fr = codecs.open(_dict['stopwordsFile'],'r','utf-8')
    word_set = set()
    for word in _fr:
        word_set.add(word.rstrip())
    _fr.close()
    return word_set

def FileFilter(filename):
    _word_set = ImportStopword()
    _dict = ReadIntoDict(filename)
    _dict = StopwordFilter(_dict,_word_set)
    _fw = codecs.open(filename,"w","utf-8")
    DictPrint(_dict,out_file = _fw)
    _fw.close()

def StopwordFilter(_dict,_stopword_set):
    for key in _dict.keys():
        if key in _stopword_set:
            _dict.pop(key)
    return _dict

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if len(sys.argv) < 2:
        print __doc__
        sys.exit(0)
    FileFilter(sys.argv[1])

if __name__ == "__main__":
   main() 
