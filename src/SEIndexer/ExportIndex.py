#! /usr/bin/env python
#-*- encoding:utf-8 -*-
"""This file will be used to export a special field index.
Usage: python ExportIndex.py field"""
import __init__
from lucene import TermEnum,IndexReader,BytesRef,initVM,SimpleFSDirectory,File
import os,sys,codecs,traceback
from SEPreprocess.ReadConfig import ReadConfig
from SEUtility.File_RW import DictPrint,SetPrint,BinaryListPrint
from SEFilter import ImportStopword,StopwordFilter

def ExportIndex(b_print = False,b_write_file = False,b_filter = True):
    _dict = ReadConfig()
    initVM()
    try:
        if(b_write_file == True):
            output_file = _dict['resultDir'] + '/' + sys.argv[1] + '.xls'
            _fw = open(output_file,'w')
        directory = SimpleFSDirectory(File(_dict['indexDir']))
        ireader = IndexReader.open(directory)
        # Enum all the terms
        all_terms = ireader.terms()
        word_dict = {}
        _stopword_set = ImportStopword()
#        SetPrint(_stopword_set)
        while all_terms.next():
            term_elem = all_terms.term()
            if term_elem.field() == sys.argv[1]:
                _temp = term_elem.text().rstrip()
                word_dict[_temp] = all_terms.docFreq()
        if(b_filter == True):
            StopwordFilter(word_dict,_stopword_set)
        if(b_print != False):
            DictPrint(word_dict)
        if(b_write_file != False):
            DictPrint(word_dict,out_file=_fw)
            _fw.close()
        all_terms.close()
        return word_dict
    except Exception,e:
        print "Failed: ",e
        traceback.print_exc(file=sys.stdout)

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if len(sys.argv) < 2:
        print __doc__
        sys.exit(0)
    ExportIndex(b_write_file = True,b_filter = False)

if __name__ == "__main__":
    main()
