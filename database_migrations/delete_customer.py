
import xlrd
import os
import requests



file_name = "customer_data.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

index = 0
for i in range(sheet.nrows):
    if index == 0:

        print(sheet.cell_value(i, 1),end=" ")

    else:

        res = requests.delete(f"http://18.216.163.168:83/api/v1/ezzytrace/customers/{sheet.cell_value(i, 1)}"

                             )

        print(sheet.cell_value(i, 1)," ->",res.status_code)
    # if index == 1:
    #     break
    # #
    # #
    index+=1