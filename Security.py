string = input("enter security input : ")
string= string.replace("x","")
print(string)


br = 0
for i in string:
    br +=1
    temp= string[br:]
   # print(br)
    print(temp)
    #print("i ->",i)


    for j in temp:

        #print ("j ->",j)
        if i == "T":
            if j == "G":
                print("quiet")
                quit()
            elif j =="$":
                print("ALARM")
                quit()
        if i == "$":
            if j == "T":
                print("ALARM")
                quit()
            elif j == "G":
                print("quiet")
                quit()








