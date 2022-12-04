file = open('data.txt')

lines = file.readlines()
def check_overlap(left, right, checker):
    if left == right:
        return True

    l1, l2 = left.split('-')
    r1, r2 = right.split('-')
    l1, l2 = int(l1), int(l2)
    r1, r2 = int(r1), int(r2)

    return checker(l1, l2, r1, r2)

# Part 1
def inner_overlap(l1, l2, r1, r2):
    is_right_gt = r1 >= l1
    is_left_ls = r2 <= l2
    is_left_gt = l1 >= r1
    is_right_ls = l2 <= r2
    return is_right_gt and is_left_ls or is_left_gt and is_right_ls

# Part 2
def hard_overlap(l1, l2, r1, r2):
    x = r1 <= l1 and r2 >= l1 and r2 <= l2
    y = l1 <= r1 and l2 >= r1 and l2 <= r2
    z = r2 <= l2 and r2 >= l1 and r1 >= l1
    e = l2 <= r2 and l2 >= r1 and l1 >= r1
    return x or y or z or e

count = 0
for line in lines:
    left, right = line.split(',')

    if check_overlap(left, right, inner_overlap) or check_overlap(left, right, hard_overlap):
        count += 1

print(count)





