user_name = input("enter you name")
user_name = user_name.upper()
list = []
for i in user_name:
    list.append(i)


k = 2*len(user_name) - 2
count = 0
try:
    for i in range(0,len(list)):
        for m in range(0,k):
            print(" ",end="")
        k -=1

        for j in range(i):
            print(list[count],end=' ')
            count+=1
        print()
except IndexError:
    pass