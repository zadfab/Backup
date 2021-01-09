from  math import sqrt
let_em_come = input("enter the number is format (x1,y1) (x2,y2) : ")
flag = False
to_remove = "() ,"

list =[]
for i in let_em_come:
    if  i == "-":
        flag = True
        continue
    if flag:
        minus = "-" + i
        list.append(int(minus))
        flag = False

    elif i not in to_remove:
        list.append(int(i))




print("%0.2f" % sqrt((list[2]-list[0])*(list[2]-list[0])+ (list[3] - list[1])*(list[3] - list[1])))
