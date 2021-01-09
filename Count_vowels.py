from string import digits
vowels_list = "aeiou"
string = input("enter the string here : ")
count = 0
empty_string = ""
for  i in string:

    if i in vowels_list:
        count +=1
        empty_string = empty_string + "_" + i
    else:
        empty_string = empty_string+ i

print(count," number of vowels in string")


print(empty_string.strip(digits))