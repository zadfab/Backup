depth = int(input("Enter the number of your choice : "))

for i in range(depth+1):
    num = 1
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()