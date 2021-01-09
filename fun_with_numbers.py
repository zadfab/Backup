target_number = input("Enter the target number :")
number = "123456789"
import  random
op = ["-","+",""]


def equation():
    global check
    eq = ""
    for i in number :
        eq = eq+i
        j = random.choice(op)
        if j =="":
            j = ""
        eq = eq+j
    if eq[-1] in op:
        check = eq[:-1]
    else:
        check = eq
    result = eval(check)

    return (result)

while True:
    result = equation()
    if str(result) == target_number:
        print(check," = ",result)

