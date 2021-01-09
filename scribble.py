points = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}

user_string = input("Enter the sentence here : ")
dict ={}
improved_user_string = user_string.split(" ")

if len(improved_user_string)  <= 10 :
    for i in improved_user_string:
        som = 0
        for j in i:
            som = som + points[j]

            dict.update({i:som})


def getmax(read):
    v=list(read.values())
    k=list(read.keys())
    print(v)
    print(k)

    return k[v.index(max(v))]

print(getmax(dict))