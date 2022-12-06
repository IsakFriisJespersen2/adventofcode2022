import string
file = open('data.txt')

lines = file.readlines()

def calc(char):
    pointer = 1
    if char.isupper():
        pointer = 27

    return string.ascii_lowercase.index(char.lower()) + pointer

def checker(res, compartments: list):
    for x in compartments[0]:
        if any([compartment.find(x) >= 0 for compartment in compartments[1:]]):
            res.append(calc(x))
            break
    return res

# Part 1
res = []
for line in lines:
    compartment_1 = line[:int(len(line) / 2)]
    compartment_2 = line[int(len(line) / 2):]
    res = checker(res, [compartment_1, compartment_2])

print(sum(res))

# Part 2
res = []
i = 1
chunk = []
for line in lines:
    chunk.append(line.split()[0])
    if i % 3 == 0:
        badge = ''.join(set(chunk[0]).intersection(chunk[1]).intersection(chunk[2]))
        print(badge)
        res.append(calc(badge))
        chunk = []
    i += 1


print(sum(res))
