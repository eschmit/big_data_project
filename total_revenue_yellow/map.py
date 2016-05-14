#!/usr/bin/python
import sys
from datetime import datetime

for line in sys.stdin:

    key, value = line.strip().split('\t')
    keys = key.split(',')
    
    if len(keys) == 2 and keys[0] != " pickup_datetime" and keys[0] != "pickup_datetime":
        
        pickup_datetime = keys[0] #if key both pickup and dropoff time
        
        pickup_date = datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')


        values = value.split(',')
    
        if len(values) == 16: # may need to check values[0] !=

            fare_amount = values[10]
            extra = values[11]
            tip_amount = values[13]

    
            print ("%s\t%s,%s,%s" % (pickup_date, fare_amount, extra, tip_amount))