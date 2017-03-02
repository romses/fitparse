#!/usr/bin/env python3

from fitparse import FitFile


#fitfile = FitFile('/home/kreitz/dev/garmin/data/727G2555.FIT')
#fitfile = FitFile('/home/kreitz/dev/garmin/data-rene/72HE3642.FIT')
#fitfile = FitFile('/home/kreitz/dev/garmin/data-rene/72BC0937.FIT')
#fitfile = FitFile('/home/kreitz/dev/garmin/data/DEVICE.FIT')
fitfile = FitFile('/home/kreitz/dev/garmin/data/Monitor/LCTNS.FIT')
#fitfile = FitFile('/home/kreitz/dev/garmin/data/722G5750.FIT')

#num_subfiles = fitfile.get_fit_subfiles()

#fitfile.parse()

# Get all data messages that are of type record
#or i in range(num_subfiles):
#    fitfile.select_fit_subfile(i)
#    fitfile.parse()

#for record in fitfile.get_messages(["device_info","sport","record","length","hr"]):
for record in fitfile.get_messages():

#    val = record.get_values()
    print(record.name)
   
    for record_data in record:
        if record_data.units:
            print (" * %s: %s %s" % (
                record_data.name, record_data.value, record_data.units,
            ))
        else:
            print (" * %s: %s" % (record_data.name, record_data.value))
    print
