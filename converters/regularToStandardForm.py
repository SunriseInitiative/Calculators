number = input("Enter a number in regular form: ")
index = len(list(number)) - 1

print(str((int(number) / 10**index)) + " * 10^" + str(index))