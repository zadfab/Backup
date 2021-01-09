from math import ceil
from string import punctuation
string = input("enter the sentence here : ")
improvedstring = ""
for i in string:
    if i == " ":
       improvedstring=improvedstring + i
    elif i not in  punctuation:
        improvedstring=improvedstring + i
nospace= improvedstring.replace(" ","")

print("improved string is ->",nospace)
array = improvedstring.split(" ")
print(array)
print("Average word for the sentence",ceil(len(nospace)/len(array)))