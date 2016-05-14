#!/usr/bin/python
import sys

current_location = None
morning = 0
afternoon = 0
night = 0

for line in sys.stdin:
    
    location, value = line.strip().split('\t', 1)
    hour, count = value.strip().split(',', 1)

    
    
    try:
        count = int(count)
        hour = int(hour)
    except ValueError:
        continue


    if location == current_location:
        if hour <= 10:
            morning += count
        elif hour > 10 and hour < 17:
            afternoon += count
        elif hour >= 17 and hour <=24:
            night += count
    else:
        if current_location:
        
            print ("%s\t%d,%d,%d" % (current_location, morning, afternoon, night))

        current_location = location
        if hour <= 10:
            morning = count
        elif hour > 10 and hour < 17:
            afternoon = count
        elif hour >= 17 and hour <=24:
            night = count


print ("%s\t%d,%d,%d" % (current_location, morning, afternoon, night))

