#!/usr/bin/python
#
# Generate localization file for Wasteland 2
#
# 2014, Edmondo Tommasina

import sys
import string
import xlrd

# Find column by name
def find_column_my_name(sheet, name, ncols):

    cur_col = 0

    while cur_col < ncols:
        if sheet.cell_value(0, cur_col) == name:
             return cur_col
        cur_col += 1

    return -1

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

    # Find column postion for key and translation
    if curr_row == 0:
        pos_key = find_column_my_name(worksheet, 'Key', worksheet.ncols)
        pos_tra = find_column_my_name(worksheet, 'it', worksheet.ncols)

        if pos_key == -1:
             print('Key column not found')
             break

        if pos_tra == -1:
             print('Translation column not found')
             break

        continue

    # Print key and translation lines
    print('#' + worksheet.cell_value(curr_row, pos_key).encode('utf8'))
    print('=' + worksheet.cell_value(curr_row, pos_tra).encode('utf8'))
