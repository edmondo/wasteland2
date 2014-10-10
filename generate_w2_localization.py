#!/usr/bin/python
#
# Generate localization file for Wasteland 2
#
# 2014, Edmondo Tommasina

import sys
import string
import xlrd

# Read arguments
xlsx_file = str(sys.argv[1])

# Open xlsx workbook and select the main sheet
workbook = xlrd.open_workbook(xlsx_file)
worksheet = workbook.sheet_by_name('Main')

# Iterate trough all rows and print the key and translate cells
# in unicode format.
num_rows = worksheet.nrows - 1
curr_row = -1

while curr_row < num_rows:
    curr_row += 1

    if curr_row == 0:
        continue

    # FIXME: column position hardcoded. Make it by name.
    print('#' + worksheet.cell_value(curr_row,  6).encode('utf8'))
    print('=' + worksheet.cell_value(curr_row, 12).encode('utf8'))
