#!/usr/bin/python
import sys
from datetime import datetime
 
for line in sys.stdin:
    
    line = line.strip().split(',')
    
    
    if len(line) == 4 and line[0] != "Dispatching_base_num":
        d_base_num = line[0] if len(line) > 0 else ''
        pickup_datetime = line[1] if len(line) > 1 else ''
        a_base_num = line[2] if len(line) > 2 else ''
        location_id = line[3] if len(line) > 3 else ''
    
        month = datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S').strftime('%m')
        
        try:
            month = int(month)
        except ValueError:
            continue
    
    
        if month == 4 or month == 5:
            print ("%s\t%s,%s,%s" % (pickup_datetime, d_base_num,a_base_num, location_id))
        
