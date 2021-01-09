def prime(number):
    for i in range(2,number):
        if number%i == 0:
            print("Not a Howling prime")
            break
    else:
        print(user_number,"  |  your number is Howling prime number ")
user_number = int(input("Enter the number : "))

sum = 0
for i in str(user_number):
    sum = sum + int(i)

prime(sum)