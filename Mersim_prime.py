user_input = int(input("Enter the number : "))

def prime(number):
    for i in range(2,number):
        if number%i == 0:
            return False
    else:
        return True
result = 1
if prime(user_input):

    for j in  range(user_input):
        result= result*2
        result1 = result-1
        if result1 == user_input:
            print("mersim prime number")
            break
    else:
        print("not a mersium prime number")
else:
    print("not a prime number")

