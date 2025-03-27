manualOverride = False

RIA = int(input("Enter the regular interior angle: "))

sides = 3
currentSideLength = 0

while True:
    '''
    print(sides)
    currentSideLength = ((sides - 2) * 180) / sides
    print(currentSideLength)
    '''
    if RIA == ((sides - 2) * 180) / sides:
        print(f"{sides}-sided polygon has a regular interior angle of {RIA}")
        break
    else:
        sides += 1
    if sides >= 100:
        print("Exceded calculation limit")
        break