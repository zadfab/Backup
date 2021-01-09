noises = input("enter the noises here")
noises_list = noises.split(" ")
result = ""
dict = {'Grr':'Lion','Rawr':'Tiger','Ssss':'snake','Chirp':'Bird'}
for  i in noises_list:
    result = result + (dict.get(i))+ " "
print(result)