listed = []
with open("input.txt") as f:
    for i in f:
        listed.append(list(i.strip()))

gamma = ""
epsilon = ""

for i in range(len(listed[0])):
    ones = 0
    zeros = 0
    for j in range(len(listed)):
        if listed[j][i] == "1":
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(listed)
print(int(gamma, 2) * int(epsilon, 2))
