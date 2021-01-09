
import xlrd
import os
import requests



file_name = "Admin Panel Data.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(6)
sheet.cell_value(0, 0)

index = 0
for i in range(sheet.nrows):
    if index == 0:
        print(sheet.cell_value(i, 1),end=" ")
        print(sheet.cell_value(i, 2),end=" ")
        print(sheet.cell_value(i, 3),end=" ")
        print(sheet.cell_value(i, 4))
        # print(sheet.cell_value(i, 5))

    else:

        res = requests.post("http://18.216.163.168:83/api/v1/ezzytrace/fedex_consolidate/",
                            {"fedex_consolidated_invoice_id":f"FC__{index}",
                             "to":sheet.cell_value(i, 3),
                             "cc_1":sheet.cell_value(i, 4),
                             "country_id":sheet.cell_value(i, 2)
                             })
        print(sheet.cell_value(i, 1)," ->",res.json())
    # if index == 1:
    #     break


    index+=1