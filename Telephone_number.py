telephone_number = (input("Enter the number : "))


country_code = telephone_number[0:3]
if len(telephone_number[3:])>7:
    one_part = telephone_number[3:5]
    second_part = telephone_number[5:8]
    third_part = telephone_number[8:11]
    print(third_part)
    print("(+{0}){1}-{2}-{3}".format(country_code,one_part,second_part,third_part))
elif len(telephone_number[3:])==7:
    one_part = telephone_number[3:6]
    second_part = telephone_number[6:10]

    print("(+{0}){1}-{2}".format(country_code,one_part,second_part))
