
import xlrd
import os
import requests



file_name = "Admin Panel Data.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(2)
sheet.cell_value(0, 0)

index = 0
for i in range(sheet.nrows):
    if index == 0:
        print(sheet.cell_value(i, 1),end=" ")
        print(sheet.cell_value(i, 2),end=" ")
        print(sheet.cell_value(i, 3))

    else:

        res = requests.post("http://18.216.163.168:83/api/v1/ezzytrace/status_details/",
                            {"status_id":sheet.cell_value(i, 3),
                             "name":sheet.cell_value(i, 1),
                             "type":"Order",
                             })
        print(sheet.cell_value(i, 1)," ->",res.json())

    index+=1