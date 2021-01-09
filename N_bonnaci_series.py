nomial = int(input("Enter the number of nomnials : "))
user_range = int(input("Enter the limit : "))

list = []
result_list = []
count = 0
for i in range(1,nomial):
    list.append(0)
    result_list.append("0")
    count+=1
list.append(1)
result_list.append("1")
user_range = user_range - count
while user_range > 1:
    partial_add = 0
    for j in list:
        partial_add = partial_add+j
    result_list.append(str(partial_add))

    list.remove(list[0])
    list.append(partial_add)
    user_range-=1
print(" ".join(result_list))