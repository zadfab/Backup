list1 = []
list2 = []
main_list = []
print("Enter the two strings")
while True:

    number  = (input(":"))
    if str(number) .lower()== "y":
        break
    list1.append(int(number))
print("Enter th second list")
while True:
    number  = (input(":"))
    if str(number) .lower()== "y":
        break


    list2.append(int(number))

for i in list1:
    for j in list2:
        if i == j:
            main_list.append(i)

main_list.sort()
print(main_list)




