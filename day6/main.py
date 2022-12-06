file = open("data.txt")
line = file.readline()


def start_of_packet(line, marker_size):
    for i in range(len(line)):
        end = i + marker_size
        substring = [x for x in line[i:end]]
        if len(set(substring)) == marker_size:
            return end


# part 1
marker = start_of_packet(line, 4)
print(marker)

# part 2
marker = start_of_packet(line, 14)
print(marker)


