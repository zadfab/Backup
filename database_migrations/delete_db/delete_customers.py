
import xlrd
import os
import requests



file_name = "customer_data.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

index = 0
for i in range(370,sheet.nrows):
    if index == 0:

        print(sheet.cell_value(i, 1),end=" ")
        print(sheet.cell_value(i, 2),end=" ")
        print(sheet.cell_value(i, 3),end=" ")
        print(sheet.cell_value(i, 4),end=" ")
        print(sheet.cell_value(i, 5),end=" ")
        print(sheet.cell_value(i, 6),end=" ")
        print(sheet.cell_value(i, 7),end=" ")
        print(sheet.cell_value(i, 8),end=" ")
        print(sheet.cell_value(i, 9),end=" ")
        print(sheet.cell_value(i, 10),end=" ")
        print(sheet.cell_value(i, 11))

    else:
        if sheet.cell_value(i,9) == 0:
            address2 = ""
        else:
            address2 = sheet.cell_value(i,9)

        res = requests.delete(f"http://18.216.163.168:83/api/v1/ezzytrace/customers/{sheet.cell_value(i, 1)}",

                            )
        try:
            print(sheet.cell_value(i, 1),res.json())
        except:
            print(sheet.cell_value(i, 1),' : deleted')
    # if index == 1:
    #     break
    # #
    # #
    index+=1