number = int(input("Enter the number here : "))
number1 = number
from math import floor
while number1 != 0:
    print(number1)
    if number1%2 == 0:
        number1 = round(number1/2)

    elif number1%3 == 0:
        print(number1)
        number1 =floor(number1/3)

    elif number1%5 == 0:
        number1 =round(number1/5)

    elif number1%number1==0:
        break

if number1 == 0 or number1==1:
    print("Ugly number")
else:
    print("not a dirty number")