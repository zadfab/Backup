
import requests

for i in range(1,100):
    numb = str(i).zfill(6)
    order = f"20-{numb}-IN-002"
    res = requests.delete(f"http://3.131.16.17/api/v1/ezzytrace/boxes_received/{order}/",
                          )
    #print(res,res.json())
    if res.status_code == 204:
        print(f"BOx deleted - {order}",res,res.status_code)
    else:
        print(f"Box not found - {order}",res,res.status_code)




