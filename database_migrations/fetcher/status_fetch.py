
import xlrd
import os
import requests

status_dict = {"Ready to ship":"RTS","Tracked":"TD","Completed":"CM","Failed":"F","Consolidation":"WFC","Incomplete":"IN","Shipped":"SP","Discarded":"DISC",
               "Payment Not Authorized":"PNA","Info Missing":"Info Missing","ESCROW":"UID","On Hold":"HOLD"}
file_name = "box_recieving_details.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

index = 0
for i in range(sheet.nrows):
    if index >= 1:
        print(status_dict[sheet.cell_value(i, 16)])

    index+=1

