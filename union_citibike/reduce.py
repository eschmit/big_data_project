#!/usr/bin/python
import sys


for line in sys.stdin:

    key, value = line.strip().split('\t',1)
    
    print("%s\t%s" % (key,value))
    


