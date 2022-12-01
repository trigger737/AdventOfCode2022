with open('input', 'r') as file:
    data = file.read().strip().split('\n\n')
    data = [i.split('\n') for i in data]

total_calories = []
for i in data:
    calories = list(map(int, i))
    result = sum(calories)
    total_calories.append(result)

final_result = []
for i in range(3):
    result = max(total_calories)
    total_calories.remove(result)
    final_result.append(result)
print(sum(final_result))
