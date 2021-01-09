cont = True
while cont:
    lower_bound = int(input("enter the lower bound :"))
    upper_bound = int(input("enter the upper bound :"))
    multiply = input("enter the expression :")
    sum = 0

    for i in range(lower_bound,upper_bound+1):
        result =("{0}{1}".format(i,multiply))
        result = eval(result)
        sum = sum + result
    print(sum)
    doagain =  (input("continue ? y/n :"))
    if doagain == 'y':
        cont = True
    else:
        cont = False