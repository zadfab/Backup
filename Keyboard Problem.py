from string import punctuation

string = input(" enter your distorted text here :")


for i in string:
    todd = string.replace(i,"")

print(todd)