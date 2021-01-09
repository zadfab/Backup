print("Enter the number :")
number = int(input(''))
count = 0
def prime(number):
    prime_list = []
    for i in range(2,number):
        flag = False
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            prime_list.append(i)

    return prime_list

for i in prime(number):
    if number%i == 0:
        residue = number/i
        print(residue,"*",i)
