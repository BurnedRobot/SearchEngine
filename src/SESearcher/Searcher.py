#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import __init__
from lucene import \
    QueryParser, IndexSearcher, StandardAnalyzer, SimpleFSDirectory, File, \
    VERSION, initVM, Version,SmartChineseAnalyzer
#from ReadConfig import ReadConfig
from SEPreprocess.ReadConfig import ReadConfig
from SEUtility.ShowResult import ShowResult

def _run(searcher, analyzer,_config_dict):
    while True:
        print
        print "请输入查询命令"
        command = raw_input("Query:")
        if command == '':
            return

        print
        print "查询:", command
        parser = QueryParser(Version.LUCENE_CURRENT,_config_dict['defaultField'],
                            analyzer)
        parser.setDefaultOperator(QueryParser.AND_OPERATOR)
        query = parser.parse(command)
        scoreDocs = searcher.search(query, int(_config_dict['allSize'])).scoreDocs

        ShowResult(searcher,scoreDocs,bDisplayAll=False,bDisplayTotalNum=False)
        print "%s 条结果." % len(scoreDocs)


def Search(bUserInput=False,command=""):
    _config_dict = ReadConfig()
    STORE_DIR = _config_dict["indexDir"]
    initVM()
    directory = SimpleFSDirectory(File(STORE_DIR))
    searcher = IndexSearcher(directory, True)
    analyzer = SmartChineseAnalyzer(Version.LUCENE_CURRENT)
    if bUserInput is not False:
        _run(searcher, analyzer,_config_dict)
    else:
        parser = QueryParser(Version.LUCENE_CURRENT,_config_dict['defaultField'],
                            analyzer)
        parser.setDefaultOperator(QueryParser.AND_OPERATOR)
        query = parser.parse(command)
        scoreDocs = searcher.search(query,int(_config_dict['allSize'])).scoreDocs
        return len(scoreDocs)
    searcher.close()

if '__main__' == __name__:
    Search(bUserInput=True)
    #Search(command='日本')
