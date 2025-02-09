from collections import defaultdict
import math

def countBadPairs(nums):
    """
    Count the number of bad pairs. Pair is bad if i < j and j - i != nums[j] - nums[i].
    It means, that we can also count good pairs (nums[i] - i == nums[j] - j)
    :param nums: array
    :return: bad pairs (total - good pair)
    """
    diffs = defaultdict(int)
    for i in range(len(nums)):
        diffs[nums[i] - i] += 1

    goods = 0
    for key in diffs:
        #find all combinations between the same values
        goods += math.comb(diffs[key], 2)

    all = math.comb(len(nums), 2)
    return all - goods


def main():
    nums = [4,1,3,3]
    print(countBadPairs(nums))


if __name__ == '__main__':
    main()