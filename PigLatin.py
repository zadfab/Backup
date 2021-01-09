string = input("Enter your words here : ")
outputstring=""
array = string.split(" ")

for i in array:
    firstword=i[0]
    outputstring = outputstring + i[1:] + firstword + "ay" +" "
print("output is : {0}".format(outputstring))


