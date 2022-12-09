import numpy

with open('input.txt', 'r') as file:
    data = file.read().strip().split()
    data = [[*i] for i in data]
data = [list(map(int, i)) for i in data]
# print(data)

array = numpy.array(data)
# print(array)
# print()

lx = len(array[0])
ly = len(array)

visible_trees = 0
for row in range(len(array)):
    for col in range(len(array[0])):
        coords = (row, col)
        value = array[coords]
        left = list(array[coords[0], :coords[1]])
        right = list(array[coords[0], coords[1] + 1:])
        up = list(array[:coords[0], coords[1]])
        down = list(array[coords[0] + 1:, coords[1]])
        result = [(max(left) if left else -1) < value, (max(right) if right else -1) < value,
                  (max(up) if up else -1) < value, (max(down) if down else -1) < value]
        if any(result):
            visible_trees += 1
        # print('coord: {}, val: {}, left: {}, right: {}, up: {}, down: {}'.format(coords, value, left, right, up, down))

print('Visible trees from outside:', visible_trees)
