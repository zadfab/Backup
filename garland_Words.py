user_word = input("Enter the word to check for garland")
revers = user_word[::-1]
count = 0
for i in range(len(user_word)+1):
    count+=1
    left_str = user_word[0:i]
    right_str = revers[0:i]
    right_str = right_str[::-1]


    if left_str == right_str:

        if count==1:
            pass
        if count>1 and count<len(user_word):
            print(count-1,left_str,right_str)