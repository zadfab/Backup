
import xlrd
import os
import requests







for i in range(3822,5224):
    res = requests.delete(f'http://18.216.163.168:83/api/v1/ezzytrace/products/{i}')
    try:
        print(res.json())
    except:
        print('deleted',i)
