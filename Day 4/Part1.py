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
    list1_substracted = list(set(list1) - set(list2))
    list2_substracted = list(set(list2) - set(list1))

    if not list1_substracted or not list2_substracted:
        overleap += 1
print(overleap)
