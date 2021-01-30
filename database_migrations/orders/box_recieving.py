
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
        print(sheet.cell_value(i, 17),end= " ")
        print(sheet.cell_value(i, 18),end=" ")
        print(sheet.cell_value(i, 19))

    else:

        res = requests.post("http://18.216.163.168:83/api/v1/ezzytrace/boxes_received/",
                            {
                                "ezz_id":sheet.cell_value(i, 1),
                                "shipper_number":sheet.cell_value(i, 2),
                                "billing_id":sheet.cell_value(i, 3),
                                "billing_type":sheet.cell_value(i, 4),
                                "destination_country":sheet.cell_value(i, 18),
                                "order_id":sheet.cell_value(i, 7),
                                "received_date":sheet.cell_value(i, 8),
                                "inbound_tracking_number":sheet.cell_value(i, 9),
                                "weight":float(sheet.cell_value(i, 10)),
                                "length":float(sheet.cell_value(i, 11)),
                                "breadth":float(sheet.cell_value(i, 12)),
                                "charge_type":"NEW",
                                'box_id':sheet.cell_value(i, 5),
                                "freight_charge":float(sheet.cell_value(i, 14)),
                                "actual_charge":float(sheet.cell_value(i, 15)),
                                "current_status":(sheet.cell_value(i, 19)),
                                "height":0,


                            }

                            )
        # if res.status_code !=201:
        #     #print("cant created",end=" ")
        #     try:
        #         if "already exists" in str(res.json()):
        #            pass
        #         else:
        #             if sheet.cell_value(i, 1) in ezz_id_list:
        #                 pass
        #             else:
        #                 print(sheet.cell_value(i, 1))
        #                 ezz_id_list.append(sheet.cell_value(i, 1))
        #     except:
        #         print("json error",sheet.cell_value(i, 1))

        print(sheet.cell_value(i,0), '=>',res.json())
    # if index == 10:
    #     break

    # #
    index+=1

    # """{ "email" : "customer1@gmail.com", "password" : "12345678", "security_question" : "First School?", "security_answer" : "sen", "is_customer" : "True" } """

