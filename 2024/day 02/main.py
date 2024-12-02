import os

current_dir = os.path.dirname(__file__)

file_path = os.path.join(current_dir, 'input.txt')


def is_safe_report(nums):
    increasing = all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))
    decreasing = all(nums[i] > nums[i + 1] for i in range(len(nums) - 1))

    valid_diff = all(1 <= abs(nums[i] - nums[i + 1]) <= 3 for i in range(len(nums) - 1))

    return (increasing or decreasing) and valid_diff

safe_reports = 0

with open(file_path, 'r') as file:
    for line_index, line in enumerate(file, start=1):
        nums = list(map(int, line.split()))
        if is_safe_report(nums):
            safe_reports += 1

print(safe_reports)
# Answer: 549

################################################################################

def is_dampened_safe(nums):
    if is_safe_report(nums):
        return True

    for i in range(len(nums)):
        modified_nums = nums[:i] + nums[i+1:]
        if is_safe_report(modified_nums):
            return True
    return False

dampened_safe_count = 0

with open(file_path, 'r') as file:
    for line in file:
        nums = list(map(int, line.split()))
        if is_dampened_safe(nums):
            dampened_safe_count += 1

print(dampened_safe_count)
# Answer: 589