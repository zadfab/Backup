
import xlrd
import os
import requests



file_name = "new_category_details.xlsx"
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
        print(sheet.cell_value(i, 5))

    else:

        res = requests.patch(f"http://18.216.163.168:83/api/v1/ezzytrace/categories/{sheet.cell_value(i, 1)}/",
                            {
                             "vat":sheet.cell_value(i, 5),
                             "custom_duty":sheet.cell_value(i, 4)
                             })
        print(sheet.cell_value(i, 1)," ->",res.json())
    # if index == 1:
    #     break


    index+=1