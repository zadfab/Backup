
import xlrd
import os
import requests



file_name = "box_recieving_details.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

ezz_id_list = []
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
        print(sheet.cell_value(i, 11),end=" ")
        print(sheet.cell_value(i, 12),end=" ")
        print(sheet.cell_value(i, 13),end=" ")
        print(sheet.cell_value(i, 14),end=" ")
        print(sheet.cell_value(i, 15),end=" ")
        print(sheet.cell_value(i, 16),end=" ")
        print('status',sheet.cell_value(i, 17),end= " ")
        print(sheet.cell_value(i, 18),end=" ")
        print(sheet.cell_value(i, 19))

    else:

        res = requests.post("http://18.216.163.168:83/api/v1/ezzytrace/boxes_out/",
                            {
                                "box_status":sheet.cell_value(i, 19),
                                "shipped_by":'operator_1',
                                "box_weight":sheet.cell_value(i, 10),
                                "box_id":sheet.cell_value(i, 5),




                            }

                            )

        try:
            print(sheet.cell_value(i,0),res.json())
        except:
            print("cant create : ",sheet.cell_value(i,0))


    # if index == 2:
    #     break

    # #
    index+=1

    # """{ "email" : "customer1@gmail.com", "password" : "12345678", "security_question" : "First School?", "security_answer" : "sen", "is_customer" : "True" } """

