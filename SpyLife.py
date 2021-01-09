
encodedstr=input("Enter your encoded string here:")
encodedstr=encodedstr[::-1]
#print(encodedstr)
numbers="1234567890!@#$%^&*()/*-+.~`<>,.?/'_=' '  '"

outputstr=""

for j in encodedstr:
    #print(j,end="")
    if j==" ":
        outputstr=outputstr + " "
    else:

        if j not in numbers:
            outputstr=outputstr + j

print(outputstr)



print()