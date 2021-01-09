inu=(input("Enter string : "))
outu=""
arr=[]
arr=inu.split(" ")

dict={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','0':'zero','10':'ten'}
for i in arr:


    if i in dict:

        output=dict.get(i)

        outu= outu + output + " "
    else:
       outu = outu+i+ " "
print(outu,)

lst=[].append("5")
print(lst)