def maxChunksToSorted(arr):
    """
    Return the largest number of chunks we can make to sort the array
    :param arr: start array
    :return: number of chunks
    """
    assert len(arr) > 0

    summ = 0
    ideal_arr = [i for i in range(len(arr))]
    for i in range(len(arr)):
        if sum(ideal_arr[:i]) == sum(arr[:i]):
            summ = summ + 1

    return summ


def main():
    arr = [1, 0, 2, 3, 4]
    print(maxChunksToSorted(arr))


if __name__ == '__main__':
    main()

