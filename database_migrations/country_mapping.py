import os

import openpyxl

file_name = "Admin Panel Data.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)


# wb = openpyxl.load_workbook(excel_path)
# # sheet = wb.active
# print(wb.get_sheet_names())
# worksheet1 = wb['Country_table']
# print(worksheet1)
# for row in worksheet1.iter_rows():
#      print(row[0].value())

import xlrd

import requests

wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

index = 0
for i in range(sheet.nrows):
     if index == 0:
          pass
     else:

          res = requests.post("http://18.216.163.168:83/api/v1/ezzytrace/countries/",
                              {"country_id":sheet.cell_value(i, 3),
                               "name":sheet.cell_value(i, 1),
                               "fedex_code":sheet.cell_value(i, 3),
                               "telecode":int(sheet.cell_value(i, 2)),
                               "threshold_weight":100,
                               "tele_length":sheet.cell_value(i, 4),
                               })
          print(sheet.cell_value(i, 1)," ->",res.json())
          
     index+=1

     # print(sheet.cell_value(i, 1),end= " ")
     # print(sheet.cell_value(i, 2),end= " ")
     # print(sheet.cell_value(i, 3),end= " ")
     # print(sheet.cell_value(i, 4),end= " ")
     # print(sheet.cell_value(i, 5))