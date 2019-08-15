#!/bin/bash

for i in {2006..2019}
do
    echo "extract info from folder $i"
    exiftool -DateTimeOriginal -d "%b %d %a ,%Y, %H:%M:%S" -TimeZone -TimeZoneCity -DaylightSavings -FocalLength -ExposureTime -Model -ISO -Aperture -MeasuredEV -MeasuredRGGB -WB_RGGBLevelsAsShot -ColorTemperature -ColorTemperatureAsShot -ColorTempDaylight -LightValue -s -\
csv -r ~/Pictures/$i > outputEXIFcsvs/PhotoEXIFDataDayType_$i.csv     
done