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
vis_left = 0
vis_right = 0
vis_up = 0
vis_down = 0
vis_score = []
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
        # print('coord: {}, val: {}, left: {}, right: {}, up: {}, down: {}, max: {}'.format(coords, value, left, right, up, down, result))

        for x in reversed(left):
            if x < value:
                vis_left += 1
            elif x == value:
                vis_left += 1
                break
            elif x > value:
                vis_left += 1
                break
            else:
                break
        for x in right:
            if x < value:
                vis_right += 1
            elif x == value:
                vis_right += 1
                break
            elif x > value:
                vis_right += 1
                break
            else:
                break
        for x in reversed(up):
            if x < value:
                vis_up += 1
            elif x == value:
                vis_up += 1
                break
            elif x > value:
                vis_up += 1
                break
            else:
                break
        for x in down:
            if x < value:
                vis_down += 1
            elif x == value:
                vis_down += 1
                break
            elif x > value:
                vis_down += 1
                break
            else:
                break
        result = vis_up * vis_down * vis_left * vis_right
        vis_score.append(result)
        vis_left = 0
        vis_right = 0
        vis_up = 0
        vis_down = 0

print('Highest scenic score:', max(vis_score))
