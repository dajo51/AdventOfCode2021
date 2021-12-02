listed = []
horizontal = 0
depth = 0
with open("input.txt") as f:
    for i in f:
        listed.append(i.strip().split(" "))

for i in listed:
    if i[0] == "forward":
        horizontal += int(i[1])
    elif i[0] == "up":
        depth -= int(i[1])
    elif i[0] == "down":
        depth += int(i[1])

print(horizontal * depth)