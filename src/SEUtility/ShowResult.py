#! /usr/bin/env python
# -*- encoding:utf-8 -*-

import __init__
from SEPreprocess.ReadConfig import ReadConfig
from SEPreprocess.ExtractField import ExtractField

def ShowResult(searcher,score_docs,bDisplayAll = True,bDisplayTotalNum = True):
        _dict = ReadConfig()
        _field_list = ExtractField()
        #print _field_list
        if "__main__" == __name__:
            print "Nothing will be done!"
            print "Good Bye!"
            return 
        if bDisplayTotalNum is True:
            print "%s total matching documents." % len(score_docs)
        if not bDisplayAll:
            return 
        for scoreDoc in score_docs:
            doc = searcher.doc(scoreDoc.doc)
            for field in _field_list:
                if field['Display'] is True:
                    print field['FieldName'],":", doc.get(field['FieldName'])
            print
        return len(score_docs)

if __name__ == "__main__":
    ShowResult(None,None)
