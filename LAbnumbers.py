user_input = int(input("Enter your number here : "))
lust = []
flag = True
if user_input >1:
    for i in range(2,user_input):
        flag = True
        for j in range(2,i):
            if (i  % j)== 0 :
                flag = False
        if flag:
            lust.append(i)

print(lust)
for j  in lust:
    jp= j*j
    if user_input % jp == 0:
        print(" its a lab number")
