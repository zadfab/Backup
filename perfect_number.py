for j in range(1,1000):
    user_number = j
    divisors  =[]
    for i in range(1,user_number):
             if user_number % i == 0:
                 divisors.append(i)
    sum = 0
    for i in divisors:
        sum = sum+i

    if sum ==user_number:
        print(user_number,"Perfect Number")

