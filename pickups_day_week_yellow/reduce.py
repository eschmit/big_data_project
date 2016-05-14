#!/usr/bin/python
import sys

current_location = None
monday = 0
tuesday = 0
wednesday = 0
thursday = 0
friday = 0
saturday = 0
sunday = 0

for line in sys.stdin:
    
    location, value = line.strip().split('\t', 1)
    month, day, count = value.strip().split(',', 2)

    
    try:
        count = int(count)
        month = int(month)
        day = int(day)
    except ValueError:
        continue


    if location == current_location:
        if month == 4:
            remainder = day % 7
            if remainder == 0:
                monday += count
            elif remainder == 1:
                tuesday += count
            elif remainder == 2:
                wednesday += count
            elif remainder == 3:
                thursday += count
            elif remainder == 4:
                friday += count
            elif remainder == 5:
                saturday += count
            elif remainder == 6:
                sunday += count
        elif month == 5:
            remainder = day % 7
            if remainder == 0:
                wednesday += count
            elif remainder == 1:
                thursday += count
            elif remainder == 2:
                friday += count
            elif remainder == 3:
                saturday += count
            elif remainder == 4:
                sunday += count
            elif remainder == 5:
                monday += count
            elif remainder == 6:
                tuesday += count

    else:
        if current_location:
        
            print ("%s\t%s,%d,%s,%d,%s,%d,%s,%d,%s,%d,%s,%d,%s,%d" % (current_location, "Monday",
                monday,"Tuesday", tuesday, "Wednesday", wednesday, "Thursday", thursday, "Friday",
                friday, "Saturday", saturday, "Sunday", sunday))

        current_location = location
        if month == 4:
            remainder = day % 7
            if remainder == 0:
                monday = count
            elif remainder == 1:
                tuesday = count
            elif remainder == 2:
                wednesday = count
            elif remainder == 3:
                thursday = count
            elif remainder == 4:
                friday = count
            elif remainder == 5:
                saturday = count
            elif remainder == 6:
                sunday = count
        elif month == 5:
            remainder = day % 7
            if remainder == 0:
                wednesday = count
            elif remainder == 1:
                thursday = count
            elif remainder == 2:
                friday = count
            elif remainder == 3:
                saturday = count
            elif remainder == 4:
                sunday = count
            elif remainder == 5:
                monday = count
            elif remainder == 6:
                tuesday = count


print ("%s\t%s,%d,%s,%d,%s,%d,%s,%d,%s,%d,%s,%d,%s,%d" % (current_location, "Monday",
      monday,"Tuesday", tuesday, "Wednesday", wednesday, "Thursday", thursday, "Friday",
      friday, "Saturday", saturday, "Sunday", sunday))
