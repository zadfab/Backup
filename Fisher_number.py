user_number = int(input("Enter the number : "))

cube = user_number*user_number*user_number
multiply = 1
for i in range(1,user_number+1):
    if user_number%i == 0:
        multiply = multiply*i
print(multiply,cube)
if multiply == cube:
    print("Number is Fisher number")
else:
    print("Not a fisher number")