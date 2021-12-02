listed = []
with open("input.txt") as f:
    for i in f:
        listed.append(int(i.strip()))

counter = 0

listed_threes = []
for i in range(0, len(listed)):
    listed_threes.append(listed[i:i + 3])

for i in range(1, len(listed_threes)):
    print(sum(listed_threes[i]))
    if sum(listed_threes[i]) > sum(listed_threes[i - 1]):
        counter += 1
print(counter)

