import string

with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n')

alphabet = list(string.ascii_letters)
score = 0
packs = []
for i in range(0,len(data),3):
    pack = []
    for x in range(0,3):
        pack.append(data[x+i])
    # print(pack)

    letters = []
    for y in pack[0]:
        if y in pack[1] and y in pack[2]:
            if y not in letters:
                letters.append(y)
    for z in letters:
        score += alphabet.index(z)+1
print(score)
