import os

current_dir = os.path.dirname(__file__)

file_path = os.path.join(current_dir, 'input.txt')

list1 = []
list2 = []

with open(file_path, 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

list1.sort()
list2.sort()

differences = [abs(a - b) for a, b in zip(list1, list2)]

print(sum(differences))
# Answer: 1830467

similarity_scores = []

for num in list1:
    count_in_list2 = list2.count(num)
    similarity_scores.append(num * count_in_list2)

print(sum(similarity_scores))