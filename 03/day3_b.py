listed = []
listed_least = []
with open("input.txt") as f:
    for i in f:
        listed.append(list(i.strip()))
        listed_least.append(list(i.strip()))

gamma = ""
epsilon = ""
pos = 0
pos_b = 0
while len(listed) > 1:
    ones = 0
    zeros = 0
    for i in range(len(listed)):
        if listed[i][pos] == "1":
            ones += 1
        else:
            zeros += 1
    if ones > zeros or ones == zeros:
        listed = [x for x in listed if x[pos] == "1"]
    elif ones < zeros:
        listed = [x for x in listed if x[pos] == "0"]
    pos += 1

while len(listed_least) > 1:
    ones = 0
    zeros = 0
    for i in range(len(listed_least)):
        if listed_least[i][pos_b] == "1":
            ones += 1
        else:
            zeros += 1
    if ones > zeros or ones == zeros:
        listed_least = [x for x in listed_least if x[pos_b] == "0"]
    elif ones < zeros:
        listed_least = [x for x in listed_least if x[pos_b] == "1"]
    pos_b += 1

print(int("".join(["".join(x) for x in listed]), 2) * int("".join(["".join(x) for x in listed_least]), 2) )