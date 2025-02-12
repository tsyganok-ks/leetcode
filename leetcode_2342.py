from collections import defaultdict

def maximumSum(nums):
    """
    Calculate max sum of a pair with equal sum of digits
    :param nums: array of nums
    :return: max sum
    """
    freq_dict = defaultdict(list)
    for num in nums:
        numbers = str(num)
        summ = sum([int(i) for i in numbers])
        freq_dict[summ].append(num)

    max_sum = -1
    for key in freq_dict:
        if len(freq_dict[key]) >= 2:
            freq_dict[key].sort()
            max_sum = max(max_sum, freq_dict[key][-1] + freq_dict[key][-2])

    return max_sum


def main():
    nums = [9, 18, 43, 36, 13, 7]
    print(maximumSum(nums))


if __name__ == '__main__':
    main()