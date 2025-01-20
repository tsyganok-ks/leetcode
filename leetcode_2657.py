def findThePrefixCommonArray(A, B):
    """
    Find prefixes for each turn (how many common nums in both arrays)
        len of A and B <= 50
    :param A: first array
    :param B: second array
    :return: array with prefixes
    """
    prefix_common = []
    dict_nums = {x: 0 for x in range(51)}
    counter = 0
    for i in range(len(A)):
        dict_nums[A[i]] += 1
        dict_nums[B[i]] += 1
        if dict_nums[A[i]] == 2 and A[i] != B[i]:
            counter += 1
        if dict_nums[B[i]] == 2 and A[i] != B[i]:
            counter += 1
        if A[i] == B[i]:
            counter += 1
        prefix_common.append(counter)
    return prefix_common


def main():
    A = [2,3,1]
    B = [3,1,2]
    print(findThePrefixCommonArray(A, B))


if __name__ == '__main__':
    main()