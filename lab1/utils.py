def in_interval(nums, least, great):
    return sum(1 for elem in nums if (least <= elem < great))


def nums_to_file(nums, file_name):
    with open(file_name, 'w') as f:
        for n in nums:
            f.write(str(n) + ' ')


def nums_from_file(file_name):
    with open(file_name, 'r') as f:
        nums = f.readline()
        nums = nums.split(' ')
        nums.remove('')
        nums = list(map(float, nums))
        return nums


