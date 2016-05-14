#!/usr/bin/python
#import sys
import __future__, sys

#current_medallion = None
current_pickup_date = None
date_count = 0

current_trip_count = 0
total_trips_count = 0.0

for line in sys.stdin:
    
    pickup_date, count = line.strip().split('\t', 1)
    #medallion, pickup_date = key.strip().split(',', 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if pickup_date == current_pickup_date:
        current_trip_count += count
        
#total_trips_count += 1
    
    else:
        if current_pickup_date:
            print ("%s\t%d" % (current_pickup_date, current_trip_count))
            total_trips_count += current_trip_count
        
        current_pickup_date = pickup_date
        current_trip_count = count
        date_count += count

print ("%s\t%d" % (current_pickup_date, current_trip_count))
total_trips_count += current_trip_count


print ("Total Trips, Average Trips per Day %.2f, %.2f" % (total_trips_count, total_trips_count/date_count))

#total number of trips
#average number of trips per day



