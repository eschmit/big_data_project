#!/usr/bin/python
import sys

current_pickup_date = None
current_fare_amount = 0.0
#current_tolls_amount = 0.0
#date_count = 0
total_fare_amount = 0.0

for line in sys.stdin:
    
    pickup_date, revenue = line.strip().split('\t', 1)
    fare_amount, extra, tip_amount = revenue.strip().split(',', 2)
    
    try:
        fare_amount = float(fare_amount)
        extra = float(extra)
        tip_amount = float(tip_amount)
    #tolls_amount = float(tolls_amount)
    except ValueError:
        continue
    
    if pickup_date == current_pickup_date:
        current_fare_amount += fare_amount + extra + tip_amount
#current_tolls_amount += tolls_amount
    else:
        if current_pickup_date:
            print ("%s\t%.2f" % (current_pickup_date, current_fare_amount))
            total_fare_amount += current_fare_amount

        current_pickup_date = pickup_date
        current_fare_amount = fare_amount + extra + tip_amount
#date_count += 1

#current_tolls_amount = tolls_amount

print ("%s\t%.2f" % (current_pickup_date, current_fare_amount))
total_fare_amount += current_fare_amount

print("Total Fares: %.2f" %(total_fare_amount))