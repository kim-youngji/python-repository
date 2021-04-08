# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:03:39 2021

@author: User
"""

from openpyxl import load_workbook
from openpyxl import workbook
from glob import *
import os

my file = [i for i in glob('*.xlsx')]

total_student = []

for item in myfiles:
    my_workbook = ioad_workbook(item, data_only = true)
    my_worksheet = my_workbook['sheet1']
    my_list = []
    my_list.append(my_worksheet['A2'].value)
    my_list.append(my_worksheet['B2'].value)
    my_list.append(my_worksheet['C2'].value)
    my_list.append(my_worksheet['D2'].value)
    total_student.append(my_list)
    print(my_list)

total_student_by_group = {}
for i in range (10):
    total_student_by_group["group"+str(i+1)] = {}
print (total_student_by_group)

assign_dict = {}
for i in range(10):
    assign_dict[i+1] = "group"+str(i+1)
    print(assign_dict)

student_number_tracker = [0,0,0,0,0,0,0,0,0,0]

print(total_student)

for item in total_student:
    group = item[2]
    group_name = assign_dict[group]
    total_student_by_group[group_name]["student_"+str(student_number_tracker[group-1]+1)] = item
    student_number_tracker[group-1] += 1
    
print(total_student_by_group)
print(student_number_tracker)

my_writting_wb = workbook()

for i in range(10):
    write_ws = my_writting_b.create_sheet("jo"+str(i+1))
    
for i in range(10):
    
    load_ws = my_writting_wb["jo"+str(i+1)]
    load_ws.append(["stu_num","name","group_id","git"])
    
    templist = list(total_student_by_group["group"+str(i+1)].values())
    print(templist)
    for j in range(4):
        try:
            load_ws.append(templist[j])
        except:
            pass
        
my_writting_wb.remove(my_writting_wb['sheet'])
my_writting_wb.save("group_python.xlsx")