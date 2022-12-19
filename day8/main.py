file = open("data.txt")
temp = file.read().strip()
forrest = temp.strip().split("\n")

def get_top_bottom(arr, tree_position_x, tree_position_y):
    top = [-1]
    bottom = [-1]
    for y in range(len(arr)):
        if y < tree_position_y:
            top.append(int(arr[y][tree_position_x]))
        elif y > tree_position_y:
            bottom.append(int(arr[y][tree_position_x]))
        continue

    return top, bottom


def get_right_left(row, tree_position_x):
    right = [-1, *row[tree_position_x:]]
    left = [-1, *row[:tree_position_x]]

    return [int(r) for r in right], [int(l) for l in left]


number_of_visible_trees = 0
for y in range(len(forrest)):
    for x in range(len(forrest[y])):
        top, bottom = get_top_bottom(forrest, x, y)
        right, left = get_right_left(forrest[y], x)
        if (
            int(forrest[y][x]) > max(top)
            or int(forrest[y][x]) > max(bottom)
            or int(forrest[y][x]) > max(right)
            or int(forrest[y][x]) > max(left)
        ):
            number_of_visible_trees += 1

print(number_of_visible_trees)
