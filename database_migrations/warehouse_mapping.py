
import xlrd
import os
import requests



file_name = "Admin Panel Data.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(4)
sheet.cell_value(0, 0)

index = 0
for i in range(sheet.nrows):
    if index == 0:
        print(sheet.cell_value(i, 1),end=" ")
        print(sheet.cell_value(i, 2),end=" ")
        print(sheet.cell_value(i, 3),end=" ")
        print(sheet.cell_value(i, 4),end=" ")
        print(sheet.cell_value(i, 5),end=" ")
        print(sheet.cell_value(i, 6),end=" ")
        print(sheet.cell_value(i, 7),end=" ")
        print(sheet.cell_value(i, 8))

    else:

        res = requests.post("http://18.216.163.168:83/api/v1/ezzytrace/warehouses/",
                            {"state":int(sheet.cell_value(i, 3)),
                             "warehouse_id":f"warehouse_{index}",
                             "name":f"Warehouse_{sheet.cell_value(i, 2)}",
                             "address":f"{sheet.cell_value(i, 4)},{sheet.cell_value(i, 5)}",
                             "city":sheet.cell_value(i, 6),
                             "zipcode":sheet.cell_value(i, 8),
                             "country":sheet.cell_value(i, 2)

                             })
        print(sheet.cell_value(i, 1)," ->",res.json())
    # if index == 1:
    #     break


    index+=1