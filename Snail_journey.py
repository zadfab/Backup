tree_length = float(input("Enter the length of the tree :"))
init_climb = float(input("Enter the length of snail climbed up at day time :"))
down = float(input("Enter the length snail climbed down at night time :"))

total_length = 0
count = 0
climb = init_climb
while tree_length > total_length:
    total_length  = climb-down
    climb = total_length + init_climb
    count+=1
    print(total_length,"total length")
    print(climb,"climb init")

print(count,"no of days took")