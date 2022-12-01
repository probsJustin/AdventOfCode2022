with open('puzzle_day1.txt') as f:
    lines = f.readlines()
current_elf = 0
elves = list()
for x in lines:
    if(x == '\n'):
        elves.append(current_elf)
        current_elf = 0
    else:
        current_elf = current_elf + int(x)

print(max(elves))