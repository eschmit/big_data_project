#!/usr/bin/python
import sys
from datetime import datetime
 
for line in sys.stdin:
    
    line = line.strip().split(',')
    
    #print('%s' % (line))
    
    
    if len(line) == 15 and line[0] != '"tripduration"':
        tripduration = line[0].strip('"') if len(line) > 0 else ''
        starttime = line[1].strip('"') if len(line) > 1 else ''
        stoptime = line[2].strip('"') if len(line) > 2 else ''
        start_station_id = line[3].strip('"') if len(line) > 3 else ''
        start_station_name = line[4].strip('"') if len(line) > 4 else ''
        start_station_lat = line[5].strip('"') if len(line) > 5 else ''
        start_station_lon = line[6].strip('"') if len(line) > 6 else ''
        end_station_id = line[7].strip('"') if len(line) > 7 else ''
        end_station_name = line[8].strip('"') if len(line) > 8 else ''
        end_station_lat = line[9].strip('"') if len(line) > 9 else ''
        end_station_lon = line[10].strip('"') if len(line) > 10 else ''
        bike_id = line[11].strip('"') if len(line) > 11 else ''
        usertype = line[12].strip('"') if len(line) > 12 else ''
        birth_year = line[13].strip('"') if len(line) > 13 else ''
        gender = line[14].strip('"') if len(line) > 14 else ''
        
        starttime = datetime.strptime(starttime, '%m/%d/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        stoptime = datetime.strptime(stoptime, '%m/%d/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        
        print ('%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (starttime, stoptime, tripduration, start_station_id, start_station_name, start_station_lat, start_station_lon, end_station_id, end_station_name, end_station_lat, end_station_lon, bike_id,usertype,birth_year,gender))
        
