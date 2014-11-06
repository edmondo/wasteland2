#!/usr/bin/python2
#
# Extract the italian localization for Wasteland 2
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
        pos_tra = row.index('it')
    except ValueError:
        print('Translation column not found')
    else:
        # Iterate trough all rows
        for row in reader:
            # Print key and translation lines
            print(row[pos_tra])
