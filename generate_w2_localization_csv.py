#!/usr/bin/python2
#
# Generate localization file for Wasteland 2 from a csv source
#
# 2014, Edmondo Tommasin

import sys
import string
import csv

# Find column by name
def find_column_my_name(row, name):

    cur_col = 0

    while cur_col < len(row):
        if row[cur_col] == name:
            return cur_col
        cur_col += 1

    return -1


# Open csv file
with open(str(sys.argv[1]), 'rb') as f:
    reader = csv.reader(f)

    # Iterate trough all rows
    rownum = -1
    for row in reader:
        rownum += 1
        if rownum == 0:
            pos_key = find_column_my_name(row, 'Key')
            pos_tra = find_column_my_name(row, 'it')

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


