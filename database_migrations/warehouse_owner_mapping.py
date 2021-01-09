
import xlrd
import os
import requests



file_name = "Admin Panel Data.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(8)
sheet.cell_value(0, 0)

index = 0
for i in range(sheet.nrows):
    if index == 0:
        print(sheet.cell_value(i, 0),end=" ")
        print(sheet.cell_value(i, 1),end=" ")
        print(sheet.cell_value(i, 2),end=" ")
        print(sheet.cell_value(i, 3),end=" ")
        print(sheet.cell_value(i, 4),end=" ")
        print(sheet.cell_value(i, 5),end=" ")
        print(sheet.cell_value(i, 6),end=" ")
        print(sheet.cell_value(i, 7),end=" ")
        print(sheet.cell_value(i, 8),end=" ")
        print(sheet.cell_value(i, 9))

    else:

        res = requests.post("http://18.216.163.168:83/api/v1/ezzytrace/warehouse_owner/",
                            {"owner_id":sheet.cell_value(i, 2),
                             "city":sheet.cell_value(i, 5),
                             "name":sheet.cell_value(i, 0),
                             "address1":sheet.cell_value(i, 7),
                             "address2":sheet.cell_value(i, 8),
                             "email":sheet.cell_value(i, 2),
                             "zipcode":sheet.cell_value(i, 9),
                             "country_id":sheet.cell_value(i, 4),
                             "phone_number":int(sheet.cell_value(i, 3)),
                             "warehouse_id":sheet.cell_value(i, 1),
                             "state":int(sheet.cell_value(i, 6)),

                             })
        print(sheet.cell_value(i, 1)," ->",res.json())
    # if index == 1:
    #     break


    index+=1