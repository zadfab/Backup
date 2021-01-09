user_range = int(input("Enter the range  : "))



letter = 65
k = 2*user_range - 2

for i in range(0,user_range+1):
    for m in range(0,k+1):
        print(" ",end="")
    k = k-1

    for j in range(0,i):
        print(chr(letter),end=" ")
        letter+=1
    print()
