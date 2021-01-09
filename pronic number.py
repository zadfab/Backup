user_number = int(input("Enter the number : "))

for i in range(1,user_number):
    partial_res = i*(i+1)
    if partial_res == user_number:
        print("number : {} is pronic number".format(user_number))
        break


else:
    print("not")
