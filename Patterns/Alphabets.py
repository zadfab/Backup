depth = int(input("Enter the depth of your choice : "))
k = 0
letter_A = 65

for i in range(depth):
    k = k+2
    for j in range(0,k):

        character = chr(letter_A)
        letter_A = letter_A+1
        if letter_A > 90:
            letter_A = 65
        print(character,end=" ")
    print()