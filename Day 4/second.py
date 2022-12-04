import re

with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n')

data = list(map(lambda x: [int(s) for s in re.findall(r'\b\d+\b', x)], data))
# print(data)
full = []
for pack in data:
    full.append([list(range(pack[0], pack[1] + 1)), list(range(pack[2], pack[3] + 1))])

# print(full)
overleap = 0
for n_list in full:
    list1 = n_list[0]
    list2 = n_list[1]
    # print(list1, list2)
    count = 0
    for n in list1:
        if n in list2:
            count += 1
            # print(n)
    if count:
        overleap += 1

print(overleap)
