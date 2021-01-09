user_input = int(input("enter the number :"))

def prime(number):

        for i in range(2,number):

            if number%i == 0:
                print("not a prime")
                break
        else:
            print("proceeding...")
            return True
        return False

if prime(user_input):
    reciprocal = str(1/user_input)
    if str(user_input) in reciprocal:
        print(user_input,"present in ",reciprocal,"this is a Voodo prime number")
    else:
        print("Not a voodo prime number")

else:
    print("try with prime number this time")