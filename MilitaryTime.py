import time
from datetime import datetime

inputformat="%I:%M %p"
outputformat="%H:%M"
format12=input("Enter 12hr format here: ")
convertedformat=datetime.strptime(format12,inputformat)

print(datetime.strftime(convertedformat,outputformat))
print("today's date")
print(datetime.today())
print(time.asctime(time.localtime()))
print(time.process_time())
