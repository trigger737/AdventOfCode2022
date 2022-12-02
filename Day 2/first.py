with open('input', 'r') as file:
    data = file.read().strip().split('\n')

'''
X - Rock        1pts
Y - Paper       2pts
Z - Scissors    3pts

A - Rock
B - Paper
C - Scissors

Lost - 0pts
Draw - 3pts
Win - 6pts
'''

score = 0


for rnd in data:
    my_choice = rnd[2]
    oponent_choice = rnd[0]

    if my_choice == 'X' and oponent_choice == 'A':
        score += 3
    elif my_choice == 'Y' and oponent_choice == 'B':
        score += 3
    elif my_choice == 'Z' and oponent_choice == 'C':
        score += 3
    elif my_choice == 'X' and oponent_choice == 'C':
        score += 6
    elif my_choice == 'Y' and oponent_choice == 'A':
        score += 6
    elif my_choice == 'Z' and oponent_choice == 'B':
        score += 6
    else:
        pass

    if my_choice == 'X':
        score += 1
    elif my_choice == 'Y':
        score += 2
    elif my_choice == 'Z':
        score += 3
    else:
        pass


print(score)
