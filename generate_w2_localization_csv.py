#!/usr/bin/python2
#
# Generate localization file for Wasteland 2 from a csv source
#
# 2014, Edmondo Tommasina

import sys
import string
import csv

# Open csv file
with open(str(sys.argv[1]), 'rb') as f:
    reader = csv.reader(f)

    # Iterate trough all rows
    rownum = -1
    for row in reader:
        rownum += 1
        if rownum == 0:
            pos_key = row.index('Key')
            pos_tra = row.index('it')

            if pos_key == -1:
                print('Key column not found')
                break

            if pos_tra == -1:
                print('Translation column not found')
                break

            continue


        # Print key and translation lines
        print('#' + row[pos_key])
        print('=' + row[pos_tra])


