#!/usr/bin/python
import sys
from datetime import datetime

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Polygon:
    def __init__(self,points):
        self.points = points
        self.nvert = len(points)
                
        minx = maxx = points[0].x
        miny = maxy = points[0].y
        for i in xrange(1,self.nvert):
            minx = min(minx,points[i].x)
            miny = min(miny,points[i].y)
            maxx = max(maxx,points[i].x)
            maxy = max(maxy,points[i].y)
        
        self.bound = (minx,miny,maxx,maxy)
    
    
    def contains(self,pt):
        firstX = self.points[0].x
        firstY = self.points[0].y
        testx = pt.x
        testy = pt.y
        c = False
        j = 0
        i = 1
        nvert = self.nvert
        while (i < nvert) :
            vi = self.points[i]
            vj = self.points[j]
                        
            if(((vi.y > testy) != (vj.y > testy)) and (testx < (vj.x - vi.x) * (testy - vi.y) / (vj.y - vi.y) + vi.x)):
                c = not(c)
                        
            if(vi.x == firstX and vi.y == firstY):
                i = i + 1
                if (i < nvert):
                    vi = self.points[i];
                    firstX = vi.x;
                    firstY = vi.y;
            j = i
            i = i + 1
        return c

    def bounds(self):
            return self.bound



for line in sys.stdin:

    key, value = line.strip().split('\t')
    
    pickup_datetime = key.split(',')[0] #if key both pickup and dropoff time
    
    #pickup_date = datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    
    hour = datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S').strftime('%H')
    
    
    values = value.strip().split(',')

        
    try:
        hour = int(hour)
        lat = float(values[3])
        lon = float(values[4])
    except ValueError:
        continue


        #may want day of week and hour of day
        #group hours into time of day

    
        #create polygons for nyc
#lower east

#lower west
    financial_d = Polygon([Point(40.70520501, -74.01918411),Point(40.70042248, -74.01261806),Point(40.70984524, -73.99203821),Point(40.72568289, -74.01093656)])

    lower_east = Polygon([Point(40.74981801, -73.98778764),Point(40.74325041, 73.97212353),Point(40.71797449, -73.9998644),Point(40.70984524, -73.99203821)])

    lower_west = Polygon([Point(40.74981801, -73.98778764),Point(40.75696271, -74.00479967),Point(40.71797449, -73.9998644),Point(40.72568289, -74.01093656)])

    midtown_east = Polygon([Point(40.74981801, -73.98778764),Point(40.74326667, -73.97235957),Point(40.76563285, -73.97626487),Point(40.75838418, -73.95905581 )])

    midtown_west = Polygon([Point(40.74981801, -73.98778764),Point(40.75696271, -74.00501425),Point(40.76563285, -73.97626487),Point(40.77271824, -73.99325934 )])

    upper_east = Polygon([Point(40.76844435, 73.98158637),Point(40.75870924, 73.95890561),Point(40.80017511, -73.95839063),Point(40.79133816, -73.93611756)]) #60th - 96

    upper_west = Polygon([Point(40.76844435, -73.98158637),Point(40.77275074, -73.9931306),Point(40.80017511, -73.95839063),Point(40.80584378, -73.97075025)]) #59 - 110


        #check which poly contains point
        
    pt = Point(lat, lon)

    if financial_d.contains(pt):
        print ("%s\t%d,%d" % ("financial",hour, 1))
    elif lower_east.contains(pt):
        print ("%s\t%d,%d" % ("lower_east",hour, 1))
    elif lower_west.contains(pt):
        print ("%s\t%d,%d" % ("lower_west",hour, 1))

    elif midtown_east.contains(pt):
        print ("%s\t%d,%d" % ("midtown_east",hour, 1))

    elif midtown_west.contains(pt):
        print ("%s\t%d,%d" % ("midtown_west",hour, 1))
    elif upper_east.contains(pt):
        print ("%s\t%d,%d" % ("upper_east",hour, 1))

    elif upper_west.contains(pt):
        print ("%s\t%d,%d" % ("upper_west",hour, 1))

#print ("%s\t%s,%s,%s" % (pickup_date, lat, long))




