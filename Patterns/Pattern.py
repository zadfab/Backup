depth = int(input("Enter the depth you want : "))
number = 1

for i in range(depth+1):
    for j in range(i):
        square_number = number*number
        print(square_number,end=" ")
        number+=1
    print()


