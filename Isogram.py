inputsrting=input()

uniqueset=set(inputsrting.lower())

if len(uniqueset)==len(inputsrting):
    print('isogram')
else:

    print(abs(len(uniqueset)-len(inputsrting)),' matching letters found ,not an isogarm')
