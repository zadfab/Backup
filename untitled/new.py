def factorial(num):
    a=0
    b=1
    temp=0
    if(num==1):
        print(a)
    elif(num<0):
        print("negative numbers are not allowed in fabonici number")
    else:
        print(a,end=" ")
        print(b,end=" ")
        while (temp < num):
            temp = a + b
            a = b
            b = temp
            print(temp, end=" ")
            temp=temp+1


limit=int(input('enter the number for fabonicci'))
factorial(limit)