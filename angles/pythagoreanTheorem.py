import math

def pythagoreanTheorem(knownSide1, knownSide2, KS1I, KS2I):
    if knownSide1 == "a" and knownSide2 == "b":\
        return math.sqrt(KS1I**2 + KS2I**2)
    elif knownSide1 == "b" and knownSide2 == "c":
        return math.sqrt(KS1I**2 - KS2I**2)
    else:
        return math.sqrt(KS2I**2 - KS1I**2)

knownSide1 = input("enter known side 1: ")
knownSide2 = input("enter known side 2: ")

KS1I = float(input("enter known side 1 length: "))
KS2I = float(input("enter known side 2 length: "))

print(pythagoreanTheorem(knownSide1, knownSide2, KS1I, KS2I))
