states = {"Barbuda":3,"Redonda":4,"St. George":11,"St. John":12,"St. Mary":13,"St. Paul":14,"St. Peter":15,"St. Philip":16,"Oranjestad":18,"Kralendijk":7,"Abaco":2,"Andros":1,"Eleuthera":8,
          "Grand Bahamas":9,"New Providence":17,"Bogota DC":22,"Willemstad":10,"Haryana":5,"Karnataka":27,"Maharashtra":24,"New Delhi":23,"Punjab":"6","Telangana":26,
          "Uttar Pradesh":25,"West Bengal":28,"Panama City":21,"Phillipsburg":19,"Kingstown":20
          }

import xlrd
import os
file_name = "customer_data.xlsx"
excel_path = os.path.join(r"C:\Users\User\Pictures\Screenshots",file_name)
wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

index = 0
for i in range(sheet.nrows):
    try:
        if index == 0:
            pass
        else:
            print(states[sheet.cell_value(i, 10)])
        index+=1
    except:
        pass
