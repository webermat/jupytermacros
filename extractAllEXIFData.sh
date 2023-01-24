#!/bin/bash

for i in {2023..2023}
do
    echo "extract info from folder $i"
    exiftool -csv -r /Volumes/Backup\ Plus/Pictures/$i > outputEXIFcsvsFullInfo/PhotoEXIFDataFull_$i.csv     
done
