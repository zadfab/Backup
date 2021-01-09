user_number = (input("Enter the number"))
sum = 0
mul = 1
for i in user_number:
    sum = sum+int(i)
    mul = mul*int(i)

if mul == sum:
    print('True | Spy number')

else:
    print("False | Not a spy number")