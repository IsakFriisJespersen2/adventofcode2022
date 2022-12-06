stacks = [
    ["S", "P", "H", "V", "F", "G"],
    ["M", "Z", "D", "V", "B", "F", "J", "G"],
    ["N", "J", "L", "M", "G"],
    ["P", "W", "D", "V", "Z", "G", "N"],
    ["B", "C", "R", "V"],
    ["Z", "L", "W", "P", "M", "S", "R", "V"],
    ["P", "H", "T"],
    ["V", "Z", "H", "C", "N", "S", "R", "Q"],
    ["J", "Q", "V", "P", "G", "L", "F"],
]

file = open("data.txt")
lines = file.readlines()


def crate_mover_9000(quantity, from_stack, to_stack):
    cargo = stacks[from_stack][:quantity]
    cargo.reverse()
    stacks[from_stack] = stacks[from_stack][quantity:]
    stacks[to_stack] = [*cargo, *stacks[to_stack]]

def crate_mover_9001():
    cargo = stacks[from_stack][:quantity]
    stacks[from_stack] = stacks[from_stack][quantity:]
    stacks[to_stack] = [*cargo, *stacks[to_stack]]


for line in lines:
    _, quantity, _, from_stack, _, to_stack = line.split(" ")
    crate_mover_9001(int(quantity), int(from_stack) - 1, int(to_stack) - 1)

print(stacks)
