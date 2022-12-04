import string
file = open('data.txt')

lines = file.readlines()

res = []
for line in lines:
    compartment_1 = line[0:round(len(line) / 2)]
    compartment_2 = line[round(len(line) / 2):]
    current = []
    for x in compartment_1:
        if compartment_2.find(x) != -1:
            current.append(x)
    res = [*res, *set(current)]

def calc(char):
    pointer = 1
    if char.isupper():
        pointer = 27

    return string.ascii_lowercase.index(char.lower()) + pointer

print(sum([calc(x) for x in res]))
