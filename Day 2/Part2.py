with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n')

'''
X - Lose
Y - Draw
Z - Win

A - Rock 1pts
B - Paper 2pts
C - Scissors 3pts
'''

score = 0

pnts = {
    'A': 1,
    'B': 2,
    'C': 3
}

for rnd in data:
    result = rnd[2]
    oponent_choice = rnd[0]

    if result == 'X':
        score += 0
    elif result == 'Y':
        score += 3
    elif result == 'Z':
        score += 6

    if result == 'Y':
        score += pnts[oponent_choice]
    elif result == 'X' and oponent_choice == 'A':
        score += 3
    elif result == 'X' and oponent_choice == 'B':
        score += 1
    elif result == 'X' and oponent_choice == 'C':
        score += 2
    elif result == 'Z' and oponent_choice == 'A':
        score += 2
    elif result == 'Z' and oponent_choice == 'B':
        score += 3
    elif result == 'Z' and oponent_choice == 'C':
        score += 1

print(score)
