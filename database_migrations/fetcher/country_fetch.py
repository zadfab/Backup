
import xlrd
import os
import requests

country_dict = {"Antigua":"AG","Aruba":"AW","Bonaire":"BQ","Bahamas":"BS","Columbia":"CO","Curacao":"CW","Dominican Republic":"DO","India":"IN","Panama":"PA","Sint Maarten":"SX","Saint Vincent":"VC"}

file_name = "new_customer_data.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

index = 0
for i in range(sheet.nrows):
    if index >= 1:
        try:
            print(country_dict[sheet.cell_value(i, 38)])
        except:
            print("NULL")

        # print(sheet.cell_value(i, 16))

    index+=1

