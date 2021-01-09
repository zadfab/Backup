number = int(input("enter the number here : "))
list = []
if number == 1 or number==0:
    print("not a composite number")
else:
    for i in range(2,number):


        if number%i == 0:
            list.append(i)
    if len(list) >0:
        print("its a composite number",list)

    else:
        print("prime number not allowed in composite number")
