print(int("10",12))
print("".join('hello world'.split()))

def fun(num):
    return num*num

a= 3
b = fun
print(b(3))

def fun1(arg):
    return arg.split("hello")

print(fun1("hello"))

print("helloworld"[2::3])

a='1000'
b = int(a,3)
print(b)

dict = {}
dict[(1,2)] = 3
dict[3] = 1,2
print(list(dict.keys()))