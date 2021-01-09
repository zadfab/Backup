string = input("enter your string : ")

length_of_string = int(len(string)/2)
print(length_of_string)
first_part = string[0:length_of_string]
second_half = string[length_of_string:]
print("testing -",first_part,second_half)
if first_part == second_half:
    print("not a prime string")
else:
    print("its a prime string")
