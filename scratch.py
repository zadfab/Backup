file=open('text.txt','rb+')
f=file.readlines()
print(f)
try:

    z=file.write("no yes but not always")
    for i in f:
        print(i,end='/')
        print(i,end='/')
except:

    print("cant write")