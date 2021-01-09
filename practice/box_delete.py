
import requests

for box in range(200,250):


    res = requests.delete(f"http://3.131.16.17/api/v1/ezzytrace/boxes_out/{str(box)}",
                        )
    #print(res,res.json())
    if res.status_code == 204:
        print(f"BOx deleted - {box}",res,res.status_code)
    else:
        print(f"Box not found - {box}",res,res.status_code)




