depth = int(input("Enter the number you want : "))

num = 3
for i in range(0,depth):
    if i >= int(depth/2)+1:
        num-=1
        for j in range(0,num-1):
            print("#",end = " ")

        print()
    else:

        for j in range(0,num):


            print("#",end=" ")
        num+=1


        print()
