import string

with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n')

pockets = list(map(lambda x: [x[:len(x)//2], x[len(x)//2:]], data))
# print(pockets)
alphabet = list(string.ascii_letters)
score = 0
for i in pockets:
    letters = []
    # print(i)
    for x in i[0]:
        if x in i[1]:

            if x not in letters:
                letters.append(x)
    # print(letters)
    for z in letters:
        score += alphabet.index(z)+1
print(score)




