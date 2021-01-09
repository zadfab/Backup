user_string = input("Enter the words here :\n\t\t\t\t ")

def recurring(string):
    dict = {}
    for i in string:
        count = string.count(i)
        dict[i] = count

    return dict
print(recurring(user_string))
print("-------------------------")
print("only first character")
def first_recurring(string):
    dict = {}
    for i in string:
        count = string.count(i)
        if count>1:
            print(i)
            break


first_recurring(user_string)  