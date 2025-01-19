def maxChunksToSorted(arr):
    assert len(arr) > 0

    summ = 0
    ideal_arr = [i for i in range(len(arr))]
    for i in range(len(arr)):
        if sum(ideal_arr[:i]) == sum(arr[:i]):
            summ = summ + 1

    return summ