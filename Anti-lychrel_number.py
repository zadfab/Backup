def palindrome(number):
    reverse = 0
    while number>0:
        remainder = number%10
        reverse = (reverse*10) + remainder
        number = number//10
    return reverse


user_number = int(input("Enter the number : "))
count = 0
while count<=30:
    count+=1
    sum = user_number + palindrome(user_number)
    if sum == palindrome(sum):
        print("its a Anti-lychel number,",count,"Iteration took place")
        break
    else:
        user_number = sum
else:
    print("not a anti-lychel number")