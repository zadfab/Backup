
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

        res = requests.post("http://18.216.163.168:83/api/v1/ezzytrace/customers/",
                            {"ezz_id":sheet.cell_value(i, 1),
                             "name":sheet.cell_value(i, 2),
                             "address":f"{sheet.cell_value(i, 8)},{address2}",
                             "city":f"city_{index}",
                             "zipcode":f"zipcode",
                             "phone_number":int(sheet.cell_value(i, 13)),
                             "email":sheet.cell_value(i,7),
                             "state":int(sheet.cell_value(i, 11)),
                             "country":sheet.cell_value(i, 14),


                             })
        if res.status_code !=201:
            print("cant created",end=" ")
        print(sheet.cell_value(i, 1)," ->",res.json())
    # if index == 1:
    #     break
    # #
    # #
    index+=1