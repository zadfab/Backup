file=open('text.txt','r+')
f=file.readlines()
print(f)
z=file.write("no yes but not always")
for i in f:
    print(i,end='/')
    print(i,end='/')

print(z)