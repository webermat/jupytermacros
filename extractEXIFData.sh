#!/bin/bash

for i in {2006..2019}
do
    echo "extract info from folder $i"
    exiftool -DateTimeOriginal -d "%b %d %a ,%Y, %H:%M:%S" -TimeZone -TimeZoneCity -DaylightSavings -FocalLength -ExposureTime -Model -ISO -s -csv -r /Volumes/INTENSO/Backups.backupdb/Matthias’s\ MacBook\ Pro/Latest/Macintosh\ HD/Users/matthiasweber/Pictures/$i > outputEXIFcsvs/PhotoEXIFDataDayType_$i.csv
done