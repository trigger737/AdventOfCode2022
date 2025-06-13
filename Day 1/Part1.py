import os

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_path, 'r') as file:
    data = file.read().strip().split('\n\n')
    data = [i.split('\n') for i in data]

total_calories = []
for i in data:
    calories = list(map(int, i))
    result = sum(calories)
    total_calories.append(result)

print(max(total_calories))
