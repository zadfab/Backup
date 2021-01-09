import  time
import  datetime
import winsound
user_time = input("Enter the time here : ")

print(datetime.datetime.today())
time_now = datetime.datetime.today()


print(time_now.strftime("%H:%M:%S"))

alram_time = datetime.datetime.strptime(user_time,"%H:%M:%S")
print(alram_time.time())

while True:
    time.sleep(1)
    time_now = datetime.datetime.today()
    instant_time = time_now.strftime("%H:%M:%S")
    if instant_time == str(alram_time.time()):
        print("Time now")
        winsound.Beep(2000,5000)
        break
    else:
        print(instant_time)