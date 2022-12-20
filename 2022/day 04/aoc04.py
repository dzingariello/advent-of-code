# Task 1
def count_fully_contained_pairs(pairs):
  count = 0
  for pair in pairs:
    assignment1, assignment2 = pair.split(',')
    start1, end1 = map(int, assignment1.split('-'))
    start2, end2 = map(int, assignment2.split('-'))
    if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
      count += 1
  return count

# Task 2
def count_overlapping_pairs(pairs):
  count = 0
  for pair in pairs:
    assignment1, assignment2 = pair.split(',')
    start1, end1 = map(int, assignment1.split('-'))
    start2, end2 = map(int, assignment2.split('-'))
    if (start1 <= end2 and start2 <= end1):
      count += 1
  return count


with open('aoc04-input.txt') as f:
    pairs = f.readlines()
    pairs = [pair.strip() for pair in pairs]


print(count_fully_contained_pairs(pairs))
print(count_overlapping_pairs(pairs))