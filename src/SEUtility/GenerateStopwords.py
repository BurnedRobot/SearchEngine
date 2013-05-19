#! /usr/bin/env python
# -*- encoding:utf-8 -*-

import sys

def GenerateStopwords(input_file,output_file):
    _fr = open(input_file,'r')
    _fw = open(output_file,'w')
    for line in _fr:
        temp = line.split()
        _fw.write(temp[0].rstrip()+"\n")
    _fr.close()
    _fw.close()

def main():
    if len(sys.argv) < 3:
        print "Usage: python GenerateStopwords.py inputfile outputfile"
        sys.exit(0)
    GenerateStopwords(sys.argv[1],sys.argv[2])
    
if __name__ == "__main__":
    main()

