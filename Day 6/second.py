with open('input.txt', 'r') as file:
    data = file.read().strip()

buff = []
result = ''
str_len = 14
for letter in data:
    buff.append(letter)
    if len(buff) >= str_len:
        pack = list(dict.fromkeys(buff))
        if len(pack) == str_len:
            result = ''.join(pack)
            break
        buff.pop(0)
print(result, data.find(result) + str_len)
