input_number = (input("Enter the number : "))
list = []
sum = 0
count = 0
for i in input_number:
    list.append(int(i))

for i in list:
    count+=1
    parts = i**count
    sum += parts
if sum == int(input_number):
    print(input_number , "is an Diasarium Number")
else:
    print(sum,list,"cant find")