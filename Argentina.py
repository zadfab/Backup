pesos = int(input("Enter pesos amount of hat : "))#1000
dollar = int(input("Enter dollar amount of hat : "))#10

pesos_conversion = (pesos/100)  * 2#2000
print(pesos_conversion)
if pesos_conversion >dollar:
    print("Dollars")
else                                                                                                                                        :
    print("Pesos")