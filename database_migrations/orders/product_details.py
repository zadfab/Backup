
import xlrd
import os
import requests



file_name = "order_details.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

id_list = []
index = 0
for i in range(sheet.nrows):
    if index == 0:

        print("1",sheet.cell_value(i, 1),end=" ")
        print("2",sheet.cell_value(i, 2),end=" ")
        print("3",sheet.cell_value(i, 3),end=" ")
        print("4",sheet.cell_value(i, 4),end=" ")
        print("5",sheet.cell_value(i, 5),end=" ")
        print("6",sheet.cell_value(i, 6),end=" ")
        print("7",sheet.cell_value(i, 7),end=" ")
        print("8",sheet.cell_value(i, 8),end=" ")
        print("9",sheet.cell_value(i, 9),end=" ")
        print("10",sheet.cell_value(i, 10),end=" ")
        print("11",sheet.cell_value(i, 11),end=" ")
        print("12",sheet.cell_value(i, 12),end=" ")
        print("13",sheet.cell_value(i, 13),end=" ")
        print("14",sheet.cell_value(i, 14),end=" ")
        print("15",sheet.cell_value(i, 15))


    else:

        res = requests.post("http://18.216.163.168:83/api/v1/ezzytrace/products/",
                            {
                                "description":sheet.cell_value(i, 4).strip(),
                                "quantity":sheet.cell_value(i, 5),
                                "unit_price":sheet.cell_value(i, 6),
                                "custom_charge":sheet.cell_value(i, 8),
                                "inspection_status":'Good',
                                "order_id":sheet.cell_value(i, 1).strip(),
                                "category":sheet.cell_value(i, 2).strip(),
                                'csv_no':sheet.cell_value(i, 11),
                            }

                     )
        try:
            print(index ,'=>',sheet.cell_value(i, 1)," ->",res.json())
        except:

            print("cant create =>", index, sheet.cell_value(i, 1),sheet.cell_value(i, 4))
    # if index == 1:
    #     break

    # #
    index+=1

    # """{ "email" : "customer1@gmail.com", "password" : "12345678", "security_question" : "First School?", "security_answer" : "sen", "is_customer" : "True" } """
