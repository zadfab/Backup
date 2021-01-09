string = input("enter a word here : ")
Result_list = []
temp_string = string
for i in range(0,len(string)):

    first_word = temp_string[0]
    big_value = temp_string[1:]
    addon = big_value + first_word
    Result_list.append(addon)
    temp_string = addon
   # print(temp_string)
print(Result_list)
