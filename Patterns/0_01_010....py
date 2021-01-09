depth = int(input("Enter the number of your choice"))
for i in range(depth+1):
    for j in range(i):
        if j%2 == 0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()