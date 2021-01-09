from math import ceil
paint_box = int(input("enter the amount of paint box needed : "))

cost_of_paint = paint_box*5 +40

tax = ((cost_of_paint* 10)/100)

print(ceil(tax + cost_of_paint) ,"- is the total cost")