import time
import  os
second = 0
minute = 0
hour = 0

while True:
    if second == 60:
        second = 0
        minute+=1
    if minute == 60:
        minute = 0
        hour+=1

    print("{0} {1} {2}".format(hour,minute,second))
    time.sleep(1)
    second+=1
    os.system("cls")