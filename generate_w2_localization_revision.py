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

    try:
        # Get the column positions from the header line
        row = reader.next()
        pos_key = row.index('Key')
        pos_eng = row.index('English')
        pos_ita = row.index('it')
    except ValueError:
        print('Key or Translation column not found')
    else:
        # Iterate trough all rows
        for row in reader:
            # Print key and translation lines
            print('#' + row[pos_key])
            print('~' + row[pos_eng])
            print('=' + row[pos_ita])
