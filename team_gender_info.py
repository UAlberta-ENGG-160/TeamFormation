#
# File : team_gender_info.py
# Author : K. Steven Knudsen
#
# Date : January 21, 2024
#
# Copyright : University of Alberta, 2024
#
import sys
import pandas as pd 

inputFile1 = sys.argv[1]

#print("Reading "+inputFile1)

classFile = pd.ExcelFile(inputFile1)
df = classFile.parse(classFile.sheet_names[0], skiprows=0)
cur_group = df.loc[0,'Groups'] 
female_count = 0
member_count = 0
for i in df.index:
    group = df.loc[i,'Groups']
    if group != cur_group:
        if female_count == 1:
            print('Group %s has %d members, %d female count <===== FIX THIS' % (cur_group, member_count,female_count) )
        else:
            print('Group %s has %d members, %d female count' % (cur_group, member_count,female_count) )
        female_count = 0
        member_count = 0
    if df.loc[i,'Sex'] != 'M':
        female_count = female_count + 1
    member_count = member_count + 1
    cur_group = group
if female_count == 1:
    print('Group %s has %d members, %d female count <===== FIX THIS' % (cur_group, member_count,female_count) )
else:
    print('Group %s has %d members, %d female count' % (cur_group, member_count,female_count) )
