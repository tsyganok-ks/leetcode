def lexicographicallySmallestArray(nums, limit):
    """
    Find such array, where we can swap all numbers if difference between them <= limit
    :param nums: array
    :param limit: limitation
    :return: changed array
    """
    ideal_nums = sorted(nums)

    #Determine groups <= limit to change numbers
    groups = {0:[ideal_nums[0]]}
    dict_group_nums = {ideal_nums[0]:0}
    iter_group = 0
    for i in range(1, len(ideal_nums)):
        if ideal_nums[i] - ideal_nums[i-1] > limit:
            iter_group += 1
            groups[iter_group] = []
        dict_group_nums[ideal_nums[i]] = iter_group
        groups[iter_group].append(ideal_nums[i])

    #Change numbers in their groups
    answ = []
    for i in range(len(nums)):
        group_number = dict_group_nums[nums[i]]
        answ.append(groups[group_number].pop(0))
    return answ


def main():
    nums = [1, 5, 3, 9, 8]
    limit = 2
    print(lexicographicallySmallestArray(nums, limit))


if __name__ == '__main__':
    main()