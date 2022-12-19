with open('aoc02-input.txt') as f:
    rounds = f.readlines()
    rounds = [round.strip() for round in rounds]

total_score = 0

rock = 1
paper = 2
scissor = 3

for round in rounds:
    if round == 'A Y':
        total_score += 3 + rock
    elif round == 'B Z':
        total_score += 6 + scissor
    elif round == 'C X':
        total_score += paper
    elif round == 'A X':
        total_score += scissor
    elif round == 'B Y':
        total_score += 3 + paper
    elif round == 'C Z':
        total_score += 6 + rock
    elif round == 'A Z':
        total_score += 6 + paper
    elif round == 'B X':
        total_score += rock
    else:
        total_score += 3 + scissor

print(total_score)