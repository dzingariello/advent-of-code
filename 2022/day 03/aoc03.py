# Task 1
def find_common_items(rucksacks):
    sum_of_priorities = 0
    for rucksack in rucksacks:
        first_compartment = rucksack[:len(rucksack)//2]
        second_compartment = rucksack[len(rucksack)//2:]
        # Create frequency maps for the items in each compartment
        first_compartment_freq = {}
        second_compartment_freq = {}
        for item in first_compartment:
            if item in first_compartment_freq:
                first_compartment_freq[item] += 1
            else:
                first_compartment_freq[item] = 1
        for item in second_compartment:
            if item in second_compartment_freq:
                second_compartment_freq[item] += 1
            else:
                second_compartment_freq[item] = 1
        
        # Find the items that appear in both compartments
        common_items = []
        for item, count in first_compartment_freq.items():
            if item in second_compartment_freq:
                common_items.append(item)
        
        # Sum up the priorities of the common items
        for item in common_items:
            # Lowercase item types have priorities 1 through 26
            if item.islower():
                sum_of_priorities += ord(item) - ord('a') + 1
            # Uppercase item types have priorities 27 through 52
            else:
                sum_of_priorities += ord(item) - ord('A') + 27
    return sum_of_priorities

# Task 2
def find_badge_items(rucksacks):
  sum_of_priorities = 0
  for i in range(0, len(rucksacks), 3):
    # Create frequency maps for the items in each rucksack
    rucksack1_freq = {}
    rucksack2_freq = {}
    rucksack3_freq = {}
    for item in rucksacks[i]:
      if item in rucksack1_freq:
        rucksack1_freq[item] += 1
      else:
        rucksack1_freq[item] = 1
    for item in rucksacks[i+1]:
      if item in rucksack2_freq:
        rucksack2_freq[item] += 1
      else:
        rucksack2_freq[item] = 1
    for item in rucksacks[i+2]:
      if item in rucksack3_freq:
        rucksack3_freq[item] += 1
      else:
        rucksack3_freq[item] = 1

    # Find the items that appear in all three rucksacks
    common_items = set(rucksack1_freq.keys()) & set(rucksack2_freq.keys()) & set(rucksack3_freq.keys())

    # Sum up the priorities of the common items
    for item in common_items:
      # Lowercase item types have priorities 1 through 26
      if item.islower():
        sum_of_priorities += ord(item) - ord('a') + 1
      # Uppercase item types have priorities 27 through 52
      else:
        sum_of_priorities += ord(item) - ord('A') + 27
  return sum_of_priorities


with open('aoc03-input.txt') as f:
    rucksacks = f.readlines()
    rucksacks = [rucksack.strip() for rucksack in rucksacks]

print(find_common_items(rucksacks))
print(find_badge_items(rucksacks))

