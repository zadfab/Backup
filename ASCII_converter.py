string = input("Enter the string ")
print(ord(string)," is the ASCII value")

print("do you want list of ASCII values y/n :")
option = input()

if option == "y" or option == "Y":
    print("enter the limit :")
    limit = int(input("upper limit :"))
    limit2 = int(input("lower limit :"))

    def grooup(limit,limit2):
        result = ''
        for i in range(limit,limit2+1):
            result = result + " "+(chr(i))

        return result
    print(grooup(limit,limit2))
