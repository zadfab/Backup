input_range = int(input("enter the range :"))
Result_list = []
for i in range(input_range+1):
    count = 0
    list = []
    sum = 0
    part = 0
    while True:
        for j in str(i):
            list.append(int(j))
        for j in list:
            count+=1
            part = j**count
            sum+=part
        #print(list,sum)
        if sum == i:
            Result_list.append(i)
            break
        else:
            break
print(Result_list)

