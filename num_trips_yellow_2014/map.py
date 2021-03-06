#!/usr/bin/python
# key is the medallion, and the value is the number of trips.
import sys
from datetime import datetime

for line in sys.stdin:


    key, value = line.strip().split('\t')
    keys = key.split(',')
    
    if len(keys) == 2 and keys[0] != " pickup_datetime" and keys[0] != "pickup_datetime":
    
        pickup_datetime = keys[0] #if key both pickup and dropoff time
    
        pickup_date = datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    
        print ("%s\t%d" % (pickup_date, 1))
