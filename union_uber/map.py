#!/usr/bin/python
import sys
 
for line in sys.stdin:
    
    line = line.strip().split(',')
    
    #print('%s' % (line))
    
    
    if len(line) == 4: #uber
        pickup_datetime = line[0] if len(line) > 0 else '' #strip('"')
        pickup_lat = line[1] if len(line) > 1 else ''
        pickup_lon = line[2] if len(line) > 2 else ''
        base = line[3] if len(line) > 3 else ''

               
        print ('%s\t%s,%s,%s' % (pickup_datetime, pickup_lat, pickup_lon, base))
        
