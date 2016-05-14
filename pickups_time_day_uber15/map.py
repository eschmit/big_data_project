#!/usr/bin/python
import sys
from datetime import datetime


for line in sys.stdin:

    key, value = line.strip().split('\t')
    
    pickup_datetime = key #if key both pickup and dropoff time
    
    hour = datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S').strftime('%H')
    
    
    location_id = value.split(',')[2]

        
    try:
        hour = int(hour)
        location_id = int(location_id)

    except ValueError:
        continue


        #may want day of week and hour of day
        #group hours into time of day

    
        #create polygons for nyc
#lower east

#lower west


    financial = [87,88, 12,13, 209, 261]

    lower_east = [90, 4, 79, 107, 137, 144, 148, 224, 234]

    lower_west = [68, 113, 114, 125, 158, 211, 231, 249]

    midtown_west = [100,48,50, 163, 186, 230]

    midtown_east = [162, 170, 229, 233]

    upper_west = [24, 142, 143, 151, 238, 239]

    upper_east = [74, 75, 140, 141, 236, 237, 262, 263]

    if location_id in financial:
        print ("%s\t%d,%d" % ("financial",hour, 1))
    elif location_id in lower_east:
        print ("%s\t%d,%d" % ("lower_east",hour, 1))
    elif location_id in lower_west:
        print ("%s\t%d,%d" % ("lower_west",hour, 1))

    elif location_id in midtown_east:
        print ("%s\t%d,%d" % ("midtown_east",hour, 1))

    elif location_id in midtown_west:
        print ("%s\t%d,%d" % ("midtown_west",hour, 1))
    elif location_id in upper_east:
        print ("%s\t%d,%d" % ("upper_east",hour, 1))

    elif location_id in upper_west:
        print ("%s\t%d,%d" % ("upper_west",hour, 1))

#print ("%s\t%s,%s,%s" % (pickup_date, lat, long))




