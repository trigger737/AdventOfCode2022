import re

with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')

crates = data[0].replace('[', ' ').replace(']', ' ').split('\n')
# print(crates[:-1])

boxes = []
for i in crates[-1]:
    if i.isdigit():
        boxes.append(crates[-1].index(i))
# print(boxes)

columns = []
for i in boxes:
    column = []
    for row in crates[:-1]:
        if row[i] != ' ':
            column.insert(0,row[i])
    columns.append(column)

# print(columns)
# print()

steps = data[1].strip().split('\n')

# print(steps)
cmds = []
for row in steps:
    cmds.append(re.findall(r"\d+",row))

for cmd in cmds:
    mv_count = int(cmd[0])
    mv_from = int(cmd[1])-1
    mv_to = int(cmd[2])-1

    columns[mv_to] += reversed(columns[mv_from][-mv_count:])
    del columns[mv_from][-mv_count:]

# print(columns)
result = ''
for column in columns:
    result += column.pop()
print(result)
