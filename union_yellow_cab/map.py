#!/usr/bin/python
import sys
 
for line in sys.stdin:
    
    line = line.strip().split(',')
    
    #print('%s' % (line))
    
    
    if len(line) == 18:
        vendor_id = line[0] if len(line) > 0 else ''
        pickup_datetime = line[1] if len(line) > 1 else ''
        dropoff_datetime = line[2] if len(line) > 2 else ''
        passenger_count = line[3] if len(line) > 3 else ''
        trip_distance = line[4] if len(line) > 4 else ''
        pickup_longitude = line[5] if len(line) > 5 else ''
        pickup_latitude = line[6] if len(line) > 6 else ''
        rate_code = line[7] if len(line) > 7 else ''
        store_and_fwd_flag = line[8] if len(line) > 8 else ''
        dropoff_longitude = line[9] if len(line) > 9 else ''
        dropoff_latitude = line[10] if len(line) > 10 else ''
        payment_type = line[11] if len(line) > 11 else ''
        fare_amount = line[12] if len(line) > 12 else ''
        extra = line[13] if len(line) > 13 else ''
        mta_tax = line[14] if len(line) > 14 else ''
        #surcharge = line[15] if len(line) > 15 else ''
        tip_amount = line[15] if len(line) > 15 else ''
        tolls_amount = line[16] if len(line) > 16 else ''
        total_amount = line[17] if len(line) > 17 else ''
        
        print ('%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (pickup_datetime, dropoff_datetime, vendor_id, passenger_count, trip_distance, pickup_longitude, pickup_latitude, rate_code, store_and_fwd_flag, dropoff_longitude, dropoff_latitude, payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,total_amount))
        
    elif len(line) == 19:
        vendor_id = line[0] if len(line) > 0 else ''
        pickup_datetime = line[1] if len(line) > 1 else ''
        dropoff_datetime = line[2] if len(line) > 2 else ''
        passenger_count = line[3] if len(line) > 3 else ''
        trip_distance = line[4] if len(line) > 4 else ''
        pickup_longitude = line[5] if len(line) > 5 else ''
        pickup_latitude = line[6] if len(line) > 6 else ''
        rate_code = line[7] if len(line) > 7 else ''
        store_and_fwd_flag = line[8] if len(line) > 8 else ''
        dropoff_longitude = line[9] if len(line) > 9 else ''
        dropoff_latitude = line[10] if len(line) > 10 else ''
        payment_type = line[11] if len(line) > 11 else ''
        fare_amount = line[12] if len(line) > 12 else ''
        extra = line[13] if len(line) > 13 else ''
        mta_tax = line[14] if len(line) > 14 else ''
        surcharge = line[15] if len(line) > 15 else ''
        tip_amount = line[16] if len(line) > 16 else ''
        tolls_amount = line[17] if len(line) > 17 else ''
        total_amount = line[18] if len(line) > 18 else ''
        
        if pickup_datetime != "tpep_pickup_datetime":
            print ('%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (pickup_datetime, dropoff_datetime, vendor_id, passenger_count, trip_distance, pickup_longitude, pickup_latitude, rate_code, store_and_fwd_flag, dropoff_longitude, dropoff_latitude, payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,total_amount))


