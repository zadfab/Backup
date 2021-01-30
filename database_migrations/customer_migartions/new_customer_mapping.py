
import xlrd
import os
import requests



file_name = "new_customer_data.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(0)
#sheet.cell_value(0, 0)

index = 0
for i in range(sheet.nrows):
    if index == 0:

        print(sheet.cell_value(i, 1),end=" ")
        print(sheet.cell_value(i, 2),end=" ")
        print(sheet.cell_value(i, 3),end=" ")
        print('email =>',sheet.cell_value(i, 4),end=" ")
        print('phone =>',sheet.cell_value(i, 5),end=" ")
        print(sheet.cell_value(i, 6),end=" ")
        print(sheet.cell_value(i, 7),end=" ")
        print(sheet.cell_value(i, 8),end=" ")
        print(sheet.cell_value(i, 9),end=" ")
        print(sheet.cell_value(i, 10),end=" ")
        print(sheet.cell_value(i, 11),end=" ")
        print(sheet.cell_value(i, 12),end=" ")
        print('add1 +>',sheet.cell_value(i, 13),end=" ")
        print("addd2 =>",sheet.cell_value(i, 14),end=" ")
        print('city +>',sheet.cell_value(i, 15),end=" ")
        print(sheet.cell_value(i, 16),end=" ")
        print(sheet.cell_value(i, 17),end=" ")
        print('zip +>',sheet.cell_value(i, 18),end=" ")
        print(sheet.cell_value(i, 19),end=" ")
        print(sheet.cell_value(i, 20),end=" ")
        print(sheet.cell_value(i, 21),end=" ")
        print(sheet.cell_value(i, 22),end=" ")
        print(sheet.cell_value(i, 23),end=" ")
        print(sheet.cell_value(i, 24),end=" ")
        print(sheet.cell_value(i, 25),end=" ")
        print(sheet.cell_value(i, 26),end=" ")
        print(sheet.cell_value(i, 27),end=" ")
        print('first =>',sheet.cell_value(i, 28),end=" ")
        print('second +>',sheet.cell_value(i, 29),end=" ")
        print(sheet.cell_value(i, 30),end=" ")
        print(sheet.cell_value(i, 31),end=" ")
        print(sheet.cell_value(i, 32),end=" ")
        print(sheet.cell_value(i, 33),end=" ")
        print(sheet.cell_value(i, 34),end=" ")
        print(sheet.cell_value(i, 35),end=" ")
        print(sheet.cell_value(i, 36),end=" ")
        print(sheet.cell_value(i, 37),end=" ")
        print(sheet.cell_value(i, 38),end=" ")
        print(sheet.cell_value(i, 39))


    else:
        if sheet.cell_value(i,9) == 0:
            address2 = ""
        else:
            address2 = sheet.cell_value(i,9)

        res = requests.post("http://18.216.163.168:83/api/v1/ezzytrace/customers/",
                            {"ezz_id":sheet.cell_value(i, 1),
                             "name":f'{sheet.cell_value(i, 28)} {sheet.cell_value(i,29)}',
                             "address":f"{sheet.cell_value(i, 13)};{sheet.cell_value(i,14)}",
                             "city":sheet.cell_value(i,15),
                             "zipcode":sheet.cell_value(i,18),
                             "phone_number":int(sheet.cell_value(i, 5)),
                             "email":sheet.cell_value(i,4),
                             "state":int(sheet.cell_value(i, 39)),
                             "country":sheet.cell_value(i, 40),


                             })
        # if res.status_code !=201:
        #     print("cant created",end=" ")
        if 'already exists.' not in f'{res.json()}':
            print(sheet.cell_value(i, 1)," ->",res.json())
    # if index == 2:
    #     break
    # #
    # #
    index+=1