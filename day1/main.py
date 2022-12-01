file = open('data.txt')

lines = file.readlines()
calories = []
_sum = 0
for index in range(len(lines)):
    line = lines[index]
    if line == "\n":
        calories.append(_sum)
        _sum = 0
        continue
    _sum += int(line)


print(max(calories))
calories.sort(reverse=True)
print(sum(calories[0:3]))
