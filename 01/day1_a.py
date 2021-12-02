listed = []
counter = 0
with open("input.txt") as f:
    for i in f:
        listed.append(int(i.strip()))
    for i in range(1, len(listed)):
        if listed[i] > listed[i - 1]:
            counter += 1

print(counter)

