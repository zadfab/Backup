triangle_depth = int(input("Enter depth of triangle : "))
reverse = input("do you want reverse of yhis triangle?  y/n :")
floyd_number = 1
for i in range(1,triangle_depth+1):

    for j in range(1,i+1):
        print(floyd_number,end=" ")
        floyd_number+=1
    print()



if reverse =="y":
    print("Reverse of triangle")
    floyd_number = int(triangle_depth*(triangle_depth+1)/2)
    for i in range(triangle_depth+1,1,-1):
        for j in range(i,1,-1):
            print(floyd_number,end=' ')
            floyd_number-=1
        print()
