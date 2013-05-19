#! /usr/bin/python
# -*- encoding:utf-8 -*-

import __init__
import os,sys
import lucene
import traceback
from lucene import \
    QueryParser, IndexSearcher, StandardAnalyzer, SimpleFSDirectory, File, \
    VERSION, initVM, Version,SmartChineseAnalyzer,Document,IndexWriter,Field,NumericField
from SEUtility.Ticker import Ticker
from SEPreprocess.ReadConfig import ReadConfig
from SEPreprocess.ExtractField import ExtractField
from SEPreprocess.FormatSql import FormatSql
from SEPreprocess.MysqlConnection import MysqlConnection

def _InitIndexer():
    initVM()
    config_dict = ReadConfig()
    field_list = ExtractField()
    sql = FormatSql(bUserInput = False)
    conn = MysqlConnection()
    conn.execute(sql)
    return field_list,conn,config_dict


def _IndexStringField(doc,field_name,field_content):
    #print "This is StringField:",field_content
    if field_content is None:
        return
    else:
        if("id" == field_name):
            doc.add(Field(field_name,str(field_content),Field.Store.YES,Field.Index.NOT_ANALYZED))
        else:
            doc.add(Field(field_name,str(field_content),Field.Store.YES,Field.Index.ANALYZED))


def _IndexNumericField(doc,field_name,field_content):
    #print "This is NumericField:",field_content
    if field_content is None:
        return
    else:
        doc.add(NumericField(field_name,Field.Store.YES,True).setIntValue(int(field_content)))


def _IndexField(field_list,content):
    i = 0
    doc = Document()
    while i < len(field_list):
        if(field_list[i]['StringField'] is not False):
            _IndexStringField(doc,field_list[i]['FieldName'],content[i])
        elif(field_list[i]['NumericField'] is not False):
            _IndexNumericField(doc,field_list[i]['FieldName'],content[i])
        i += 1
    return doc


def _IndexDocs(writer,field_list,connection):
    cursor = connection.get_cursor()
    content = cursor.fetchone()
    while(content is not None):
        doc = _IndexField(field_list,content)
        writer.addDocument(doc)
        #print content
        content = cursor.fetchone()
    writer.optimize()
    writer.close()


def Index():
    field_list,conn,_config_dict = _InitIndexer()

    indexDir = _config_dict['indexDir']
    if not os.path.exists(indexDir):
        os.mkdir(indexDir)
    store = SimpleFSDirectory(lucene.File(indexDir))
    #print store
    writer = IndexWriter(store, SmartChineseAnalyzer(lucene.Version.LUCENE_CURRENT), True,
                               IndexWriter.MaxFieldLength.LIMITED)
    writer.setMaxFieldLength(1048576)
    try:
        ticker = Ticker()
        ticker.start()
        _IndexDocs(writer,field_list,conn)
        ticker.end()
        ticker.TimeCost()
    except Exception,e:
        print "Failed in Indexing...",e
        traceback.print_exc()
    

def main():
    reload(sys)
    sys.setdefaultencoding("utf-8")
    Index()
    
    
if "__main__" == __name__ :
    main()
