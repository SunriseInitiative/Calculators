angles = []
angleSum = 0
maxAngleSum = 0
while True:
    try:
        N = int(input())
        angles.append(N)
    except:
        break

for i in range(len(angles)):
    angleSum += angles[i]

maxAngleSum = (len(angles) - 1) * 180
print(maxAngleSum - angleSum)