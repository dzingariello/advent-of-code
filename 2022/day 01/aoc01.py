with open('aoc01-input.txt') as f:
    line = f.readline()
    calories = {}
    elf = None
    while line:
        if line.strip() == '':
            elf = None
        else:
            calories_per_item = int(line)
            if elf is None:
                elf = len(calories) + 1
                calories[elf] = 0
            calories[elf] += calories_per_item

        line = f.readline()

max_calories = 0
max_elves = []

for elf, elf_calories in calories.items():
    if not max_elves or elf_calories > min([x[1] for x in max_elves]):
        max_elves.append((elf, elf_calories))
        if len(max_elves) > 3:
            min_calories = min([x[1] for x in max_elves])
            max_elves = [x for x in max_elves if x[1] != min_calories]

max_elves = sorted(max_elves, key=lambda x: x[1], reverse=True)

print(sum([x[1] for x in max_elves[:3]]))
